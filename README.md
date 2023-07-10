# Sphinx-Greenberg-Courses

## Slide format:
All documents/textbook slides are written in RST and NOT markdown, therefore if you want to add new documents in slides please update the `toctree` in the appropriate index

## Spinning up a local server:
Run the server script `run_livereload.py` to spin up the server

## Please run the following lines in your termnial before spinning up the server:
Install node packages (its just one package):
```
npm install
```
Install python packages:
```
pip install -r requirements.txt
```
Then run initial setup and debugging:
```
sphinx-build -M html ./ _build/ -W -a -j auto -n --keep-going
```
Then run the following to make production build
```
make clean
make html
```

## Current Problems:

- **Week 4 Testing Mean and Testing Median need to be worked on, code runners cannot handle infinite while loops and key interrupts as pyodide makes it near impossible to support**

## Custom Directives and how to use them

Sphinx and RestructredText in general rely on directives to do a lot of the heavy lifting. Here are some of the most common directives that you can use and how to use them:

### Challenges
The challenge directive when called will render a Python text editor for you to type in code and even run it using Pyodide. The text editor is from Ace. An additional feature is that it can run test scripts, here are a few examples:

Standard usage with test script and having some initial code to put in the editor:
```
.. challenge::
    :tester: /test/file/path/here.py

    # Here is some initial code to put in your text editor

    for i in range(10):
        print(i)
    
    s = input("Random input!")
    print(s)
```

When you dont want a test script but still want to run code:
```
.. challenge::

    # Here is some initial code to put in your text editor

    for i in range(10):
        print(i)
    
    s = input("Random input!")
    print(s)
```

### Code Runners
Code runners, sometimes incorrectly referred to as REPL's is more or less identical to the challenge directive except its purely meant for code editing and running initial code you place in the editor. Here are is an example:

```
.. runner::

    # Here is some initial code to put in your text editor

    def foo(msg):
        print(msg + 'bar')
```

### Free Response Questions
This is a very recent directive I made out of frustration on relying on Quizdown and a very amerture and disfunctional directive I once had to handle free response questions so I created a new directive that would allow for a more flexible and robust way of handling free response questions. It support the following:

- Markdown syntax
- Explanations
- Allow you to use regular expressions as answers (this is a big one)
- Default explanations (It will tell the user the answer)
- Explanations only appear if a user gets a question wrong on first try

Here are a few examples:

Here is a standard quiz that does not use regex for answers and has explanation:

```
.. free-r::
    :answer: 1

    # Question

    What does the following Python expression evaluate to? (For maximum learning, try to work it out yourself!)

    ```41 // 2 ** 3 - 4 * 2 + ( 9 % 5 )```

    >>>
    41 // 2 ** 3 - 4 * 2 + ( 9 % 5 ) evaluates to<br>
    41 // 2 ** 3 - 4 * 2 + 4 evaluates to<br>
    41 // 8 - 4 * 2 + 4 evaluates to<br>
    5 - 4 * 2 + 4 evaluates to<br>
    5 - 8 + 4 evaluates to<br>
    -3 + 4 evaluates to<br>
    1
```

**Everything below the >>> will be concidered part of the custom explanation**

Example that uses regex and explanation, **you need to specify "regex: true" so the directive knows to use regex**:


```
.. free-r::
    :answer: '"It\\'s a backslash," he said, "you write it like \\'\\\\\\'\."'|"\\"It\\?'s a backslash,\\" he said, \\"you write it like \\?'\\\\\\?'\.\\""
    :regex: true

    # Question 3

    How would you write the following as a string in Python?

    ```"It's a backslash," he said, "you write it like '\'."```

    Just write the string literal, as in ```"this\tis not  the answer"```.

    >>>
    ```'"It\'s a backslash," he said, "you write it like \'\\\'."'```<br>
    or<br>
    ```"\"It's a backslash,\" he said, \"you write it like '\\'.\""```
```
What if you want your answer to be multiple lines? You can do that too!

```
.. free-r:: 
    :answer:
        func_a
        func_d
        func_c
        func_b
        func_e
        func_b
    
    # Question 1

    What order will the functions be called in? Write each function name once per line. If a function is called more than once, list it once for each time its called.
    
    >>>
    The functions will be called in this order:<br>
    ```func_a<br>
    func_d<br>
    func_c<br>
    func_b<br>
    func_e<br>
    func_b```
```

### Quizdown
Quizdown is a custom directive that I did not make and simply use it for single choice and free response, its pretty good, here are some examples of usage:

Take note that 1. [ ] indicates single choice and - [ ] indicates multiple choice, where things marked with 'x' are the correct answers

Here is one where you want to put images AND have the question answers be multi line and have code blocks
```
.. quizdown::
        
    ### The following 3x4 image is given as a 2D list ```rgb_rows```.

    ![](https://i.ibb.co/dMJ6J8R/rgbrows.png)

    <br>

    What code will print the RGB information in the following image:

    ![](https://i.ibb.co/djbYVY1/bluerow.png)

    1. [ ] ```
        for column in range(4):
            print(rgb_rows[1][column])
        ```
    2. [ ] ```
        for column in range(4):
            print(rgb_rows[3][column])
        ```
    3. [x] ```
        for column in range(4):
            print(rgb_rows[2][column])
        ```
    4. [ ] ```
        for column in range(4):
            print(rgb_rows[0][column])
        ```
```

Here is a more standard quiz without explanations
```
.. quizdown::

    ### What is this color?

    R = 100, G = 100, B = 100

    Hint: Test it out with the color picker tool if you are unsure.

    1. [ ] white
    2. [ ] brown
    3. [ ] black
    4. [ ] gray 


    ### What is this color?

    R = 255, G = 255, B = 0

    Hint: Test it out with the color picker tool if you are unsure.

    1. [x] yellow
    2. [ ] red
    3. [ ] purple
    4. [ ] green 
```

More directives can be added over time, otherwise, that is all!