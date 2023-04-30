Validating Values
=================

.. add_css::




.. code-block:: python

    if x > 100 and x < 200:
        print("The value of x is valid")


.. raw:: html

   <form onsubmit="return checkAnswer()">
   <p>Given the following if-statement above, which values of x will result in "The value of x is valid" being printed?</p>
   <label><input type="checkbox" name="answer" value="A"> 139</label>
   <label><input type="checkbox" name="answer" value="B"> 111</label>
   <label><input type="checkbox" name="answer" value="C"> 50</label>
   <label><input type="checkbox" name="answer" value="D"> 200</label>
   <label><input type="checkbox" name="answer" value="E"> 100</label>
   <label><input type="checkbox" name="answer" value="E"> 203</label>
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
           var correctAnswers = ['A', 'B'];
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