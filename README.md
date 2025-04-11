# NWO cookiecutter template

This is a cookie cutter template for research projects at NWO.
Nothing here is obligatory. It is a possible way to organize all
your project files. Feel free to adapt the structure to your 
needs, but keep in mind that having standard names for things
helps yourself and others to find things. 

The template assumes a UNIX operating system like Mac OS or Linux.

# Directory structure

    ├── README.md          <- The top-level README.md file for information about the project.
    ├── data
    │   ├── external       <- Data from third party sources.
    │   ├── intermediate   <- Intermediate data that has been transformed.
    │   ├── processed      <- The final, canonical data set.
    │   └── raw            <- The original, immutable data dump.
    │
    ├── references         <- Related papers, manuals, and all other explanatory materials.
    │   ├── manuals        <- Directory for manuals.
    │   ├── papers         <- Directory for related papers.
    │   └── other          <- Other explanatory materials.
    │
    ├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
    │   ├── presentations  <- Presentations given about the project.
    │   ├── meetings       <- Updates presented in group meetings, etc.
    │   └── figures        <- Generated graphics and figures to be used in reporting.
    │
    ├── env.sh             <- A bash file to contain all the environment variables
    │                         and software sources to run the project. 
    │
    ├── src                <- Source code for use in this project (* Git).
    │   │
    │   ├── docs           <- Documentation for the source code. 
    │   │
    │   ├── notebooks      <- Jupyter notebooks.
    │   │
    │   ├── <repo_name>    <- Python module for project.
    │   │   │                 
    │   │   ├── __init__.py   <- Make this directory a python module.
    │   │   ├── scripts       <- Directory to add python scripts. 
    │   │   └── functions.py  <- Add your python functions here.
    │   │
    │   └── pyproject.toml <- Python project definition file used to build a python package. 
    │
    └── paper              <- Directory to write your paper (* Git/Overleaf).

# Create your project directory

You can create your own project directory following this directory structure
using the cookiecutter program. Open a terminal and go to the directory
where you want to create your new project (for example `~/Projects/`).
Then run `cookiecutter` with the URL of the template:
```
cookiecutter https://github.com/nwo-i-dcc/nwo-cookiecutter
```
Cookiecutter will ask a couple of questions about your project.
Give a name to your project. This is going to be the name of the project
directory, so make sure it is easy enough (one word).
```
  [1/5] project_name (What is the name of your project?): astro
```
A Python package directory is automatically created. You can give this package
a unique name. Do not give it the same or similar name as existing Python packages.
```
  [2/5] repo_name (Give a name to the Python package of your project (one word)): projastro
```
If you add your name and email address to the project, it will appear in
the Python package and the README.
```
  [3/5] author_name (Your name (or your organization/company/team)): Jane Doe (NWO)
  [4/5] email (Your email address): jdoe@nwo-i.nl
```
Finally, you provide a short description of the project. This will also
be added to the Python package and the top-level README file.
```
  [5/5] description (A short description of the project): Astro project
```

# Data

Now that the directory structure is created, we can discuss the contents.
In the data directory you can store your data. These data can be in various
stages of analysis. There can be raw data from an instrument or data
from an external source, from which you derive intermediate data and
end results.

It is usually a good idea to separate the original data (raw or external)
from the processed data. You usually do not want to alter the raw or external
files in any way, so saving them in separate directories avoids accidentally
changing these files.

## Subdirectories

The data directory contains the following subdirectories:

- external: To store external data,
- raw: To store raw data from the instrument,
- intermediate: To store intermediate data products while processing,
- processed: To store the end results of the processing.

## Link to large file storage

If your datasets are large, it is best to store them on a disk with high
capacity. You can still include them in this directory structure by creating
a symbolic link. It is best to replace the current directory. For example,
the `external` directory needs to be removed before we can make a link to
an existing directory elsewhere. Be careful with the `rm` command!
```
# First check whether the external directory is empty:

user@linux:~/nwo-cookiecutter/data> ls external/

# If the directory does not contain anything that you want to keep, then remove it:

user@linux:~/nwo-cookiecutter/data> rm -rf external/
```

If we have the external data stored in `/path/to/storage/external`, then
we can create the new link with the command:
```
user@linux:~/nwo-cookiecutter/data> ln -s /path/to/storage/external external
```
The data will still be available at `data/external`, but the files will be
physically stored in `/path/to/storage/external`.

# The env.sh file

Since you probably use a number of external software packages in this
project, it may be a good idea to use `env.sh` as a source file to
set all the software packages and environment variables that you need.

In the file, you can source software packages to make them available
in your environment. In addition, you can set project specific variables.
For example, you can set a variable containing the absolute path to
your project directory. You can then read this variable in your Python
programs and use it to find your files relative to this path. This 
way, you can move your directory to another system and all you need 
to change is the path contained in the environment variable.

For an example, see `PROJECT_DATA_DIR` set in `env.sh`. In 
`src/<repo_name>/functions.py` you can find the `get_data_dir` function
which reads and checks the path from `PROJECT_DATA_DIR`. This
way, you can use the path throughout your package.

Please make sure that your `env.sh` file does not end up in
a git repository, or at least make sure that the environment
does not contain sensitive information.

# References

You can use this directory to save any explanatory materials related
to your project. These can be papers, manuals, and other documents
that are useful to have around.

# Reports

The reports directory can be used to store all kinds of (intermediate)
reports about the project. From figures that you presented at group 
meetings to presentations given at conferences. 

Tip for the meeting directory: If you create a subdirectory for each
meeting with the date in `YYMMDD` format, they will be nicely ordered
by time in your directory listing.

# Source directory (src)

In this directory, you can put your Python source code.
It is usually very helpful to create functions or classes
for operations that you use often.

It is very useful to keep this directory under git version
control. See below how to initialize Git for this directory.

The directory is set up in a way such that you can easily
create a Python package. It contains the ``docs`` and
``notebooks`` directories to document the code and provide
examples as jupyter notebooks.

## Docs

You can use this directory to create source code documentation.
A way to do that is to use the python ``sphinx`` package.

If you are interested, then look at the [Sphinx Quickstart
guide](https://www.sphinx-doc.org/en/master/usage/quickstart.html).

## Notebooks

In this directory, you can store jupyter notebooks that you use
to explore the data and visualize it.

## Pyproject.toml

The `pyproject.toml` file describes the properties of your python
package, what packages it depends on and how it is installed. You
can find more information about this file here:
[Write your own pyproject.toml](https://packaging.python.org/en/latest/guides/writing-pyproject-toml/).

# Initialize Git for this directory

To start using version control for this directory, you can give the
commands below. Make sure that you are in the ``src/`` directory
before you give these commands.
```
git init
git add .
git commit -m "Initialise git for the project"
```
Since this is an existing directory, you need to create an empty
project on github.com. Make sure that you
**uncheck** the option to create a README file when you create a new
project. Once your Github project is created, you can add
the URL to your local git repository:
```
git remote add origin https://github.com/your_project.git
git push -u origin main
```
From now on, the source directory is under version control.

# Paper

In the paper directory, you can write your (LaTeX) paper. Many people
use Overleaf these days and it is possible to use git version control
to sync your paper files with Overleaf.

Please see the [Git integration](https://www.overleaf.com/learn/how-to/Git_integration)
manual of Overleaf to get your Overleaf project into this directory.
