from docutils.parsers.rst import Directive
from docutils.nodes import raw


class HtmlQuestionDirective(Directive):
    required_arguments = 3

    def run(self):
        question, correct_answer, explanation = self.arguments
        html = f"""
        <form onsubmit="return checkAnswer()">
        <p>{question}</p>
        <input type="text" id="userAnswer">
        <button type="submit">Submit Answer</button>
        <p id="result"></p>
        </form>

        <script>
        function checkAnswer() {{
            var userAnswer = document.getElementById("userAnswer").value;
            var correctAnswer = "{correct_answer}";
            if (userAnswer.toLowerCase() === correctAnswer.toLowerCase()) {{
                document.getElementById("result").innerHTML = `
                <div class="alert alert-success">
                    <strong>Explanation</strong><br>
                    <pre>
                    {explanation}
                    </pre>
                </div>`;
            }} else {{
                document.getElementById("result").innerHTML = `
                <div class="alert alert-danger">
                    <strong>Sorry, incorrect answer.</strong>
                </div>`;
            }}
            return false;
        }}
        """
        return [raw("", html, format="html")]

def setup(app):
    app.add_directive("free_response", HtmlQuestionDirective)
