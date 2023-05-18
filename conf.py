# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information
import sys
sys.path.append('./')

project = 'Course'
copyright = '2023, Joshua Hizgiaev & Michael Greenberg'
author = 'Joshua Hizgiaev & Michael Greenberg'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "sphinx_book_theme"
html_static_path = ['_static']

html_theme_options = {
    "home_page_in_toc": True,
}

# global options passed to the quizdown library
quizdown_config = {
    'quizdown_js': 'https://cdn.jsdelivr.net/gh/bonartm/quizdown-js@latest/public/build/quizdown.js', # quizdown javascript
    'shuffle_answers': False,		# shuffle answers for each question
    'shuffle_questions': False,     # shuffle questsions for each quiz
    'primary_color': '#000000',     # primary CSS color
    'secondary_color': '#F2F3F5',   # secondary CSS color
    'text_color': 'black',          # text color of interactive elements
    'locale': 'en'                  # language of text in user interface
}

extensions = [
    'jupyterlite_sphinx',
    'sphinx_exec_code',
    'plugins.add_css',
    'plugins.free_response',
    'sphinxcontrib.quizdown',
    'sphinx_pyscript',
]
# html_css_files = ['//cdnjs.cloudflare.com/ajax/libs/highlight.js/11.7.0/styles/default.min.css']
# html_js_files = ['//cdnjs.cloudflare.com/ajax/libs/highlight.js/11.7.0/highlight.min.js']

html_sidebars = {
    "**": ["sbt-sidebar-nav.html"]
}
jupyterlite_contents = ["./content/courses/cs515/cs515_challenges/"]

jupyterlite_bind_ipynb_suffix = False