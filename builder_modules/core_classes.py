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

    def name(self) -> str:
        """
        Returns the files name.
        """
        return self.path.rsplit('/', 1)[-1]

    def without_extension(self) -> str:
        """
        Returns the files full path without the extension.
        """
        return self.path.rsplit('.', 1)[0]

    def extension(self) -> str:
        """
        Returns the files extension, like `.md`.
        """
        return self.path.rsplit('.', 1)[-1]

    def name_without_extension(self) -> str:
        """
        Returns the files name without the extension.
        """
        return self.path.rsplit('.', 1)[0].rsplit('/', 1)[-1]

    def write_to(self, path: str, *, safety=1): # may also need to take content.
        """
        Writes a compiled file to the absolute path provided, overwriting a
        previous file if existent, creating any folders that do not yet exist.

        [!] DANGER: This function is blind! It will overwrite anything at the desired path!
        """

        if os.path.exists(path) == False:
            # This errors because it tries to then read from this directory that was just made.
            # We need to make this not make the last directory.
            os.makedirs(path)

        file = open(f"{path}", "w")
        file.write(self.content)
        file.close()

    def write_fancy(self, path: str, *, safety=1, extension="html"): # may also need to take content.
        """
        Writes a compiled file to the absolute path provided, followed by `/index.html
        to add a trailing slash in browsers. overwriting a previous file if existent,
        creating any folders that do not yet exist.

        [!] DANGER: This function is blind! It will overwrite anything at the desired path!
        """

        # Note: normally it goes to {path}/index.html, but if you had
        # /posts/kittentd-devlog-1/
        #       kittentd-devlog-1.md
        #       screenshot1.png
        #       (etc)
        #
        # then it would get written to /posts/kittentd-devlog-1/kittentd-devlog-1/index.html, which is ugly. So if the files name
        # is the same as the directories or is `index` we want it to not create another directory.
        #
        # we also want to allow for pattersn like /posts/12/sep/2023/ and allow writing to multiple locations.

        if os.path.exists(path) == False:
            os.makedirs(path)

        file = open(f"{path}/index.{extension}", "w")
        file.write(self.content)
        file.close()