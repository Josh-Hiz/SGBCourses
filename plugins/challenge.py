from docutils.parsers.rst import Directive
from docutils.nodes import raw
import urllib.parse

class ChallengeDirective(Directive):
    optional_arguments = 1
    has_content = True
    option_spec = {'tester': str}
    
    def run(self):
        tester = self.options.get('tester', '')
        code = "\n".join(self.content)
        encoded_code = urllib.parse.quote(code)
        html = f"""
        <iframe src="/_static/Pyodide Tools/challenge-ide/ace_editor.html?testFile={tester}&initCode={encoded_code}" height="1200" width="950" title="Challenge"></iframe>
        """
        
        return [raw("", html, format="html")]
        
def setup(app):
    app.add_directive("challenge", ChallengeDirective)