Call Me, Maybe
==============

.. raw:: html

   <style>
    form {
        margin: 20px;
        padding: 20px;
        border: 1px solid #ccc;
        border-radius: 5px;
    }

    input[type=radio] {
        margin: 20px 15px;
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
   <p>Which of the following is the correct Python syntax for a function call?</p>
   <label><input type="radio" name="answer" value="correct"><code>min(4,5)</code></label>
   <label><input type="radio" name="answer" value="incorrect"><code>max</code></label>
   <label><input type="radio" name="answer" value="incorrect"><code>nax(4,5</code></label>
   <label><input type="radio" name="answer" value="incorrect"><code>min 4 5</code></label>
   <button type="submit">Submit Answer</button>
   <p id="result"></p>
   </form>
   
.. raw:: html

   <script>
   function checkAnswer() {
       var userAnswer = document.querySelector('input[name="answer"]:checked');
       if (userAnswer === null) {
           document.getElementById("result").innerHTML = `
           <div class="alert alert-warning">
               <strong>Please select an answer.</strong>
           </div>`;
       } else if (userAnswer.value.toLowerCase() === "correct") {
           document.getElementById("result").innerHTML = `
           <div class="alert alert-success">
               <strong>Correct answer!</strong>
           </div>`;
       } else {
           document.getElementById("result").innerHTML = `
           <div class="alert alert-danger">
               <strong>Sorry, incorrect answer.</strong>
           </div>`;
       }
       return false;
   }
   </script>