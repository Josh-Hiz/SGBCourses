What's On Your Stack?
=====================

Consider the following program (Please run it to see the output):

.. py-config::

    splashscreen:
        autoclose: true

.. py-repl::
    :output: replOutput

    def func_a():
        func_d()
        func_b()
        return

    def func_b():
        return

    def func_c():
        func_b()
        func_e()
        return

    def func_d():
        func_c()
        return

    def func_e():
        print("HERE!")
        return

    func_a()

.. raw:: html

    <div id="replOutput"></div>

.. py-terminal::

Please answer the following two questions about the program. Note that the quiz checker wants *exact* answers! (Func1,Func2,Func3...etc, the last one should have no comma at the end).

.. add-css:: 


.. raw:: html

   <form onsubmit="return checkAnswer_1()">
   <p>What order will the functions be called in? Write each function name once per line. If a function is called more than once, list it once for each time its called.</p>
   <input type="text" id="userAnswer_1">
   <button type="submit">Submit Answer</button>
   <p id="result_1"></p>
   </form>

.. raw:: html

   <script>
   function checkAnswer_1() {
       var userAnswer = document.getElementById("userAnswer_1").value;
       var correctAnswer_1 = "func_a,func_d,func_c,func_b,func_e,func_b";
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
   <p>When <code>func_e</code> is called, it will print out <code>HERE!</code>. What is the call stack right before the <code>print</code> happens? Please list it in top down order: the current function, its caller, then its caller, and so on. Put one function name per line.</p>
   <input type="text" id="userAnswer_2">
   <button type="submit">Submit Answer</button>
   <p id="result_2"></p>
   </form>

.. raw:: html

   <script>
   function checkAnswer_2() {
       var userAnswer_2 = document.getElementById("userAnswer_2").value;
       var correctAnswer_2 = "func_e,func_c,func_d,func_a";
       if (userAnswer_2.toLowerCase() === correctAnswer_2.toLowerCase()) {
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

