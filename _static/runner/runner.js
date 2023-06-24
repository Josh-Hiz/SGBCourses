var editor = ace.edit("editor");
var output_pane;

function setParams() {
    const queryString = new URLSearchParams(location.search);
    const initCode = queryString.get('initCode');

    if (initCode) {
        const decodedCode = decodeURIComponent(initCode);
        editor.setValue(decodedCode);
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

async function runCode(code_to_run) {
    // Run the code thats within the editor so students can test
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