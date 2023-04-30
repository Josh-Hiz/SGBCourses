Does It Float Again?
====================

.. raw:: html

   <form onsubmit="return checkAnswer()">
   <p>Which of the following code segments will evaluate to a floating-point number?<br>(Hint: make the prediction on your own, and test in a Python interpreter if you're not sure.)</p>
   <label><input type="checkbox" name="answer" value="A"><code> 5 + 5.0 // 10</code> </label>
   <label><input type="checkbox" name="answer" value="B"><code> 11 * 11 // 10.0</code> </label>
   <label><input type="checkbox" name="answer" value="C"><code> 10 + 2 // 3</code></label>
   <label><input type="checkbox" name="answer" value="D"><code> 5 / 10 // 10</code> </label>
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
           var correctAnswers = ['A', 'B', 'D'];
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
                   <strong>Correct!</strong><br>
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