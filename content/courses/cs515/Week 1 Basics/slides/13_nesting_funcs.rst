Nesting Function Calls
======================

Just like we can nest arithmetic expressions and use variable names with operators, like in (1 + 2) * 4 or (number_of_tas * 2) we can also use expressions and variables as arguments to functions. In addition, their results can be stored in variables. For example, we could write:

.. code-block:: python

        >>> x = 10
        >>> y = 17
        >>> max(x, y)
        17
        >>> z = max(x, y)
        >>> z + 4
        21

A few more examples:

.. code-block:: python

        >>> min(max(1, 2), 3)
        2
        >>> x = 10
        >>> y = -17
        >>> max(abs(x), abs(y))
        17


.. raw:: html

   <style>
    form {
        margin: 20px;
        padding: 20px;
        border: 1px solid #ccc;
        border-radius: 5px;
    }

    input[type=checkbox] {
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
   <p>Which of the programs below end in valid function calls? Try them out if you're not sure!</p>
   <label><input type="checkbox" name="answer" value="A"><code> max(abs(1) 2)</code> </label>
   <label><input type="checkbox" name="answer" value="B"><code> min(max(1, 2), 300)</code> </label>
   <label><input type="checkbox" name="answer" value="C"><code> x = 100</code><br><code>abs(max(x, 10))</code> </label>
   <label><input type="checkbox" name="answer" value="D"><code> max(max(4, 5), 6)</code> </label>
   <label><input type="checkbox" name="answer" value="E"><code> abs(abs(max(4, 5))</code> </label>
   <label><input type="checkbox" name="answer" value="F"><code> x = abs(-3)</code><br><code>max(x, x + 1)</code> </label>
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
           var correctAnswers = ['B', 'C', 'D', 'F'];
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