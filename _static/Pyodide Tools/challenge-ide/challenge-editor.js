// Variable to hold the literal path for test file
var testFilePath;
// Variable to hold the Ace Editor container
var editor = ace.edit("editor");
// Variable to hold the output pane
var output_pane;
// Variable to hold a list of file paths for any extra modules if any to load
var modules;
// Variable to hold the dropdown menu
var dropdown = document.getElementById("module-select");
var fileNames = [];
/**
 * Sets the initial variables above except output_pane and 
 * will decode the URI components initCode and testFile, if
 * no test file exists, the "Run" button will not display.
 */
function setParams() {
    const queryString = new URLSearchParams(location.search);
    const initCode = queryString.get('initCode');
    const testFile = queryString.get('testFile');
    const files = queryString.get('files');

    if(localStorage.getItem("code") == null){
        // Check if there is any code in the quert string
        if (initCode) {
            const decodedCode = decodeURIComponent(initCode);
            // console.log(decodedCode)
            editor.setValue(decodedCode);
        }
        // Check if there is a test file in the query string
        if(testFile != ''){
            const decodedTest = decodeURIComponent(testFile);
            testFilePath = decodedTest;
            // console.log(testFilePath);
        } else {
            // If there is no test file, remove the run button
            const element = document.getElementById("run_code");
            element.remove();
        }

        if(files){
            createModuleList(files);
        }
    } else {
        editor.setValue(localStorage.getItem("code"));

        // Check if there is a test file in the query string
        if(testFile != ''){
            const decodedTest = decodeURIComponent(testFile);
            testFilePath = decodedTest;
            // console.log(testFilePath);
        } else {
            // If there is no test file, remove the run button
            const element = document.getElementById("run_code");
            element.remove();
        }

        if(files){
            createModuleList(files);
        }
    }
}

// As per the documentation for Pyodide, this will load the Python interpreter
// through WASM and create an Emscripten virtual file system
loadPyodide().then((pyodide) => {
    // pyodide is now ready to use...
    globalThis.pyodide = pyodide;
    appendOutput('Python ready.\n');
});

// Override console.warn so that anything logged will go to textarea
console.warn = function(message) {
    console.log(message);
};

/**
 * Push everything that is logged to the console to an array
 * and then append it to the output pane
 * @param {String} msg  Anything that is logged to console
 */
function appendOutput(msg) {
    // used to add program output to the textarea
    output_pane.value = output_pane.value + '\n' + msg;
    output_pane.scrollTop = output_pane.scrollHeight;
}

function createModuleList(modules) {
    modules = modules.split('\n');
    //Get the file name from path, it is everything from the last letter to the first backslash next to it
    for(let i = 0; i < modules.length; i++){
        var fileName = modules[i].substring(modules[i].lastIndexOf('/') + 1);
        fileNames[i] = fileName;
    }

    //Initialize event listener for dropdown
    dropdown.addEventListener('change', function () {
        saveSession(dropdown.value,editor.getValue());
    });
    dropdown.style.visibility = "visible";
    for(let i = 0; i < modules.length; i++){
        var fileName = fileNames[i];
        var element = document.createElement("option");
        element.textContent = fileName;
        dropdown.appendChild(element);
        element.value = fileNames[i];
    }
    //Init first session
    saveSession(fileNames[0],editor.getValue());
}

/**
 * Standard configuration of the Ace editor as per the documentation
 */
function configEditor(){
    // Place the editor to a container of ID "editor"
    editor = ace.edit("editor");
    // Sets the theme to Xcode
    editor.setTheme("ace/theme/xcode");
    // Sets the language mode to Python for syntax highlighting
    editor.session.setMode("ace/mode/python");
    // Disable the print margin
    editor.setShowPrintMargin(false);
    // Enable soft tabs
    editor.setBehavioursEnabled(true);
    // Set the font size to 13px
    editor.setFontSize(13);
    // Calls setParams so the editor can pick up the test file and set its initial code
    setParams();
}

/**
 * Will open any .py file from the literal path provided and set the 
 * ace editor value to all python code in the file
 * @param {String} filePathToUse Literal path to the file to open
 */
function openCode(filePathToUse) {
    // Call getCode to grab the literal code from the file
    getCode(filePathToUse)
      .then(code => {
        var modelist = ace.require("ace/ext/modelist");
        // Detect if the file is a python file and set the mode to Python
        var modeName = modelist.getModeForPath(filePathToUse).mode;
        // Set the new mode and value of the editor
        editor.session.setMode(modeName);
        editor.session.setValue(code);
    })
      .catch(error => {
        console.error('Error occurred while opening the code:', error);
    });
}

/**
 * Async function that will run the code that is in the ace editor
 * @param {*} code_to_run This will be derived from the decoded URI component and come from whatever is in ace editor
 */
