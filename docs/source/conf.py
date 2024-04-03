# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'REST APIs with Flask and Python in 2024'
copyright = '2024, Udemy & Pougilhac'
author = 'Udemy & Pougilhac'
release = '0.0'

# Sphinx must go “up” one directory level to find the Python package.
import os
import sys
sys.path.insert(0, os.path.abspath('../..'))

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinx.ext.autodoc', # Core library for html generation from docstrings
    'sphinx.ext.autosummary', #  generates function/method/attribute summary lists
    'sphinx.ext.autosectionlabel', # This extension allows you to refer sections its title.
    'sphinx.ext.coverage', # Check Python modules and C API for coverage
    'sphinx.ext.viewcode', # Add links to highlighted source code
    'sphinx.ext.napoleon', # enables Sphinx to parse both NumPy and Google style docstrings
    'sphinx_rtd_theme',
    'myst_parser', # pour gérer Markdown 
    'sphinxemoji.sphinxemoji', # pour les emojis
]

templates_path = ['_templates']
exclude_patterns = []

napoleon_google_docstring = True

language = 'fr'

source_suffix = {
    '.rst': 'restructuredtext',
    '.txt': 'markdown', # to use Markdown files with extensions other than .md
    '.md': 'markdown',
}

sphinxemoji_style = 'twemoji'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']

# THEME LOGO
html_logo = 'flask.svg'

html_theme_options = {
    # ----------------- RTD THEME
    'logo_only': False,
    'display_version': True,
    'prev_next_buttons_location': 'both',
    'collapse_navigation': False,
    'titles_only': False,
}
