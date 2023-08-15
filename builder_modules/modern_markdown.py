def compile(string: str, *, config):
    """
    The compiler interface for Modern Markdown.
    """

    compiler = ModernMarkdownCompiler(config=config)
    compiler.compile(string)

    print(string)

class ModernMarkdownCompiler:
    lines = []
    config = None

    def __init__(self, *, config):
        self.config = config

    def tokenize(self, string: str):

        lines = []

        since_last_token = 0
        character = 0
        # for i in range(0, len(string)):
        while character <= len(string) - 1:
            
            if self.config.simple_inline.__contains__(string[character]) == False:
                since_last_token += 1
                character += 1
                continue

            lines.append(string[character - since_last_token:character])
            since_last_token = 0

            lines.append(string[character])
            character += 1

            # if self.config.simple_inline.__contains__(string[character] + string[character + 1]) == False:
            #     character += 1
            #     continue 

            # lines[len(lines)] += string[character]

        print(lines)




    def replace(self, string: str):
        pass

    def compile(self, string: str) -> str:

        splitlines = string.splitlines()
        new_lines = ""

        line = 0
        while line <= len(splitlines) - 1:
            splitlines[line] = self.tokenize(splitlines[line])
            # self.lines[i] = self.replace(line)
            line += 1
        
        # Conbine into one string to return
        return ""

class ModernMarkdownConfig:

    # . = span with class
    # thing.class = element with the class
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