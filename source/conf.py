# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information
import revitron_sphinx_theme
import myst_parser

project = 'Madeline'
copyright = '2022 - present, MatthewSoft'
author = 'Clemie McCartney'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ["myst_parser", "revitron_sphinx_theme",]

templates_path = ['_templates']
exclude_patterns = []
source_suffix = {
    '.rst': 'restructuredtext',
    '.txt': 'markdown',
    '.md': 'markdown',
}


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "revitron_sphinx_theme"
html_static_path = ['_static']
html_theme_options = {
    'color_scheme': 'dark'
}
html_context = {
    'landing_page': {
        'menu': [
            {'title': 'Get Started', 'url': 'installing.html'},
            {'title': 'GitHub', 'url': 'https://github.com/user/repo'}
        ]
    }
}
