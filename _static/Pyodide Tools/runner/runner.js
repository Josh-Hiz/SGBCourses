var editor = ace.edit("editor");
var output_pane;
var wordData; 

function setParams() {
    const queryString = new URLSearchParams(location.search);
    const initCode = queryString.get('initCode');

    if (initCode) {
        const decodedCode = decodeURIComponent(initCode);
        editor.setValue(decodedCode);
    }

    getCode('words')
        .then(code => {
            wordData = code;
        }) 
        .catch(error => {
            console.error('Error occurred while opening the code:', error);
    });    
}

loadPyodide().then((pyodide) => {
    // pyodide is now ready to use...
    globalThis.pyodide = pyodide;
    appendOutput('Python ready.\n');
});

// Override console.warn so that anything logged will go to textarea
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
    editor.setTheme("ace/theme/xcode");
    editor.session.setMode("ace/mode/python");
    editor.setShowPrintMargin(false);
    editor.setBehavioursEnabled(true);
    editor.setFontSize(13);
    editor.setAnimatedScroll(true);
    editor.setAutoScrollEditorIntoView(true);
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

// Function to write all directories I would want into the file system
var executed = false;
function createDirectories() {
    if(!executed) {
        executed=true
    window.pyodide.FS.mkdir('/usr');
    window.pyodide.FS.mkdir('/usr/share');
    window.pyodide.FS.mkdir('/usr/share/dict');
    window.pyodide.FS.writeFile("/usr/share/dict/words", wordData);
    }
}

async function runCode(code_to_run) {
    // Run the code thats within the editor so students can test
    console.logs = [];
    createDirectories();
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

document.addEventListener('DOMContentLoaded', (event) => {
    output_pane = document.getElementById("output");

    // Add event listeners for running the code the user types
    document.getElementById("runButton").addEventListener('click', function () {
        runCode(editor.getValue());
    });

    // Add event listeners for the clear button
    document.getElementById("clearButton").addEventListener('click', function () {
        output_pane.value = '';
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