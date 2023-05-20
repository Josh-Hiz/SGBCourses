from docutils.parsers.rst import Directive
from docutils.nodes import raw


class HtmlQuestionDirective(Directive):
    required_arguments = 0
    optional_arguments = 4
    final_argument_whitespace = True
    option_spec = {
        'file_path': str,
        'test_script_path': str,
        'height': str
    }

    def run(self):
        file_path = self.options.get('file_path', '')
        test_script_path = self.options.get('test_script_path', '')
        height = self.options.get('height', '')
        html = f"""
        <style type="text/css" media="screen">
            #editor {{ 
                position: absolute;
                top: 0;
                right: 0;
                bottom: 0;
                left: 0;
            }}
        </style>
        <body>

        <div id="editor">function foo(items) {{
            
        }}</div>
            
        <script src="/_static/src-noconflict/ace.js" type="text/javascript" charset="utf-8"></script>
        <script>
            var editor = ace.edit("editor");
            editor.setTheme("ace/theme/monokai");
            editor.session.setMode("ace/mode/python");
        </script>
        </body>
        
        """
        return [raw("", html, format="html")]

def setup(app):
    app.add_directive("ace-editor", HtmlQuestionDirective)
