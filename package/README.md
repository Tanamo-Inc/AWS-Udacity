# Making a Package


A package is a collection of Python modules.

An __init__.py file is  needed in a Python package.

Pip is a Python package manager that helps with installing and uninstalling Python packages. 

 When you execute a command like ***pip install numpy***, pip will download the package from a Python package repository called PyPi.

 ---
 >A Python package does not need to use object-oriented programming.


 # Python Environments

 A virtual environment is a silo-ed Python installation apart from your main Python installation. That way you can install packages and delete the virtual environment without affecting your main Python installation.

* conda and venv are two way different Python environment managers. You can create virtual environments with either one.

# Conda

Conda does two things: manages packages and manages environments.

As a package manager, conda makes it easy to install Python packages especially for data science. For instance, typing conda install numpy will install the numpy package.

As an environment manager, conda allows you to create silo-ed Python installations. With an environment manager, you can install packages on your computer without affecting your main Python installation.

The command line code looks something like this:
=================================================

conda create --name environmentname

source activate environmentname

conda install numpy



# Pip and Venv

There are other environmental managers and package managers besides conda. For example, venv is an environment manager that comes pre-installed with Python 3. 

> Pip is a package manager.

Pip can only manage Python packages whereas conda is a language agnostic package manager.

 In fact, conda was invented because pip could not handle data science packages that depended on libraries outside of Python. 
 
 If you look at the history of conda, you'll find that the software engineers behind conda needed a way to manage data science packages (NumPy, Matplotlib, etc.) that relied on libraries outside of Python.

> Conda manages environments AND packages.

> Pip only manages packages.

To use venv and pip, the commands look something like this:

python3 -m venv environmentname

source environmentname/bin/activate

pip install numpy




Which to Choose
=============

Whether you choose to create environments with venv or conda will depend on your use case. Conda is very helpful for data science projects, but conda can make generic Python software development a bit more confusing; that's the case for this project.

If you create a conda environment, activate the environment, and then pip install the distributions package, you'll find that the system installs your package globally rather than in your local conda environment. However, if you create the conda environment and install pip simultaneously, you'll find that pip behaves as expected installing packages into your local environment:


Once you've activated a virtual environment, you can then use terminal commands to go into the directory where your Python library is stored. And then you can run pip install .



>Use source env_name/bin/activate  to make the virtual environment


Run the pip install on the package folder to install it into the virtual Environment.


> pip install .