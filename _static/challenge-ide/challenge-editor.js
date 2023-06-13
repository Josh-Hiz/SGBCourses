var testFilePath;
var editor = ace.edit("editor");
var output_pane;

function setParams() {
    const queryString = new URLSearchParams(location.search);
    const initCode = queryString.get('initCode');
    const testFile = queryString.get('testFile');
    if (initCode) {
        const decodedCode = decodeURIComponent(initCode);
        console.log(decodedCode)
        editor.setValue(decodedCode);
    }
    if(testFile){
        const decodedTest = decodeURIComponent(testFile);
        testFilePath = decodedTest;
        console.log(testFilePath);
    }
}

loadPyodide().then((pyodide) => {
    // pyodide is now ready to use...
    globalThis.pyodide = pyodide;
    appendOutput('Python ready.\n');
});

console.warn = function(message) {
    console.log(message);
};
  
function appendOutput(msg) {
    // used to add program output to the textarea
    output_pane.value = output_pane.value + '\n' + msg;
    output_pane.scrollTop = output_pane.scrollHeight;
}

function configEditor(){
    // configure the ace editor to make it usable
    editor = ace.edit("editor");
    editor.setTheme("ace/theme/monokai");
    editor.session.setMode("ace/mode/python");
    editor.setShowPrintMargin(false);
    editor.setBehavioursEnabled(true);
    editor.setFontSize(13);
    setParams();
}

function openCode(filePathToUse) {
    getCode(filePathToUse)
      .then(code => {
        var modelist = ace.require("ace/ext/modelist");
        var modeName = modelist.getModeForPath(filePathToUse).mode;
        editor.session.setMode(modeName);
        editor.session.setValue(code);
    })
      .catch(error => {
        console.error('Error occurred while opening the code:', error);
    });
}

async function runCode(code_to_run) {
    // Run the code thats within the editor so students can test
    if(code_to_run == editor.getValue()){
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
        window.pyodide.FS.writeFile("challenge.py", data);
        window.pyodide.FS.writeFile("test.py", testData);
        
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

function saveCode(code) {
    var blob = new Blob([code], { type: "text/plain;charset=utf-8" });
    window.saveAs(blob, 'challenge.py');
}

//make a function getCode that takes in a file path and returns the code in that file as a string to use in ace
async function getCode(codeToGet) {
    try {
      const response = await fetch(codeToGet);
      const data = await response.text();
      return data;
    } catch (error) {
      console.error('Error occurred while opening the code:', error);
    }
}

//codeToSwitch will be a file path
function switchFile(codeToSwitch) {
    getCode(codeToSwitch)
    .then(code => {
        var EditSession = ace.require("ace/edit_session").EditSession;
        var oldSession = editor.getSession();
        //change to new file
        var newSession = new EditSession(code, "ace/mode/python");
        editor.setSession(newSession);
    })
    .catch(error => {
      console.error('Error occurred while opening the code:', error);
    });
}

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
    console.log = function(){
        console.logs.push(Array.from(arguments));
        console.stdlog.apply(console, arguments);
    }
    configEditor(); 
});