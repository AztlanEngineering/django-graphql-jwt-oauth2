import os
import sys
sys.path.insert(0, os.path.abspath('../../'))
from django.conf import settings
settings.configure(
    SECRET_KEY="test", 
    OAUTH2_CONFIG={
        "GOOGLE":{
            "CLIENT_ID":None,
            "CLIENT_SECRET":None,
        }
    },
    OAUTH2_PROVIDER_CLASSES={

    }
)
# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'django-graphql-jwt-oauth2'
copyright = '2023, AztlanEngineering'
author = 'AztlanEngineering'
release = '1.0.1'


# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx_markdown_builder',
]


templates_path = ['_templates']
exclude_patterns = []



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

#html_theme = 'alabaster'
#html_static_path = ['_static']
