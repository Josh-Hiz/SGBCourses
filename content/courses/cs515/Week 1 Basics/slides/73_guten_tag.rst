Guten Tag!
==========

.. add-css::


.. code-block:: python

    def print_two(string1, string2):
        print(string1 + " " + string2)
        return

    string1 = "Buenos"
    string2 = "Dias"
    print_two(string2, string1)

.. raw:: html

   <form onsubmit="return checkAnswer_1()">
   <p>What will be printed when the following code above is run?</p>
   <input type="text" id="userAnswer_1">
   <button type="submit">Submit Answer</button>
   <p id="result_1"></p>
   </form>

.. raw:: html

   <script>
   function checkAnswer_1() {
       var userAnswer = document.getElementById("userAnswer_1").value;
       var correctAnswer_1 = "Dias Buenos";
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