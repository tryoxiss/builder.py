def compile(string: str, *, config):
    """
    The compiler interface for Modern Markdown.
    """

    print(config["italics"])

    for line in string.splitlines():
        print(f"{line}")

class ModernMarkdownConfig:

    # . = span with class
    # thing.class = element wioth the class
    # thing#id = elemnt with that id
    # can be combined with .
    # if its capitalised its a component, not an element.

    # Remove a token from the list or replace its html value with
    # an empty string to remove it.
    simple_inline = {
        "*": "em",
        "/": "em",
        "**": "strong",
        "__": "u", # DEPRECATED
        "^": "sup",
        "_": "sub",

        "--": "del",
        "++": "ins",

        "~~": "s",

        "==": "mark",
        "===": "mute",

        "||": "Spoiler",

        "`": "code",

        # "***": "hr",
        # "---": "hr"
    }

    do_right_align = True
    do_left_align = True
    do_center_align = True

    # -------

    do_autolinks = True
    do_links = True

    do_tables = True

    do_callouts = True
    callout_components = { # HTTL = HyperText Template Language
        "info": "Info",
        "warn": "Warn",
        "question": "Faq",
        "faq": "Faq",
        "danger": "Danger",
    }


class ModernMarkdown:
    def __init__(self):
        pass
    
    def inline_token():
        pass
    
    def list_token():
        pass
    
    def callout():
        pass
    
    # etc ...