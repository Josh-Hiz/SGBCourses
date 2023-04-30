from docutils.parsers.rst import Directive
from docutils.nodes import raw

class AddQuizzCSS(Directive):
    required_arguments = 0
    has_content = True
    
    def run(self):
        html = f"""
        <style>
        form {{
            margin: 20px;
            padding: 20px;
            border: 1px solid #ccc;
            border-radius: 5px;
        }}
        
        label {{
            display: block;
            margin-bottom: 10px;
            font-size: 16px;
        }}

        input[type=text] {{
            width: 100%;
            padding: 12px 20px;
            margin: 8px 0;
            box-sizing: border-box;
            border: 2px solid #ccc;
            border-radius: 4px;
            font-size: 16px;
            background-color: #fff;
            color: #333333;
        }}
        
        input[type=checkbox] {{
            margin: 8px 0;
            box-sizing: border-box;
            border: 2px solid #ccc;
            border-radius: 4px;
            font-size: 16px;
            background-color: #fff;
            color: #333333;
        }}

        button[type=submit] {{
            background-color: #4CAF50;
            color: white;
            padding: 12px 20px;
            border: none;
            border-radius: 4px;
            cursor: pointer;
            font-size: 16px;
        }}
        
        input[type=radio] {{
            margin: 8px 0;
            box-sizing: border-box;
            border: 2px solid #ccc;
            border-radius: 4px;
            font-size: 16px;
            background-color: #fff;
            color: #333333;
        }}

        button[type=submit]:hover {{
            background-color: #45a049;
        }}

        #result {{
            margin-top: 10px;
            font-size: 16px;
            font-weight: bold;
            color: #333333;
        }}

        </style>
        """
        return [raw("", html, format='html')]

def setup(app):
    app.add_directive("add_css",AddQuizzCSS)