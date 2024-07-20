# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

from pyipcmini.version import __version__

project = "pyIPCMini"
copyright = "2024, The pyIPCMini Developers"
author = "Benjamin Pasquiou"
release = __version__

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ["sphinx.ext.autodoc", "sphinx.ext.autosummary", "sphinx.ext.viewcode", "numpydoc", "nbsphinx", "nbsphinx_link"]

templates_path = ["_templates"]
exclude_patterns = ["**.ipynb_checkpoints"]

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
#
# source_suffix = ['.rst', '.md']
source_suffix = ".rst"

# The master toctree document.
master_doc = "index"

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

Source = "https://github.com/benjaminpasquiou/pyIPCMini"
Documentation = "https://pyIPCMini.readthedocs.io"

html_theme = "pydata_sphinx_theme"
html_theme_options = {
    "show_nav_level": 0,
    "show_toc_level": 2,
    "header_links_before_dropdown": 4,
    "external_links": [{"name": "GitHub", "url": Source}, {"name": "PyPI", "url": Documentation}],
    "icon_links": [
        {
            "name": "GitHub",
            "url": Source,
            "icon": "fa-brands fa-github-alt",
            "type": "fontawesome",
        },
        {
            "name": "PyPI",
            "url": Documentation,
            "icon": "fa-solid fa-download",
            "type": "fontawesome",
        },
    ],
    "primary_sidebar_end": ["indices.html", "sidebar-ethical-ads.html"],
    "back_to_top_button": True,
}
html_sidebars = {"**": ["sidebar-nav-bs.html", "sidebar-ethical-ads.html"]}
html_context = {"default_mode": "dark"}

nbsphinx_execute = "never"
nbsphinx_allow_errors = True

myst_enable_extensions = ["dollarmath"]
