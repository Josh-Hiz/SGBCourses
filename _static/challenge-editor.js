const fileSaver = require('file-saver');

var editor = ace.edit("editor");
var output_pane;
var filePath = '/_static/test_files/main.py';

languagePluginLoader.then(() => {
    // pyodide is now ready to use...
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

function openCode(filePath) {
    fetch(filePath)
      .then(response => response.text())
      .then(code => {
        var modelist = ace.require("ace/ext/modelist");
        var modeName = modelist.getModeForPath(filePath).mode;
        console.log(modeName);
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
        alert("Error: " + err)
    });

    let result = await promise;
    if (result) { 
        appendOutput(console.logs.join('\n')); 
        save_code(code_to_run);
    }
}

function save_code(code) {
    var blob = new Blob([code], { type: "text/plain;charset=utf-8" });
    window.saveAs(blob, filePath);
}


document.addEventListener('DOMContentLoaded', (event) => {

    output_pane = document.getElementById("output");

    document.getElementById("run_code").addEventListener('click', function () {
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