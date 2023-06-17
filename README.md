# Sphinx-Greenberg-Courses

## Slide format:
All documents/textbook slides are written in RST and NOT markdown, therefore if you want to add new documents in slides please update the `toctree` in the appropriate index

## Spinning up a local server:
Run the server script `run_livereload.py` to spin up the server

## Before running:
Please run `sphinx-build -M html ./ _build/ -W -a -j auto -n --keep-going` so Sphinx can build the HTML and render RST
Then run the following: `make clean` followed by `make html` to make production build

## Current Goals

- I need to find an alternative solution for markdown quizzes, the literally only single issue is free response, how the hell does quizdown work??? If the issue continues I will have to prioritize it.

**Slide 21 needs the answers updated. Slide 81 week 2 needs to be fixed**