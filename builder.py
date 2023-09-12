import builder_modules.core as core # Ignore this <3
import builder_modules.modern_markdown as modern_markdown
import builder_modules.htcl_template as htcl_template
import builder_modules.core_classes as classes
import builder_modules.log as log
import builder_modules.config as config

host_to_lan = False
mode = "live" # live | release

# Main config variables! These are what you most likely want to tweak.
# In most IDE's you can CTRL+Click on the `config.` to view all variables!
config.content.extensions = [".md", ".mmd", ".txt"]
config.components.extensions = [".htcl", ".httl"]

md_config = modern_markdown.ModernMarkdownConfig()

# Example on removing simple inline syntax
md_config.simple_inline["/"] = ""

# Example on adding simple inline syntax
md_config.simple_inline["?"] = "mew"

# This is more complex, feel free to ignore everything below this!

def build(file: classes.File) -> None:
    """
    Defines the per-file build process. This function returns nothing :3
    """

    # TODO: Skip through the header for modern markdown or remove it initially and turn it into variables

    # Example of how you can compile files with diffrent extensions.
    # match file.extension():
    #     case "md":
    #         file.content = modern_markdown.compile(file.content, config=md_config)
    #     case _:
    #         pass

    # file.content = modern_markdown.compile(file.content, config=md_config)

    # This is where you add extensions! Just run its function
    # as part of the build process

    # TODO: Apply htcl template

    # check dead links
    # minify
    # generate permalink

    file.write_fancy(core.get_output_variant(f"{file.without_extension()}"))

# Now we just run the main process!
if __name__ == "__main__":
    if mode == "live":
        core.run(lan=host_to_lan)
    elif mode == "release":
        core.build_release()