Escaping Practice
=================

Question 1
==========

.. raw:: html

   <style>
    form {
        margin: 20px;
        padding: 20px;
        border: 1px solid #ccc;
        border-radius: 5px;
    }

    input[type=checkbox] {
        margin: 8px 0;
        box-sizing: border-box;
        border: 2px solid #ccc;
        border-radius: 4px;
        font-size: 16px;
        background-color: #fff;
        color: #333333;
    }

    label {
        display: block;
        margin-bottom: 10px;
        font-size: 16px;
    }

    input[type=text] {
        width: 100%;
        padding: 12px 20px;
        margin: 8px 0;
        box-sizing: border-box;
        border: 2px solid #ccc;
        border-radius: 4px;
        font-size: 16px;
        background-color: #fff;
        color: #333333;
    }

    button[type=submit] {
        background-color: #4CAF50;
        color: white;
        padding: 12px 20px;
        border: none;
        border-radius: 4px;
        cursor: pointer;
        font-size: 16px;
    }

    button[type=submit]:hover {
        background-color: #45a049;
    }

    #result {
        margin-top: 10px;
        font-size: 16px;
        font-weight: bold;
        color: #333333;
    }

    </style>

.. raw:: html

   <form onsubmit="return checkAnswer()">
   <p>Which definitions of s will Python accept?</p>
   <label><input type="checkbox" name="answer" value="A"><code> s = "don't"</code> </label>
   <label><input type="checkbox" name="answer" value="B"><code> s = "don"t"</code> </label>
   <label><input type="checkbox" name="answer" value="C"><code> s = "don\'t"</code></label>
   <label><input type="checkbox" name="answer" value="D"><code> s = 'don\'t'</code> </label>
   <label><input type="checkbox" name="answer" value="E"><code> s = 'don't'</code> </label>
   <button type="submit">Submit Answer</button>
   <p id="result"></p>
   </form>

.. raw:: html

   <script>
   function checkAnswer() {
       var userAnswers = document.querySelectorAll('input[name="answer"]:checked');
       if (userAnswers.length === 0) {
           document.getElementById("result").innerHTML = `
           <div class="alert alert-warning">
               <strong>Please select at least one answer.</strong>
           </div>`;
       } else {
           var correctAnswers = ['A', 'C', 'D'];
           var isCorrect = true;
           var i = 0;
           for (i; i < userAnswers.length; i++) {
               if (!correctAnswers.includes(userAnswers[i].value)) {
                   isCorrect = false;
                   break;
               }
           }
           if(i < correctAnswers.length){
             isCorrect = false;
           }
           if (isCorrect) {
               document.getElementById("result").innerHTML = `
               <div class="alert alert-success">
                   <strong>Correct!</strong>
               </div>`;
           } else {
               document.getElementById("result").innerHTML = `
               <div class="alert alert-danger">
                   <strong>Sorry, incorrect answer.</strong>
               </div>`;
           }
       }
       return false;
   }
   </script>

Question 2
==========

.. raw:: html

   <form onsubmit="return checkFreeResponseAnswer()">
   <p>How would you write the following as a string in Python?<br> 
   <pre>
   <code>
   hello
    world
     how are you?
   </code>
   </pre> <br>
   Just write the string literal, as in <code>"this\tis not  the answer"</code>.
   </p>
   <input type="text" id="userAnswer">
   <button type="submit">Submit Answer</button>
   <p id="freeResponseResult"></p>
   </form>

.. raw:: html

   <script>
   function checkFreeResponseAnswer() {
       var userAnswer = document.getElementById("userAnswer").value;
       var correctAnswer_1 = "INSERT_VALUE_HERE";
       console.log(correctAnswer_1)
       if (userAnswer.toLowerCase() === correctAnswer_1.toLowerCase()) {
           document.getElementById("freeResponseResult").innerHTML = `
           <div class="alert alert-success">
               <strong>Correct!</strong>
           </div>`;
       } else {
           document.getElementById("freeResponseResult").innerHTML = `
           <div class="alert alert-danger">
               <strong>Sorry, incorrect answer.</strong>
           </div>`;
       }
       return false;
   }
   </script>

Question 3
==========

.. raw:: html

   <form onsubmit="return checkFreeResponseAnswer2()">
   <p>How would you write the following as a string in Python?<br> 
   <pre>
   <code>
    "It's a backslash," he said, "you write it like '\'."
   </code>
   </pre> <br>
   Just write the string literal, as in <code>"this\tis not  the answer"</code>.
   </p>
   <input type="text" id="userAnswer_2">
   <button type="submit">Submit Answer</button>
   <p id="freeResponseResult_2"></p>
   </form>

.. raw:: html

   <script>
   function checkFreeResponseAnswer2() {
       var userAnswer = document.getElementById("userAnswer_2").value;
       var correctAnswer_2 = '"It\'s a backslash," he said, "you write it like \'\\\'."';
       console.log(correctAnswer_2)
       if (userAnswer.toLowerCase() === correctAnswer_2.toLowerCase()) {
           document.getElementById("freeResponseResult_2").innerHTML = `
           <div class="alert alert-success">
               <strong>Correct!</strong>
           </div>`;
       } else {
           document.getElementById("freeResponseResult_2").innerHTML = `
           <div class="alert alert-danger">
               <strong>Sorry, incorrect answer.</strong>
           </div>`;
       }
       return false;
   }
   </script>