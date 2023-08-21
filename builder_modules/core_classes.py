import builder as userspace
import os

class File:
    """
    A custom file class for builder.py.
    """

    content = str
    path = str

    def __init__(self, path: str):
        # Import current content file and pass to the builder

        # Opens the buildable file in read only
        self.content = open(f'{path}', "r").read()

        # Stores the files path
        self.path = path

        # log.debug("File: ", self.name, " at location: ", self.path " has been created")
    
    def write_to(self, path: str, *, safety=1): # may also need to take content.
        """
        Writes a compiled file to the absolute path provided, overwriting a 
        previous file if existent, creating any folders that do not yet exist.

        [!] DANGER: This function is blind! It will overwrite anything at the desired path,
        consider using `write()` for a less blind function! (Fix this!)
        """

        if os.path.exists(path) == False:
            os.makedirs(path)

        file = open(f"{path}/index{userspace.content_output_extension}", "w")
        file.write(self.content)
        file.close()