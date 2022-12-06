# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

import revitron_sphinx_theme
import datetime
master_doc = 'index'

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information
project = 'Madeline'
copyright = '{}, MatthewSoft'.format(
    datetime.datetime.now().year
)
author = 'Clemie McCartney'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration
# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.coverage',
    'sphinx.ext.napoleon',
    'sphinxext.opengraph',
]

napoleon_google_docstring = True
napoleon_include_init_with_doc = True
napoleon_include_private_with_doc = False
napoleon_include_special_with_doc = True
napoleon_use_admonition_for_examples = False
napoleon_use_admonition_for_notes = True
napoleon_use_admonition_for_references = True
napoleon_use_ivar = False
napoleon_use_param = True
napoleon_use_rtype = True

templates_path = ['_templates']
exclude_patterns = []

# Open Graph extension config. https://pypi.org/project/sphinxext-opengraph/
ogp_site_url = "https://www.madeline.my.id/"

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "revitron_sphinx_theme"
html_logo = '_static/madeline.png'
html_title = 'Madeline'
html_favicon = '_static/madeline.png'
html_static_path = ['_static']
html_theme_options = {
    'navigation_depth': 5,
    'github_url': 'https://github.com/madeline-bot',
    'color_scheme': 'dark'
}
html_context = {
    'landing_page': {
        'menu': [{
            'title': 'Home',
            'url': 'index.html'
        }, {
            'title': '♡ Sponsor',
            'url': 'https://github.com/sponsors/madeline-bot'
        }, {
            'title': 'Vote us on top.gg',
            'url': 'https://top.gg/bot/859991918800011295'
        }]
    }
}
html_sidebars = {}
html_css_files = ['custom.css']