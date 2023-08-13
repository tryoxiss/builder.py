__version__ = 'v0.0.3'

import pathlib
import os
import shutil
import time

import builder as userspace

# class ModernMarkdown:
#     def compile(file: File):
#         pass

class File:

    initial_content = str
    built_content = str
    name = str

    def __init__(self, path: str):
        # Import current content file and pass to the builder

        # Opens the buildable file in read only
        self.initial_content = open(f'{path}', "r").readlines()
        
        # Stores the filename
        self.name = path.rstrip(userspace.content_file_extention)

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

def search_buildable_files(child):
    if os.path.isdir(child) == False:
        return
    
    os.mkdir(userspace.output_directory)
    for child in pathlib.Path(child).iterdir():
        if os.path.isdir(child) == False:
            return

        if child.suffix == userspace.content_file_extention:
            print(child.stat())
            userspace.build( File(str(child)) )
        else:
            # shutil.copyfile(child, child)
            pass
        
        search_buildable_files(child)

