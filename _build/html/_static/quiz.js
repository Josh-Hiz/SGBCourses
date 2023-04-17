// Define the Quiz class
class Quiz {
    constructor() {
      this.questions = [];
    }
  
    // Add a multiple choice question to the quiz
    addMultipleChoiceQuestion(question, options, answer) {
      this.questions.push({
        type: "multiple_choice",
        question,
        options,
        answer,
      });
    }
  
    // Add a true/false question to the quiz
    addTrueFalseQuestion(question, answer) {
      this.questions.push({
        type: "true_false",
        question,
        answer,
      });
    }
  
    // Generate the HTML for the quiz
    generateHtml() {
      let html = "";
  
      // Loop through each question in the quiz
      this.questions.forEach((q, index) => {
        html += `<div class="question">`;
  
        // Add the question text
        html += `<h3>${index + 1}. ${q.question}</h3>`;
  
        // Add the answer options
        if (q.type === "multiple_choice") {
          q.options.forEach((option) => {
            html += `
              <label><input type="radio" name="q${index}" value="${option}"> ${option}</label>
            `;
          });
        } else if (q.type === "true_false") {
          html += `
            <label><input type="radio" name="q${index}" value="true"> True</label>
            <label><input type="radio" name="q${index}" value="false"> False</label>
          `;
        }
  
        // Add the submit button
        html += `<button onclick="submitQuiz()">Submit</button>`;
  
        html += `</div>`;
      });
  
      // Add the container for the quiz results
      html += `<div id="quiz-results"></div>`;
  
      return html;
    }
  
    // Check the quiz answers and show the results
    submitQuiz() {
      let score = 0;
      let html = "";
  
      // Loop through each question in the quiz
      this.questions.forEach((q, index) => {
        const selected = document.querySelector(`input[name="q${index}"]:checked`);
  
        // Check if the answer is correct and update the score and HTML string accordingly
        if (selected && selected.value === q.answer) {
          score++;
          html += `<div class="correct">${index + 1}. ${q.question} - ${selected.value} is correct</div>`;
        } else {
          html += `<div class="incorrect">${index + 1}. ${q.question} - ${selected ? selected.value : "No answer"} is incorrect</div>`;
        }
      });
  
      // Show the score and quiz results
      html = `<h2>Score: ${score} / ${this.questions.length}</h2>` + html;
      document.querySelector("#quiz-results").innerHTML = html;
    }
  }
  
  // Initialize the quiz
  const quiz = new Quiz();
  
  // Example usage
  quiz.addMultipleChoiceQuestion("What is the capital of France?", ["Paris", "Berlin", "London", "Madrid"], "Paris");
  quiz.addTrueFalseQuestion("The Earth is flat.", "false");
  
  // Generate the HTML for the quiz and add it to the page
  document.querySelector("#quiz").innerHTML = quiz.generateHtml();
  
  // Bind the submitQuiz method to the window object so it can be called from the HTML
  window.submitQuiz = quiz.submitQuiz.bind(quiz);