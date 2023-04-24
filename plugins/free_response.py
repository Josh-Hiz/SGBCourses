from docutils.parsers.rst import Directive
from docutils.nodes import raw


class HtmlQuestionDirective(Directive):
    required_arguments = 3

    def run(self):
        question, correct_answer, explanation = self.arguments
        html = f"""
        <style>
        form {{
            margin: 20px;
            padding: 20px;
            border: 1px solid #ccc;
            border-radius: 5px;
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

        button[type=submit] {{
            background-color: #4CAF50;
            color: white;
            padding: 12px 20px;
            border: none;
            border-radius: 4px;
            cursor: pointer;
            font-size: 16px;
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
