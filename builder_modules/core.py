__version__ = 'v0.0.3'

import pathlib
import os
import shutil
import time

import log

import builder as userspace

class File:

    content = str
    name = str
    path = str

    def __init__(self, path: str):
        # Import current content file and pass to the builder

        # Opens the buildable file in read only
        self.content = open(f'{path}', "r").readlines()
        self.path = path
        # Stores the filename
        self.name = path.rstrip(userspace.content_file_extention)
    
    def write_to(path: str):
        # Write to the path provided, inside the project root then `userspace.output_directory`
        # of course remove the input path from the thing.
        pass

def run():
    find_and_build_files()

def find_and_build_files():
    # loop over every file
    # run the per-file build process
    for child in pathlib.Path().iterdir():
        if os.path.isdir(child) == False:
            return
    
        if (child.name == userspace.input_content_directory):
            search_buildable_files(child)

# WARNING: This is recursive! We need to put an upper limit on recursions!
def search_buildable_files(child):
    if os.path.isdir(child) == False:
        return
    
    os.mkdir(userspace.output_directory)
    for child in pathlib.Path(child).iterdir():
        if os.path.isdir(child) == False:
            return

        if child.suffix != userspace.content_file_extention:
            continue

        print(child.stat())
        response = userspace.build( File(str(child)) )

        match response:
            case 0:
                log.ok()
        
        search_buildable_files(child)

