# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information
import sys
sys.path.append('./')

project = 'CS 515-A'
copyright = '2023 (c) Michael Greenberg'
author = 'Michael Greenberg with Joe Gibbs Politz, Joshua Hizgiaev, and others from UCSD'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store', 'venv']

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "sphinx_book_theme"
html_static_path = ['_static']

html_css_files = [
    'css/code_block.css',
]

html_theme_options = {
    "home_page_in_toc": True,
    "repository_provider": "github",
    "repository_url": "https://github.com/Josh-Hiz/SGBCourses",
    "use_source_button": True,
    "use_edit_page_button": True,
    "use_repository_button": True,
    "use_issues_button": True,
    "navbar_end": ["navbar-icon-links"],
    "navigation_with_keys": False,
}


extensions = [
    'sphinxcontrib.quizdown',
    'plugins.challenge',
    'plugins.runner',
    'plugins.free_r'
]

quizdown_config = {
    'quizdown_js': 'https://cdn.jsdelivr.net/gh/bonartm/quizdown-js@latest/public/build/quizdown.js', # quizdown javascript
    'start_on_load': True,			# detect and convert all divs with class quizdown
    'shuffle_answers': False,		# shuffle answers for each question
    'shuffle_questions': False,     # shuffle questsions for each quiz
    'primary_color': '#000000',     # primary CSS color
    'secondary_color': '#FFFFFF',   # secondary CSS color
    'text_color': 'black',          # text color of interactive elements
    'locale': 'en'                  # language of text in user interface
}

html_favicon = 'favicon.ico'

html_sidebars = {
    "**": ["sbt-sidebar-nav.html"] 
}

