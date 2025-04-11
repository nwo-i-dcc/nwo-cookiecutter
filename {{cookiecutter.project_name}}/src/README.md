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