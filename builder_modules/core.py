__version__ = '0.0.3'

import pathlib
import os
import shutil
import time

import builder as userspace
import builder_modules.core_classes as classes
import builder_modules.log as log

_reset = "\033[0m"
_green = "\033[92m"
_addinfo = "\033[37m" # wrong clor, should be bright black.

def run(*, ip="10.0.0.37:8080", lan=False):
    """
    This is abstracted for future modification of the running process.
    This will allow for a constantly running server to edit and see changes
    live later.
    """
        # SH = 🚀, weird windows bug
    print(f"\n{_reset}  SH \033[102m\033[90m builder.py {_reset} {_addinfo}v{_green}{__version__}\n")
    print(f"{_reset}  Local:   http://localhost:8080")

    if lan == True: 
        print(f"{_reset}  Network: http://{ip}\n")
    else:
        print(f"{_reset}  Network: {_addinfo}use lan=True to expose{_reset}\n")

    find_and_build_files()

def build_release():
    pass

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

        search_buildable_files(child, 0)

# WARNING: This is recursive! We need to put an upper limit on recursions!
def search_buildable_files(child, recursion):
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
    recursion += 1

    if recursion >= userspace.recursion_upper_bound:
        log.fatal("Recursion limit exeeded: build failed! core.py:search_buildable_files")
        exit()

    for child in pathlib.Path(child).iterdir():
        # If the path is a directory, 
        # we need to search in that directory for more files to build
        if os.path.isdir(child) == True:
            # Create the directory for output
            if os.path.exists(get_output_variant(child)) == False:
                os.mkdir(get_output_variant(child))
            
            search_buildable_files(child, recursion)
            continue

        # Need to add an option to rebuild all files on release build
        # If a file hasn't been edited after the previous build time, continue
        # if os.path.getmtime(get_output_file(child)) >= os.path.getmtime(child):
        #     continue
        
        code = -1

        # If the file has a mentioned content file extention, build it
        if userspace.content_file_extention.__contains__(child.suffix):
            code = userspace.build( classes.File(str(child)) )
        # elif (): # Else if the file is a mentioned compilation only file, compile it
        else: # This should be files such as images, JS documents, and others
            code = 1 # File copied
            shutil.copyfile(child, get_output_variant(child))

        match code:
            case 0: log.built(f"{child}")
            case 1: log.copied(f"{child}")
            case _: log.error(f"(unknown) for {child}! If this occurs, one of you devs needs to add an error for case {code}!")


def get_output_variant(path: pathlib.Path) -> str:
    """
    Takes a path to a file and replaces the first case of the input directory
    with the output directory to create the output files path.
    """
    return str(path).replace(userspace.input_content_directory, userspace.output_directory, 1)