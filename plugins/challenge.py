from docutils.parsers.rst import Directive
from docutils.parsers.rst import Directive
from docutils.nodes import raw

class ChallengeDirective(Directive):
    required_arguments = 0
    optional_arguments = 1
    has_content = True
    option_spec = {'tester': str}
    
    def run(self):
        tester = self.options.get('tester', '')
        code = '\n'.join(self.content)
        
        html = f"""
        <iframe id="challenge-iframe" src="/_static/ace_editor.html?testFile='{tester}'&initCode='{code}'" height="800" width="800" title="Challenge"></iframe>
        """
        
        return [raw("", html, format="html")]
        
def setup(app):
    app.add_directive("challenge", ChallengeDirective)