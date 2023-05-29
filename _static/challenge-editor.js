var testFilePath = "/_static/cs515_challenges/Week1/Challenge12/test_cube.py";

async function getParams() {
    var params = location.href.split('?')[1];
    var data = {};

    if (params) {
        params = params.split('&');

        for (var i = 0; i < params.length; i++) {
            var param = params[i].split('=');
            var paramName = decodeURIComponent(param[0]);
            var paramValue = decodeURIComponent(param[1]);
            data[paramName] = paramValue;
        }
    }
    return data['testFile'];
}

//fileSaver is used to save the code to a file and download it 
const fileSaver = require('file-saver');
// Setup ace variables and the output pane for pyodide
var editor = ace.edit("editor");
var output_pane;
// The following line will essentially be the "file path" input for the RST directive, or 
// we can figure out how to pass arguments into an iframe if thats even possible

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
    //Fix indentation issue with ace editor, not really the best solution but it works
    var code = editor.getValue();
    var lines = code.split("\n");
    var minIndent = null;
    for (var i = 0; i < lines.length; i++) {
        var line = lines[i];
        if (line.trim().length > 0) {
            var indent = line.search(/\S/);
            if (minIndent === null || (indent !== -1 && indent < minIndent)) {
                minIndent = indent;
            }
        }
    }
    if (minIndent !== null) {
        for (var i = 0; i < lines.length; i++) {
            if (lines[i].trim().length > 0) {
                lines[i] = lines[i].slice(minIndent);
            }
        }
        code = lines.join('\n');
        editor.setValue(code);
    }
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
        let chalStr = new TextDecoder().decode(window.pyodide.FS.readFile("challenge.py"));
        let testStr = new TextDecoder().decode(window.pyodide.FS.readFile("test.py"));
        
        console.log(chalStr);
        console.log(testStr);

        let promise = new Promise((resolve, reject) => {
            window.pyodide.runPython("exec(open('test.py').read())")
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

    document.getElementById("runButton").addEventListener('click', function () {
        runCode(editor.getValue());
    });
    
    // Add event listeners for running code
    document.getElementById("run_code").addEventListener('click', function () {
        //Run the getcode function to get the code from the editor
        getCode(testFilePath)
        .then(code => {
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