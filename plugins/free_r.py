from docutils.parsers.rst import Directive
from docutils.nodes import raw
import urllib.parse

class ChallengeDirective(Directive):
    optional_arguments = 1
    has_content = True
    option_spec = {'answer': str}
    
    def run(self):
        answer = self.options.get('answer', '')
        code = "\n".join(self.content)
        encoded_code = urllib.parse.quote(code)
        html = f"""
        <iframe src="/_static/free_response/index.html?answer={answer}&initCode={encoded_code}" height="450" width="800" title="Free-Response"></iframe>
        """
        
        return [raw("", html, format="html")]
        
def setup(app):
    app.add_directive("free-r", ChallengeDirective)