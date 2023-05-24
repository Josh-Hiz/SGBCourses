from docutils.parsers.rst import Directive
from docutils.nodes import raw
from docutils import nodes
from docutils.statemachine import StringList

class HtmlQuestionDirective(Directive):
    has_content = True

    def run(self):
        code = '\n'.join(self.content)

        html = f"""
        <style>
        #editor {{
            position: absolute;
            top: 0;
            right: 0;
            bottom: 0;
            left: 0;
            width: 1225px;
            height: 500px;
        }}

        .container {{
            width: 80%;
            height: 500px;
            margin: auto;
            padding: 10px;
        }}
        .one {{
            width: 50%;
            height: 500px;
            float: left;
        }}
        .two {{
            margin-left: 50%;
            height: 500px;
       }}

        #run_code {{
            border-radius: 4px; /* Adjust the value to change the roundness of the corners */
            padding: 10px 20px;
            background-color: #408ddf;
            color: white;
            font-size: 16px;
            border: none;
            cursor: pointer;
        }}
        </style>
        <body>
                <div class="container">
                    <div class="one">
                        <pre id="editor" style="width: 750px;height:500px;"></pre>
                    </div>
                </div>

                <button id="run_code">Mark</button><br>

                <br>

                <textarea rows=10 cols=30 id=output style="margin: 0px; width: 750px; height: 500px;">Loading and compiling...</textarea><br>

            
            <script src="https://cdnjs.cloudflare.com/ajax/libs/ace/1.4.4/ace.js"></script>
            <script src="https://cdnjs.cloudflare.com/ajax/libs/ace/1.4.4/ext-static_highlight.js"></script>
            <script src="https://cdnjs.cloudflare.com/ajax/libs/ace/1.4.4/ext-modelist.js"></script>
            <script src="https://cdn.jsdelivr.net/pyodide/v0.23.2/full/pyodide.js"></script>
             
            <script>
            // Setup ace variables and the output pane for pyodide
            var editor = ace.edit("editor");
            var output_pane;

            loadPyodide().then((pyodide) => {{
                // pyodide is now ready to use...
                globalThis.pyodide = pyodide;
                appendOutput('Python ready.\n');
            }});

            function appendOutput(msg) {{
                // used to add program output to the textarea
                output_pane.value = output_pane.value + '\n' + msg;
                output_pane.scrollTop = output_pane.scrollHeight;
            }}

            function configEditor(){{
                // configure the ace editor to make it usable
                editor = ace.edit("editor");
                editor.setTheme("ace/theme/xcode");
                editor.session.setMode("ace/mode/python");
                editor.setShowPrintMargin(false);
                editor.setBehavioursEnabled(true);
                editor.setFontSize(13);
                editor.setValue('{code}')
                
            }}

            async function runCode(code_to_run) {{
                // run the code from the editor and display the output in the textarea
                console.logs = [];

                let promise = new Promise((resolve, reject) => {{
                    window.pyodide.runPython(code_to_run)
                    resolve(true)
                }}).catch(err => {{
                    console.log(err);
                    appendOutput(console.logs.join('\n')); 
                }});

                let result = await promise;
                if (result) {{
                    appendOutput(console.logs.join('\n')); 
                }}
            }}

            document.addEventListener('DOMContentLoaded', (event) => {{

                output_pane = document.getElementById("output");
                
                // Add event listeners for running code
                document.getElementById("run_code").addEventListener('click', function () {{
                    //Run the getcode function to get the code from the editor
                    runCode(editor.getValue());
                }});

                // Capture the output from Pyodide and add it to an array
                console.stdlog = console.log.bind(console);
                console.logs = [];
                console.log = function(){{
                    console.logs.push(Array.from(arguments));
                    console.stdlog.apply(console, arguments);
                }}
                
                configEditor();
            }});
            </script>
        </body>
        """
        iframe_html = f"""<iframe srcdoc="{html}" width="100%" height="100%" frameborder="0" allowfullscreen></iframe>"""
        return [raw("", html, format="html")]

def setup(app):
    app.add_directive("runner", HtmlQuestionDirective)