# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information
""" Configuration file for the Sphinx documentation builder.

Changelog
---------
.. versionadded::    23.09
    |br| first version of config (01)

|   **Open Source Notification:** This file is part of open source program **AVANTAR**
|   **Copyright © 2023  Carlo Oliveira** <carlo@nce.ufrj.br>,
|   **SPDX-License-Identifier:** `GNU General Public License v3.0 or later <https://is.gd/3Udt>`_.
|   `Labase <http://labase.selfip.org/>`_ - `NCE <https://portal.nce.ufrj.br>`_ - `UFRJ <https://ufrj.br/>`_.

.. codeauthor:: Carlo Oliveira <carlo@nce.ufrj.br>

"""
import sys
import pathlib
path = pathlib.Path(__file__).parent.parent.parent / "src"
sys.path.insert(0, str(path))

from avantar import __version__

project = 'A V A N T A R 🐧'
copyright = '2023, Carlo E. T. Oliveira'
author = 'Carlo E. T. Oliveira'
version = __version__

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ['sphinx.ext.autodoc', 'sphinx.ext.todo', 'sphinx.ext.viewcode', 'sphinx_rtd_theme',
              'sphinx_toolbox.more_autodoc.autonamedtuple']

templates_path = ['_templates']
exclude_patterns = []

language = 'PT-br'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']
