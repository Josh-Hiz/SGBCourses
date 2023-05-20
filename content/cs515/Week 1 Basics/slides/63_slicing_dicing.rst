Slicing (without Dicing)
========================

Identify what each expression evaluates to, given that `

Identify what each expression evaluates to, given that ``word = 'slicing'``. Please use **single quotes** in your answer.

.. add-css::


.. raw:: html

   <form onsubmit="return checkAnswer_1()">
   <p><code>word[6:7]</code></p>
   <input type="text" id="userAnswer_1">
   <button type="submit">Submit Answer</button>
   <p id="result_1"></p>
   </form>

.. raw:: html

   <script>
   function checkAnswer_1() {
       var userAnswer = document.getElementById("userAnswer_1").value;
       var correctAnswer_1 = "'g'";
       if (userAnswer.toLowerCase() === correctAnswer_1.toLowerCase()) {
           document.getElementById("result_1").innerHTML = `
           <div class="alert alert-success">
               <strong>Correct!</strong>
           </div>`;
       } else {
           document.getElementById("result_1").innerHTML = `
           <div class="alert alert-danger">
               <strong>Sorry, incorrect answer.</strong>
           </div>`;
       }
       return false;
   }
   </script>

.. raw:: html

   <form onsubmit="return checkAnswer_2()">
   <p><code>word[0:2]</code></p>
   <input type="text" id="userAnswer_2">
   <button type="submit">Submit Answer</button>
   <p id="result_2"></p>
   </form>

.. raw:: html

   <script>
   function checkAnswer_2() {
       var userAnswer = document.getElementById("userAnswer_2").value;
       var correctAnswer_2 = "'sl'";
       if (userAnswer.toLowerCase() === correctAnswer_2.toLowerCase()) {
           document.getElementById("result_2").innerHTML = `
           <div class="alert alert-success">
               <strong>Correct!</strong>
           </div>`;
       } else {
           document.getElementById("result_2").innerHTML = `
           <div class="alert alert-danger">
               <strong>Sorry, incorrect answer.</strong>
           </div>`;
       }
       return false;
   }
   </script>

.. raw:: html

   <form onsubmit="return checkAnswer_3()">
   <p><code>word[0:1]</code></p>
   <input type="text" id="userAnswer_3">
   <button type="submit">Submit Answer</button>
   <p id="result_3"></p>
   </form>

.. raw:: html

   <script>
   function checkAnswer_3() {
       var userAnswer = document.getElementById("userAnswer_3").value;
       var correctAnswer_3 = "'s'";
       if (userAnswer.toLowerCase() === correctAnswer_3.toLowerCase()) {
           document.getElementById("result_3").innerHTML = `
           <div class="alert alert-success">
               <strong>Correct!</strong><br>
           </div>`;
       } else {
           document.getElementById("result_3").innerHTML = `
           <div class="alert alert-danger">
               <strong>Sorry, incorrect answer.</strong>
           </div>`;
       }
       return false;
   }
   </script>

.. raw:: html

   <form onsubmit="return checkAnswer_4()">
   <p><code>word[2:5]</code></p>
   <input type="text" id="userAnswer_4">
   <button type="submit">Submit Answer</button>
   <p id="result_4"></p>
   </form>

.. raw:: html

   <script>
   function checkAnswer_4() {
       var userAnswer = document.getElementById("userAnswer_4").value;
       var correctAnswer_4 = "'ici'";
       if (userAnswer.toLowerCase() === correctAnswer_4.toLowerCase()) {
           document.getElementById("result_4").innerHTML = `
           <div class="alert alert-success">
               <strong>Correct!</strong><br>
           </div>`;
       } else {
           document.getElementById("result_4").innerHTML = `
           <div class="alert alert-danger">
               <strong>Sorry, incorrect answer.</strong>
           </div>`;
       }
       return false;
   }
   </script>

.. raw:: html

   <form onsubmit="return checkAnswer_5()">
   <p><code>word[0:len(word)]</code></p>
   <input type="text" id="userAnswer_5">
   <button type="submit">Submit Answer</button>
   <p id="result_5"></p>
   </form>

.. raw:: html

   <script>
   function checkAnswer_5() {
       var userAnswer = document.getElementById("userAnswer_5").value;
       var correctAnswer_5 = "'slicing'";
       if (userAnswer.toLowerCase() === correctAnswer_5.toLowerCase()) {
           document.getElementById("result_5").innerHTML = `
           <div class="alert alert-success">
               <strong>Correct!</strong><br>
           </div>`;
       } else {
           document.getElementById("result_4").innerHTML = `
           <div class="alert alert-danger">
               <strong>Sorry, incorrect answer.</strong>
           </div>`;
       }
       return false;
   }
   </script>