# Configuration file for the Sphinx documentation builder.

# -- Project information -----------------------------------------------------
project = 'Task List App'
copyright = '2025, Alexis'
author = 'Alexis'
release = '1.0'

# -- General configuration ---------------------------------------------------
extensions = [
    'sphinx.ext.autodoc',        # Auto-generates documentation from docstrings
    'sphinx.ext.napoleon',       # Supports Google/NumPy style docstrings
    'sphinx.ext.viewcode',       # Adds links to source code
]

# Add paths to your main app directory
import os
import sys
sys.path.insert(0, os.path.abspath('../../'))  # This assumes conf.py is in docs/source/

templates_path = ['_templates']
exclude_patterns = []

# -- Options for HTML output -------------------------------------------------
html_theme = 'alabaster'
html_static_path = ['_static']
