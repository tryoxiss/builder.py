import builder_modules.core as core # Ignore this <3
import builder_modules.modern_markdown as modern_markdown

# Main config variables! These are what you most likely want to tweak.
input_content_directory = "content"
content_file_extention = [".md", ".txt"]
only_template_compilation = [".htcl", ".httl"]
input_component_directory = "components"

output_directory = "target"
content_output_extension = ".html"

prettify_links = True

md_config = modern_markdown.ModernMarkdownConfig()

# Example on removing simple inline syntax
md_config.simple_inline["/"] = ""

# Example on adding simple inline syntax
md_config.simple_inline["?"] = "mew"

# This is more complex, feel free to ignore everything below this!

def build(file) -> int:
    """
    Defines the per-file build process. The return value true if it was
    built successfully and false if an error occured. (Feel free to change
    this as needed)
    """

    # core.shutil.copyfile(file.name, core.get_output_file(file.name))

    # print(modern_markdown_config.do_meow)

    file.content = modern_markdown.compile(file.content, config=md_config)
    # This is where you add extensions! Just run its function
    # as part of the build process

    # check dead links
    # minify
    # generate permalink

    # file.write_to(f"{file.path.rstrip(userspace.content_file_extention)}/index.html")

    return 0

# Now we just run the main process!
if __name__ == "__main__":
    # md_config.simple_inline["||"] = "OwO"

    # print(md_config.simple_inline["/"])
    # print(md_config.simple_inline["?"])

    core.run()