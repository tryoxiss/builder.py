def compile(string: str, *, config):
    """
    The compiler interface for Modern Markdown.
    """

    compiler = ModernMarkdownCompiler(config=config)
    compiler.compile(string)

    # print(string)

class ModernMarkdownCompiler:
    lines = []
    config = None

    def __init__(self, *, config):
        self.config = config

    def find_token(self, string: str, index: int) -> str:
        """
        Takes a string and an index and will provide the token found. 
        If no token is found then it will supply an empty string.
        """
        length = self.config.simple_inline_max_token_length

        while length > 0:
            # Checks if from the given index to the current length if a token
            # from the list is contained within the string slice.
            if self.config.simple_inline.__contains__(string[index:length + index]) == False:
                length -= 1
                continue

            return string[index:length + index]
        return ""

    def tokenize(self, string: str) -> list:
        """
        Takes a string and uses the Mondern Markdown Config to return a 
        tokenized array of the string.
        """
        line = []
        since_last_token = 0
        character = 0

        while character <= len(string) - 1:
            token = self.find_token(string, character)

            if token == "":
                since_last_token += 1
                character += 1
            else:
                line.append(string[character - since_last_token:character])
                since_last_token = 0
                line.append(token)
                character += len(token)

        return line




    def replace(self, line: list):
        """
        Takes in a tokenized list and outputs a list with each token replaced 
        with its value in simple_inline.
        """
        for index, token in enumerate(line):
            if self.config.simple_inline.__contains__(token) == False:
                continue

            if line[index:-1].count(token) <= 0:
                continue

            next_similar_token = line[index + 1:].index(token) + (index + 1)
            line[next_similar_token] = f"<{self.config.simple_inline[token]}/>"
            line[index] = f"<{self.config.simple_inline[token]}>"
        
        return line

    def compile(self, string: str) -> str:
        """
        Takes in a ModernMarkdown string and outputs it compiled to HTML.
        This string may be of an arbatrary size and contain many lines,
        such as a single paragraph or an entire document.
        """
        splitlines = string.splitlines()
        new_lines = ""

        line = 0
        while line <= len(splitlines) - 1:
            tokenized_line = self.tokenize(splitlines[line])
            new_lines += "".join(self.replace(tokenized_line)) + "\n"
            line += 1
        
        self.lines = new_lines
        return self.lines

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

    # Get the max length of any string inside of the simple inline dictionary.
    # This is used inside of the function to find the max amount of characters 
    # it must look at, at once.
    simple_inline_max_token_length = 0

    for value in simple_inline.keys():
        if len(value) > simple_inline_max_token_length:
            simple_inline_max_token_length = len(value)
    
    ## like simple inline tokens but instead of requireing on both sides and requireing an html tag and it 
    # see something and it will replace it if it is not a vaild token it will replace it wiwth the character on the se
    # cond thing for example two hyphens would replace it with an emdash
    # (EMOJIS BASICALLY) (NOT APART O FTHIS FILE?) <- Maybe

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