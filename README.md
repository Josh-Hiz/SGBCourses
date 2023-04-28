# Sphinx-Greenberg-Courses

## Slide format:
All documents/textbook slides are written in RST and NOT markdown, therefore if you want to add new documents in slides please update the `toctree` in the appropriate index

## Spinning up a local server:
Run the server script `run_livereload.py` to spin up the server

## Before running:
Please run `sphinx-build -M html ./ _build/ -W -a -j auto -n --keep-going` so Sphinx can build the HTML and render RST

### Side note:
For some reason on google chrome you may need to clear your cache of the past hour as when new files are added there could be *times* where Sphinx caches the files and then google caches them leading to sometimes seeing files that shouldnt exist anymore. This is a very rare instance however, just a side note.

## How courses and chapters are organized (so far):
Every chapter will have a `slides` folder in which will contain the following:
- `books` -> folder that will hold all the folders containing the files for challenges
  - The books folder will contain `challenge` folders organized by number, and contain 1 jupyter notebook to run the test script and one python file so students can code in it
- X_slide-title -> X is the slide number and it has the title, these are the basic text book slides and easy to make
- Every course thats added should follow the format of having a `slides` folder that contains RST (or markdown) of the typed up text book slide, if you want to make a slide with a challenge or quiz, the good this is RST directives will cover that assuming that the site is finished

# Current update notes, ideas and issues:

### input() in python ide's
Running python that requires the ``input()`` command seems to be causing alot of issues for a reason I don't know, must fix this asap as this halts progress on many other slides, the current slides that have input() issues is:
- Slide 25
- Slide 26
- Slide 27

### Quiz answers
- Must update slide 21 quiz answers as for some reason edstem literally wont recognize the answers

### Current goals:
- Finish chapter 1 in whatever state it may be in
- Perfect all functions and types of slides used in chapter 1 so it can be easily reproducible and allow copy and pasting into next chapters, in which effectivley the site will be done
- The stuff that needs testing include:
  - JupyterLite challenges and seeing how much freedom we are willing to give users in viewing test scripts (we can just add instructions on how to use)
  - Quizzes, instead of quizzdown i am just writing the html and javascript myself, i need to figure out a more efficient way of doing it rather than copy and pasting, will make rst directives after finishing week 1
