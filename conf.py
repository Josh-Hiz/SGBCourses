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


extensions = [
    'jupyterlite_sphinx',
    'sphinx_exec_code',
    'plugins.add_css',
    'plugins.free_response',
    'sphinxcontrib.quizdown',
    'sphinx_pyscript',
]

html_sidebars = {
    "**": ["sbt-sidebar-nav.html"]
}
jupyterlite_contents = ["content/courses/cs515/cs515_challenges/"]
jupyterlite_bind_ipynb_suffix = False