# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Course'
copyright = '2023, Joshua Hizgiaev & Michael Greenburg'
author = 'Joshua Hizgiaev & Michael Greenburg'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = []

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "sphinx_book_theme"
html_static_path = ['_static']

html_theme_options = {
    "home_page_in_toc": True,
}

extensions = [
    'jupyterlite_sphinx',
    'sphinxcontrib.quizdown', 
]

jupyterlite_bind_ipynb_suffix = False