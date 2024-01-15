from docutils.parsers.rst import Directive
from docutils.nodes import raw
import urllib.parse

class ChallengeDirective(Directive):
    optional_arguments = 1
    has_content = True
    option_spec = {'tester': str, 'files': str}
    
    def run(self):
        tester = self.options.get('tester', '')
        code = "\n".join(self.content)
        encoded_code = urllib.parse.quote(code)
        files = self.options.get('files', '')
        files = urllib.parse.quote_plus(files)
        html = f"""
        <div class="challenge-wrapper">
            <iframe class="challengeIDE" src="/_static/Pyodide Tools/challenge-ide/ace_editor.html?testFile={tester}&initCode={encoded_code}&files={files}" height="1200" width="875" title="Challenge"></iframe>
        </div>
        """
        
        return [raw("", html, format="html")]
        
def setup(app):
    app.add_directive("challenge", ChallengeDirective)
    return { 'parallel_read_safe': True }
