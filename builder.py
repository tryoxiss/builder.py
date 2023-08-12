import builder_backend as builder # Ignore this <3

# Main config variables! These are what you most likely want to tweak.
input_directory = "source"
output_directory = "built"
prettify_links = True

# This is more complex, feel free to ignore everything below this!

def process(file: File) -> bool:
    """
    Defines the per-file build process. The return value true if it was
    built successfully and false if an error occured. (Feel free to change
    this as needed)
    """

    file = builder.ModernMarkdown.compile(file)
    # This is where you add extensions! Just run its function
    # as part of the build process

    return 0

# Now we just run the main process!
def build():
    builder.run()