from docutils.parsers.rst import Directive
from docutils.nodes import raw
from docutils import nodes
from docutils.statemachine import StringList

class HtmlQuestionDirective(Directive):
    has_content = True
    optional_arguments = 1
    option_spec = {
        'tester': str,
    }


    def run(self):
        code = '\n'.join(self.content)
        testFilePath = self.options.get('tester', '')
        
        html = f"""
        <button>Not ready yet></button>
        """
        return [raw("", html, format="html")]

def setup(app):
    app.add_directive("runner", HtmlQuestionDirective)