Viral Twitter Math Problem
==========================

.. code-block:: python

    41 // 2 ** 3 - 4 * 2 + (9 % 5)

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

   <form onsubmit="return checkAnswer()">
   <p>What does the following Python expression above evaluate to? (For maximum learning, try to work it out yourself!)</p>
   <input type="text" id="userAnswer">
   <button type="submit">Submit Answer</button>
   <p id="result"></p>
   </form>

.. raw:: html

   <script>
   function checkAnswer() {
       var userAnswer = document.getElementById("userAnswer").value;
       var correctAnswer = "1";
       if (userAnswer.toLowerCase() === correctAnswer.toLowerCase()) {
           document.getElementById("result").innerHTML = `
           <div class="alert alert-success">
               <strong>Explanation</strong><br>
               <pre>
               41 // 2 ** 3 - 4 * 2 + ( 9 % 5 ) evaluates to
               41 // 2 ** 3 - 4 * 2 + 4 evaluates to
               41 // 8 - 4 * 2 + 4 evaluates to
               5 - 4 * 2 + 4 evaluates to
               5 - 8 + 4 evaluates to
               -3 + 4 evaluates to
               1
               </pre>
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