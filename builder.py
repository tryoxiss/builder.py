import builder_backend as builder # Ignore this <3

# Main config variables! These are what you most likely want to tweak.
input_content_directory = "content"
content_file_extention = ".md"
input_component_directory = "components"

output_directory = "target"
content_output_extension = ".html"

prettify_links = True

# This is more complex, feel free to ignore everything below this!

def build(file: builder.File) -> bool:
    """
    Defines the per-file build process. The return value true if it was
    built successfully and false if an error occured. (Feel free to change
    this as needed)
    """

    file = builder.ModernMarkdown.compile(file)
    # This is where you add extensions! Just run its function
    # as part of the build process

    # check dead links

    # write to destination
    # minify

    # generate permalink

    return 0

# Now we just run the main process!
builder.run()