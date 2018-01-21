import os
import sys
import inspect

# Here we define helper functions


"""
TODO: write docstring
"""
def check_directory(directory=None):

    if not directory:
        print("A valid directory must be provided to '{0}'"
              .format(inspect.stack()[0][3])) 
        sys.exit(0)

    cwd = os.getcwd()
    if not os.path.isdir(cwd + "/" + directory):
        print("Directory '{0}' does not exist. Creating one..".format(directory))
        try:
            os.mkdir(cwd + "/" + directory)
        except:
            print("Something went wrong trying to create the directory..")
            sys.exit(0)
        
        print("Created '{0}' directory!".format(directory))