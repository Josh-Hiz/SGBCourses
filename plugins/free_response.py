from docutils.parsers.rst import Directive
from docutils.nodes import raw


class HtmlQuestionDirective(Directive):
    required_arguments = 0
    optional_arguments = 4
    final_argument_whitespace = True
    option_spec = {
        'question': str,
        'correct_answer': str,
        'explanation': str,
        'question_num': str,
    }

    def run(self):
        question = self.options.get('question', '')
        correct_answer = self.options.get('correct_answer', '')
        explanation = self.options.get('explanation', '')
        question_num = self.options.get('question_num','')
        html = f"""
        <form onsubmit="return checkAnswer_{question_num}()">
        <p>{question}</p>
        <input type="text" id="userAnswer_{question_num}">
        <button type="submit">Submit Answer</button>
        <p id="result_{question_num}"></p>
        </form>

        <script>
        function checkAnswer_{question_num}() {{
            var userAnswer = document.getElementById("userAnswer_{question_num}").value;
            var correctAnswer_{question_num} = "{correct_answer}";
            if (userAnswer.toLowerCase() === correctAnswer_{question_num}.toLowerCase()) {{
                document.getElementById("result_{question_num}").innerHTML = `
                <div class="alert alert-success">
                    <strong>Explanation</strong><br>
                    <pre>
                    {explanation}
                    </pre>
                </div>`;
            }} else {{
                document.getElementById("result_{question_num}").innerHTML = `
                <div class="alert alert-danger">
                    <strong>Sorry, incorrect answer.</strong>
                </div>`;
            }}
            return false;
        }}
        </script>
        """
        return [raw("", html, format="html")]

def setup(app):
    app.add_directive("free-response", HtmlQuestionDirective)
