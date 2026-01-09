# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = "repo2wasm"
copyright = "2025, Raniere Gaia Costa da Silva"
author = "Raniere Gaia Costa da Silva"

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "myst_parser",
    "sphinx_rtd_theme",
    "sphinxcontrib.mermaid",
    "sphinxcontrib.programoutput",
]

templates_path = ["_templates"]
exclude_patterns = []

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "sphinx_rtd_theme"
html_static_path = ["_static"]
html_logo = "_static/img/repo2wasm-square.svg"
html_favicon = "_static/img/favicon.png"
html_copy_source = False
html_context = {
    "display_github": True,
    "github_user": "repo2wasm",
    "github_repo": "repo2wasm-py",
    "github_version": "main",
    "conf_py_path": "/docs/source/",
}

# -- Options for Read the Docs theme ------------------------------------------
# https://sphinx-rtd-theme.readthedocs.io/en/stable/configuring.html
html_theme_options = {
    "display_version": True,
    "prev_next_buttons_location": "both",
    "style_external_links": True,
}
