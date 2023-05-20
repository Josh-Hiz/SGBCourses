What's good about functions?
============================

.. add-css:: 


.. raw:: html

   <form onsubmit="return checkAnswer()">
   <p>Which of the following is true about functions?</p>
   <label><input type="radio" name="answer" value="incorrect">They group code that gets executed multiple times to avoid duplicate code</label>
   <label><input type="radio" name="answer" value="incorrect">They help organize your code to make it easier to read, write, debug, and modify</label>
   <label><input type="radio" name="answer" value="incorrect">They make writing code easier for others since they don't need to know how a function works to use it</label>
   <label><input type="radio" name="answer" value="correct">All of the above</label>
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