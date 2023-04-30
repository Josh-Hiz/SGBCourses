It Dosen't Float!
=================

.. raw:: html

   <form onsubmit="return checkAnswer()">
   <p>Which of the following code segments will evaluate to a floating-point number?<br>(Hint: make the prediction on your own, and test in a Python interpreter if you're not sure.)</p>
   <label><input type="checkbox" name="answer" value="A"><code> int(5 * 5.0)</code> </label>
   <label><input type="checkbox" name="answer" value="B"><code> 5 * 2.5</code> </label>
   <label><input type="checkbox" name="answer" value="C"><code> 5 + 2</code></label>
   <label><input type="checkbox" name="answer" value="D"><code> 5 + 2.0</code> </label>
   <label><input type="checkbox" name="answer" value="E"><code> float(5 * 2)</code> </label>
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
           var correctAnswers = ['A', 'C'];
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
                   <strong>Explanation:</strong><br>
                   Manually converting floats yields an int (A); operations other than <code>/</code> on ints yield ints (C).<br>(B) and (D) promote to floats, while (E) converts.
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