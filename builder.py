import builder_modules.core as core # Ignore this <3
import builder_modules.modern_markdown as modern_markdown
import builder_modules.htcl_template as htcl_template
import builder_modules.core_classes as classes
import builder_modules.log as log

host_to_lan = False
mode = "live" # live | release

# Main config variables! These are what you most likely want to tweak.
input_content_directory = "content"
content_file_extention = [".md", ".txt"]
only_template_compilation = [".htcl", ".httl"]
input_component_directory = "components"

output_directory = "target"
content_output_extension = ".html"

recursion_upper_bound = 99

prettify_links = True

md_config = modern_markdown.ModernMarkdownConfig()

# Example on removing simple inline syntax
md_config.simple_inline["/"] = ""

# Example on adding simple inline syntax
md_config.simple_inline["?"] = "mew"

# This is more complex, feel free to ignore everything below this!

def build(file: classes.File) -> int:
    """
    Defines the per-file build process. The return value is 0 if it was
    built successfully and false if an error occured. (Feel free to change
    this as needed)
    """

    # TODO: Skip through the header for modern markdown or remove it initially and turn it into variables

    file.content = modern_markdown.compile(file.content, config=md_config)
    # This is where you add extensions! Just run its function
    # as part of the build process

    # TODO: Apply htcl template

    # check dead links
    # minify
    # generate permalink

    file.write_fancy(core.get_output_variant(f"{file.without_extension()}"))

    return 0

# Now we just run the main process!
if __name__ == "__main__":
    # md_config.simple_inline["||"] = "OwO"

    # print(md_config.simple_inline["/"])
    # print(md_config.simple_inline["?"])

    log.info("meow")
    log.warning("meow")
    log.debug("meow")
    log.fatal("meow")

    log.found("file")
    log.built("file")
    log.reload("file")

    if mode == "live":
        core.run(lan=host_to_lan)
    elif mode == "release":
        core.build_release()