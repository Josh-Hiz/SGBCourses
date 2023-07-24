from docutils.parsers.rst import Directive
from docutils.nodes import raw
import urllib.parse

class ChallengeDirective(Directive):
    optional_arguments = 1
    has_content = True
    option_spec = {'answer': str, 'regex':str}
    
    def run(self):
        answer = self.options.get('answer', '')
        isRegex = self.options.get('regex', '')
        code = "\n".join(self.content)
        encoded_code = urllib.parse.quote(code)
        encoded_answer = urllib.parse.quote_plus(answer)
        html = f"""
        <iframe width=900px height=400px src="/_static/Quiz Tools/Free Response/index.html?answer={encoded_answer}&initCode={encoded_code}&isRegex={isRegex}" allowfullscreen="true"></iframe>
        """
        
        return [raw("", html, format="html")]
        
def setup(app):
    app.add_directive("free-r", ChallengeDirective)