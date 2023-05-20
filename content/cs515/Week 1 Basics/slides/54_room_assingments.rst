Room Assignments
================

Given the following function assign_room(num_students), identify what each function calls will be return.

.. code-block:: python

    def assign_room(num_students):
        if num_students <= 146:
            return "GS 216"
        elif num_students <= 196:
            return "Babbio"
        elif num_students <= 295:
            return "Pier A"
        return "no room"

.. add-css:: 



.. raw:: html

   <form onsubmit="return checkAnswer_1()">
   <p>What will <code>assign_room(100)</code> return?</p>
   <input type="text" id="userAnswer_1">
   <button type="submit">Submit Answer</button>
   <p id="result_1"></p>
   </form>

.. raw:: html

   <script>
   function checkAnswer_1() {
       var userAnswer = document.getElementById("userAnswer_1").value;
       var correctAnswer_1 = '"GS 216"';
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
   <p>What will <code>assign_room(150)</code> return?</p>
   <input type="text" id="userAnswer_2">
   <button type="submit">Submit Answer</button>
   <p id="result_2"></p>
   </form>

.. raw:: html

   <script>
   function checkAnswer_2() {
       var userAnswer = document.getElementById("userAnswer_2").value;
       var correctAnswer_2 = '"Babbio"';
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
   <p>What will <code>assign_room(200)</code> return?</p>
   <input type="text" id="userAnswer_3">
   <button type="submit">Submit Answer</button>
   <p id="result_3"></p>
   </form>

.. raw:: html

   <script>
   function checkAnswer_3() {
       var userAnswer = document.getElementById("userAnswer_3").value;
       var correctAnswer_3 = '"Pier A"';
       if (userAnswer.toLowerCase() === correctAnswer_3.toLowerCase()) {
           document.getElementById("result_3").innerHTML = `
           <div class="alert alert-success">
               <strong>Explanation</strong><br>
               <code>int</code> truncates.
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
   <p>What will <code>assign_room(300)s</code> return?</p>
   <input type="text" id="userAnswer_4">
   <button type="submit">Submit Answer</button>
   <p id="result_4"></p>
   </form>

.. raw:: html

   <script>
   function checkAnswer_4() {
       var userAnswer = document.getElementById("userAnswer_4").value;
       var correctAnswer_4 = '"no room"';
       if (userAnswer.toLowerCase() === correctAnswer_4.toLowerCase()) {
           document.getElementById("result_4").innerHTML = `
           <div class="alert alert-success">
               <strong>Explanation</strong><br>
               <code>float</code>s must have a decimal point in them.
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