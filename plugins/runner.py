from docutils.parsers.rst import Directive
from docutils.nodes import raw
import urllib.parse

class RunnerDirective(Directive):
    has_content = True

    def run(self):
        code = "\n".join(self.content)
        encoded_code = urllib.parse.quote(code)
        html = f"""
        <div class="code-runner-wrapper">
            <iframe class="code-runner" src="/_static/Pyodide Tools/runner/runner.html?initCode={encoded_code}" height="500" width="875" title="Runner"></iframe>
        </div>
        """
        return [raw("", html, format="html")]
        
def setup(app):
    app.add_directive("runner", RunnerDirective)