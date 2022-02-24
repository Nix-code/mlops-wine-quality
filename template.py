import os

# directory requirements for creating files
# os.path.join helps to manage directory without error 
# irrespective of the os
dirs = [
    os.path.join('data','raw'),
    os.path.join('data','processed'),
    "notebooks",
    "saved_models",
    "src"
    # our dataset will go in src
]
# exist ok checks if folder already created or not
# # if already created , wont throw error
for dir_ in dirs:
    os.makedirs(dir_ ,exist_ok=True)
    with open(os.path.join(dir_,'.gitkeep'),"w") as f:
        pass


files = [
    'dvc.yaml',
    'parameters.yaml',
    '.gitignore',
    os.path.join("src","__init__.py")
    
]

# The gist is that __init__.py is used to indicate that a directory is a python package
# From a file system perspective, packages are directories and modules are files."). If we want a folder to be considered a python package, we need to include a __init__.py file.

for file_ in files:
    with open(file_, "w") as f:
        pass