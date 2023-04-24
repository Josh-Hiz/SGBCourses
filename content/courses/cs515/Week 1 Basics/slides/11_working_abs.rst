Working on Your Abs
===================

We saw some examples for the ``abs`` function:

.. code-block:: python

        >>> abs(-3)
        3
        >>> abs(3)
        3
        >>> min(1,4)
        1
        >>> min(-3,7)
        -3

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
   <p>Which is the best (i.e., most accurate) documentation for <code>abs?</code> Try out more examples in your own workspace if you're not sure!</p>
   <label><input type="radio" name="answer" value="incorrect"><code>abs(n,m)</code><br> abs takes two numbers n and m, and produces the absolute value of n</label>
   <label><input type="radio" name="answer" value="incorrect"><code>abs(n)</code><br> abs takes a number n and produces -n</label>
   <label><input type="radio" name="answer" value="incorrect"><code>abs(n,m)</code><br> abs takes two numbers n and m, and produces m</label>
   <label><input type="radio" name="answer" value="incorrect"><code>abs(n,m)</code><br> abs takes two numbers n and m, and produces n</label>
   <label><input type="radio" name="answer" value="correct"><code>abs(n,m)</code><br> abs takes a number n and produces the absolute value of n</label>

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