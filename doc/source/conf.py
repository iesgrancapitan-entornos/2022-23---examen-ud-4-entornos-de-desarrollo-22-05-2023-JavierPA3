# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information
import os
import sys

sys.path.insert(0, os.path.abspath('../../'))
version = '1.0'
project = 'Examen Entornos'
copyright = '2023, Javier Postigo Arévalo'
author = 'Javier Postigo Arévalo'
release = 'GNU'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ['sphinx.ext.autodoc',
'sphinx.ext.intersphinx',
'sphinx.ext.todo',
'sphinx.ext.mathjax',
'sphinx.ext.napoleon',
'sphinx.ext.autosummary',
'sphinx.ext.viewcode']


templates_path = ['_templates']
exclude_patterns = []



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "sphinx_rtd_theme"
html_static_path = ['_static']
