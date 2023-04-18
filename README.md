# Sphinx-Greenburg-Courses

## Slide format:
All documents/textbook slides are written in RST and NOT markdown, therefore if you want to add new documents in slides please update the `toctree` in the appropriate index

## Spinning up a local server:
Run the server script `run_livereload.py` to spin up the server

## Before running:
Please run `sphinx-build -M html ./ _build/ -W -a -j auto -n --keep-going` so Sphinx can build the HTML and render RST

### Side note:
For some reason on google chrome you may need to clear your cache of the past hour as when new files are added there could be *times* where Sphinx caches the files and then google caches them leading to sometimes seeing files that shouldnt exist anymore. This is a very rare instance however, just a side note.