async function runCode(code_to_run) {
    // Run the code thats within the editor so students can test
    if(fileNames && testFilePath == '') {
        console.logs = [];
        let currentFile = dropdown.value;
        let promise = new Promise((resolve, reject) => {
            window.pyodide.runPython(`
                exec(open('${currentFile}').read())
                import sys
                sys.modules.pop("${currentFile}", None)
            `)
            resolve(true)
        }).catch(err => {
            console.log(err);
            appendOutput(console.logs.join('\n')); 
        });
    
        let result = await promise;
        if (result) { 
            appendOutput(console.logs.join('\n')); 
        }
    } else if(code_to_run == editor.getValue()){
        console.logs = [];

        let promise = new Promise((resolve, reject) => {
            window.pyodide.runPython(code_to_run)
            resolve(true)
        }).catch(err => {
            console.log(err);
            appendOutput(console.logs.join('\n')); 
        });
    
        let result = await promise;
        if (result) { 
            appendOutput(console.logs.join('\n')); 
        }
    } else {
        console.logs = [];
        var data = editor.getValue(); 
        var testData = code_to_run;
        
        // Write both the challenge and test code to the virtual file system
        window.pyodide.FS.writeFile("challenge.py", data);
        window.pyodide.FS.writeFile("test.py", testData);
        
        // Run the test file and then delete from the file system
        let promise = new Promise((resolve, reject) => {
            window.pyodide.runPython(`
                exec(open('test.py').read())
                import sys
                sys.modules.pop("challenge", None)
                sys.modules.pop("test", None)
                `)
            resolve(true)
        }).catch(err => {
            console.log(err);
            appendOutput(console.logs.join('\n')); 
        });
        
        let result = await promise;
        if (result) { 
            appendOutput(console.logs.join('\n')); 
        }
    }
}

/**
 * Function to save a .py file from the editor so users can download their code
 * @param {*} code The code that is in the editor
 */
function saveCode(code) {
    var blob = new Blob([code], { type: "text/plain;charset=utf-8" });
    window.saveAs(blob, 'challenge.py');
}

/**
 * Grabs and returns the code from the file that is passed in as a string literal
 * @param {*} codeToGet Literal file path to the file to open
 * @returns Code from the file that is passed in
 */
async function getCode(codeToGet) {
    try {
      const response = await fetch(codeToGet);
      const data = await response.text();
      return data;
    } catch (error) {
      console.error('Error occurred while opening the code:', error);
    }
}

/**
 * Experimental function to test changing the file in the editor in live time
 * @param {*} codeToSwitch Literal file path to the file to open
 */
// Object to store sessions
var sessions = {};

function saveSession(fileName, codeToSwitch) {
    // Save the current session to the file system
    var currentSessionPath = editor.session.$orig;
    if(currentSessionPath){
        window.pyodide.FS.writeFile(currentSessionPath, editor.getValue());
    } 
    // Check if session already exists for this file, if so, switch to it
    if(sessions[fileName]){
        editor.setSession(sessions[fileName]);
    }else{
        // If session doesn't exist, create a new one
        var EditSession = ace.require("ace/edit_session").EditSession;
        //create new session, set the returned code to new session
        var newSession = new EditSession(codeToSwitch, "ace/mode/python");
        newSession.$orig = fileName;
        // Cache the session
        sessions[fileName] = newSession;
        // Set new session to editor
        editor.setSession(newSession);
    }
}

function saveToLocalDB() {
    // Get the code from the editor and put it in local storage
    var code = editor.getValue();
    localStorage.setItem("code", code);
}

// All event listeners for the buttons
document.addEventListener('DOMContentLoaded', (event) => {
    output_pane = document.getElementById("output");
    // Add event listeners for downloading code
    document.getElementById("downloadButton").addEventListener('click', function () {
        saveCode(editor.getValue());
    });
    // Add event listeners for running the code the user types
    document.getElementById("runButton").addEventListener('click', function () {
        runCode(editor.getValue());
    });

    // Add event listeners for the clear button
    document.getElementById("clearButton").addEventListener('click', function () {
        output_pane.value = '';
    });

    // Add event listeners for saving to local storage
    document.getElementById("savecode").addEventListener('click', function () {
        saveToLocalDB();
    });

    // Add event listeners for running the test script
    document.getElementById("run_code").addEventListener('click', function () {
        
        //Run the getcode function to get the code from the editor
        getCode(testFilePath)
        .then(code => {
            console.log(code)
            runCode(code);
        }) 
        .catch(error => {
            console.error('Error occurred while opening the code:', error);
        });
        
    });
    
    // Capture the output from Pyodide and add it to an array
    console.stdlog = console.log.bind(console);
    console.logs = [];
    // Override log function
    console.log = function(){
        console.logs.push(Array.from(arguments));
        console.stdlog.apply(console, arguments);
    }
    configEditor(); 
});