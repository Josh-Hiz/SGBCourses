Conversions and Promotions
==========================

.. raw:: html

   <style>
    form {
        margin: 20px;
        padding: 20px;
        border: 1px solid #ccc;
        border-radius: 5px;
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

   <form onsubmit="return checkAnswer_1()">
   <p>What does <code>int(10/2.5) / 10</code> evaluate to?</p>
   <input type="text" id="userAnswer_1">
   <button type="submit">Submit Answer</button>
   <p id="result_1"></p>
   </form>

.. raw:: html

   <script>
   function checkAnswer_1() {
       var userAnswer = document.getElementById("userAnswer_1").value;
       var correctAnswer_1 = "0.4";
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
   <p>What does <code>int(10/2.5) * 10</code> evaluate to?</p>
   <input type="text" id="userAnswer_2">
   <button type="submit">Submit Answer</button>
   <p id="result_2"></p>
   </form>

.. raw:: html

   <script>
   function checkAnswer_2() {
       var userAnswer = document.getElementById("userAnswer_2").value;
       var correctAnswer_2 = "40";
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
   <p>What does <code>float(10/2.5) * 10</code> return?</p>
   <input type="text" id="userAnswer_3">
   <button type="submit">Submit Answer</button>
   <p id="result_3"></p>
   </form>

.. raw:: html

   <script>
   function checkAnswer_3() {
       var userAnswer = document.getElementById("userAnswer_3").value;
       var correctAnswer_3 = "40.0";
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
   <p>What does <code>int(10/2.5) // 10</code> evaluate to?</p>
   <input type="text" id="userAnswer_4">
   <button type="submit">Submit Answer</button>
   <p id="result_4"></p>
   </form>

.. raw:: html

   <script>
   function checkAnswer_4() {
       var userAnswer = document.getElementById("userAnswer_4").value;
       var correctAnswer_4 = "0";
       if (userAnswer.toLowerCase() === correctAnswer_4.toLowerCase()) {
           document.getElementById("result_4").innerHTML = `
           <div class="alert alert-success">
               <strong>Correct!</strong>
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
   <p>What does <code>2 * 5 + 10 // 4</code> evaluate to?</p>
   <input type="text" id="userAnswer_5">
   <button type="submit">Submit Answer</button>
   <p id="result_5"></p>
   </form>

.. raw:: html

   <script>
   function checkAnswer_5() {
       var userAnswer = document.getElementById("userAnswer_5").value;
       var correctAnswer_5 = "12";
       if (userAnswer.toLowerCase() === correctAnswer_5.toLowerCase()) {
           document.getElementById("result_5").innerHTML = `
           <div class="alert alert-success">
               <strong>Correct!</strong><br>
           </div>`;
       } else {
           document.getElementById("result_5").innerHTML = `
           <div class="alert alert-danger">
               <strong>Sorry, incorrect answer.</strong>
           </div>`;
       }
       return false;
   }
   </script>

.. raw:: html

   <form onsubmit="return checkAnswer_6()">
   <p>What does <code>2 * 5 + 10 / 4</code> evaluate to?</p>
   <input type="text" id="userAnswer_6">
   <button type="submit">Submit Answer</button>
   <p id="result_6"></p>
   </form>

.. raw:: html

   <script>
   function checkAnswer_6() {
       var userAnswer = document.getElementById("userAnswer_5").value;
       var correctAnswer_5 = "12.5";
       if (userAnswer.toLowerCase() === correctAnswer_5.toLowerCase()) {
           document.getElementById("result_6").innerHTML = `
           <div class="alert alert-success">
               <strong>Correct!</strong><br>
           </div>`;
       } else {
           document.getElementById("result_6").innerHTML = `
           <div class="alert alert-danger">
               <strong>Sorry, incorrect answer.</strong>
           </div>`;
       }
       return false;
   }
   </script>