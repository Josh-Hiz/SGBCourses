Safe Indexing
=============

.. add-css::


.. code-block:: python

    college = "Stevens"

.. raw:: html

   <form onsubmit="return checkAnswer()">
   <p>Choose all of the following that are valid and will NOT cause an index out of bounds error (using the variable above).</p>
   <label><input type="checkbox" name="answer" value="A"><code> college[7]</code> </label>
   <label><input type="checkbox" name="answer" value="B"><code> college[len(college)-1]</code> </label>
   <label><input type="checkbox" name="answer" value="C"><code> college[-1]</code></label>
   <label><input type="checkbox" name="answer" value="D"><code> college[len(college)]</code> </label>
   <label><input type="checkbox" name="answer" value="E"><code> college[0]</code> </label>
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
           var correctAnswers = ['B', 'C','E'];
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