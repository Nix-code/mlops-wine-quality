from setuptools import setup, find_packages
# setup.py lets you create packages 
# find packages automatically finds the packages inside src(__init__.py)

setup(

    name="src",
    version="0.0.1",
    description="It's a mlops wine q package",
    author="Nix",
    packages=find_packages(),
    license="MIT"
)

# run now 
# pip install -e .
# check by typing pip freeze
# python3 
# import src

# make tar file dist
# python setup.py sdist bdist_wheel
