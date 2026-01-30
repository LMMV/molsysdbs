import os
import sys

sys.path.insert(0, os.path.abspath(".."))

project = "molsysdbs"
author = "molsysdbs contributors"

extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
]

templates_path = ["_templates"]
exclude_patterns = ["_build"]

html_theme = "alabaster"
