"""
Configuration file for pytest.
This file helps pytest find and import our package correctly.
"""

import os
import sys

# Get the absolute path to the project root
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

# Add the project root to the Python path
sys.path.insert(0, project_root)

# Add the src directory to the Python path
sys.path.insert(0, os.path.join(project_root, "src")) 