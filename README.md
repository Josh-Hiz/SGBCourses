# Sphinx-Greenberg-Courses

## Slide format:
All documents/textbook slides are written in RST and NOT markdown, therefore if you want to add new documents in slides please update the `toctree` in the appropriate index

## Spinning up a local server:
Run the server script `run_livereload.py` to spin up the server

## Before running:
Please run `sphinx-build -M html ./ _build/ -W -a -j auto -n --keep-going` so Sphinx can build the HTML and render RST

## Current Goals

- Get Free response on quizdown to work, however my free response plugin is pretty good as is, just have no idea how the parser works in quizdown, need to figure that out as I also need to understand how in the world the svelete works
- Figure out challenges, looks like pyscript wont work completely as I need to have some sort of text editor thats good enough to replace jupyter, ill try making my own with pyodide and code mirror, the problem I am facing is that can code mirror open and edit live files? Research is needed, not only that but I need to make sure its compatible with an rst directive, lets say it has a 'file' argument that will open a file in a specific directory for you to edit, then how is the test script run?

TODO: Continue revising week 1 and week 7, continue development on pyodide-ace editor, free response in quizzdown?
**Slide 21 needs the answers updated for challenges, Challenge 10, Challenge 11, are work in progress**