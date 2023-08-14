__version__ = 'v0.0.3'

import pathlib
import os
import shutil
import time

import builder as userspace
import builder_modules.log as log

class File:
    """
    A custom file class for builder.py.
    """

    content = str
    name = str
    path = str

    def __init__(self, path: str):
        # Import current content file and pass to the builder

        # Opens the buildable file in read only
        self.content = open(f'{path}', "r").readlines()

        # Stores the files path
        self.path = path

        # Stores the filename
        self.name = path.rstrip(userspace.content_file_extention)

        # log.debug("File: ", self.name, " at location: ", self.path " has been created")

def run():
    """
    This is abstracted for future modification of the running process. 
    This will allow for a constantly running server to edit and see changes 
    live later.
    """
    find_and_build_files()

def find_and_build_files():
    """
    Loops over every file in the main directory for the input content directory.
    Create the output directory if the output directory does not exist and
    the input content directory was found. 
    Search for buildable files if the input content directory was found.
    """
    for child in pathlib.Path().iterdir():
        # We do not need to check for files if it is the content directory
        if (child.name != userspace.input_content_directory):
            continue

        # Make sure it is not a file named the same as the content directory
        if (os.path.isfile(child) == True):
            continue

        # Create the directory for output
        if os.path.isdir(userspace.output_directory) == False:
            os.mkdir(userspace.output_directory)

        search_buildable_files(child)

# WARNING: This is recursive! We need to put an upper limit on recursions!
def search_buildable_files(child):
    """
    Iterates over the current contents of a directory. 
    
    If it is a directory that does not yet exist in the output, create the
    output file.
    
    If it is a directory, then run this function to run through that directory.
    
    If it is a file that is the correct file extension and the output files 
    modify date is younger then the input, build a new file to output. If the 
    file is older, then ignore.
    
    If a file is the wrong extension, do the same actions but copy the file 
    instead of building.
    """
    for child in pathlib.Path(child).iterdir():
        # If the path is a directory, 
        # we need to search in that directory for more files to build
        if os.path.isdir(child) == True:
            # Create the directory for output
            if os.path.exists(get_output_file(child)) == False:
                os.mkdir(get_output_file(child))
            
            search_buildable_files(child)
            continue

        # If a file hasn't been edited after the previous build time, continue
        if os.path.getmtime(get_output_file(child)) >= os.path.getmtime(child):
            continue

        # If the file has a mentioned content file extention, build it
        if userspace.content_file_extention.__contains__(child.suffix):
            userspace.build( File(str(child)) )
        # elif (): # Else if the file is a mentioned compilation only file, compile it
        else: # This should be files such as images, JS documents, and others
            shutil.copyfile(child, get_output_file(child))
            pass

def get_output_file(path: pathlib.Path) -> str:
    """
    Takes a path to a file and replaces the first case of the input directory
    with the output directory to create the output files path.
    """
    return str(path).replace(userspace.input_content_directory, userspace.output_directory, 1)