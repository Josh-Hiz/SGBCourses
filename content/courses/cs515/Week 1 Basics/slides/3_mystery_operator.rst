Mystery Operator
================

There are more operators than just the standard four arithmetic operators of + for addition, - for subtraction, * for multiplication, and / for division.

Question
========
Consider this interation:

.. code-block:: python

        >>> 4 ** 2
        16 
        >>> 2 ** 6
        64
        >>> 3 ** 3
        27


.. raw:: html

   <style>
    form {
        margin: 20px;
        padding: 20px;
        border: 1px solid #ccc;
        border-radius: 5px;
    }

    input[type=radio] {
        margin: 8px 0;
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
   <p>What does the <code>**</code> do?</p>
   <label><input type="radio" name="answer" value="incorrect"> Squaring</label>
   <label><input type="radio" name="answer" value="incorrect"> Cubing</label>
   <label><input type="radio" name="answer" value="correct"> Exponentiation</label>
   <label><input type="radio" name="answer" value="incorrect"> I don't know</label>

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
        