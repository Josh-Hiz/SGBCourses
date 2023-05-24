/**
 * TODO: UI
 * Display a directory tree and then use the switchFiles() method to switch between files within said directory
 */

/** 
 * TODO: FUNCTIONALITY
 * Figure out how to run test files and append its output
 * 3 Methods to go about how to save files so we run test scripts live:
 * Backend with AJAX requests (Flask most likely)
 * Change how we originally wanted challenges: Have the student upload a file and then run the test script 
 * Use jupyter interface to handle it all
 */

//fileSaver is used to save the code to a file and download it 
const fileSaver = require('file-saver');
// Setup ace variables and the output pane for pyodide
var editor = ace.edit("editor");
var output_pane;
// The following line will essentially be the "file path" input for the RST directive, or 
// we can figure out how to pass arguments into an iframe if thats even possible
var filePath = '/_static/test_files/main.py';
var testFilePath = '/_static/test_files/test.py';

loadPyodide().then((pyodide) => {
    // pyodide is now ready to use...
    globalThis.pyodide = pyodide;
    appendOutput('Python ready.\n');
});

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
    openCode(filePath);
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
    // run the code from the editor and display the output in the textarea
    
    console.logs = [];

    let promise = new Promise((resolve, reject) => {
        window.pyodide.runPython(code_to_run)
        resolve(true)
    }).catch(err => {
        appendOutput(console.logs.join('\n')); 
    });

    let result = await promise;
    if (result) { 
        appendOutput(console.logs.join('\n')); 
    }
}

function saveCode(code) {
    var blob = new Blob([code], { type: "text/plain;charset=utf-8" });
    window.saveAs(blob, filePath);
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

    // Add event listeners for switching files
    document.getElementById("switchButton").addEventListener('click', function () {
        switchFile(testFilePath);
    });

    // Add event listeners for running code
    document.getElementById("run_code").addEventListener('click', function () {
        //Run the getcode function to get the code from the editor
        console.log(editor.getValue());
        runCode(editor.getValue());
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