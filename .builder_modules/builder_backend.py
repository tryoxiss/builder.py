__version__ = 'v0.0.3'

import pathlib
import os
import shutil
import time

import builder as userspace

class ModernMarkdown:
    def compile(file: File):
        pass

class File:

    initial_content = str
    built_content = str
    name = str

    def __init__(self: self, content: str, name: str):
        self.initial_content = content
        self.name = name

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
            userspace.build(str(child))
            pass
        else:
            shutil.copyfile(child, child)
        
        search_buildable_files(child)

def build(path: str):
    # Import current content file and pass to the builder

    # Opens the buildable file in read only
    file_content = open(f'{path}', "r").readlines()
    
    # Stores the filename
    file_name = path.rstrip(userspace.content_file_extention)

    # Create the file class
    file = File(file_content, file_name)

    # Pass the file to be built
    userspace.build(file)