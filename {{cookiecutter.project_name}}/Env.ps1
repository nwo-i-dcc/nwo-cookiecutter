# Env.ps1
# Set environment variables for your research project in Windows PowerShell

# Project directory (set the path to the top-level directory of this project)
$env:PROJECT_DIR = "C:\Users\user\Projects\this_project"
$env:PROJECT_DATA_DIR = "$env:PROJECT_DIR\data"

# Add the project python package to the PYTHONPATH
$env:PYTHONPATH = "$env:PROJECT_DIR\src;$env:PYTHONPATH"

