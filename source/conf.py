# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

master_doc = 'index'

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information
import revitron_sphinx_theme

project = 'Madeline'
copyright = '2022 - present, MatthewSoft'
author = 'Clemie McCartney'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ["revitron_sphinx_theme",]

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