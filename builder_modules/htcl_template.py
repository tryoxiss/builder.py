def compile(string: str, *, config):
    """
    The compiler interface for Modern Markdown.
    """

    compiler = HtclTemplate(config=config)
    compiler.compile(string)

# NOTE TO KHAIM:
# Scropes styles are done with a class added to all sectors in an object, and are per unique component.
# As in, two <Button>s don't need to have diffrent scopes or even re-inject styles since they are the
# same. As long as they are unique. I might try a class called `.scope_ComponentName` though? Since
# you can only have one component named the same thing, that should be gaurnteed to be unique.

# NOTE ON IMPLEMENTING LISTS:
# Semantically, a list inside a list SHOULD be contained inside an <li>
# So:
# <ul>
#     <li> Content
#     <ul>
#         <li>Nested Item</li>
#     </ul>
#     </li>
# </ul>

class HtclTemplateConfig:
    pass

class HtclTemplate:
    def __init__(self, *, config):
        pass

class HtclDocument:
    def __init__(self):
        pass

class HtclNode:
    name = "Meow"
    contents = list
    attributes = dict

    def __init__(self):
        name = "meow"
        contents = []
        attributes = {}

    def is_component(self):

        if len(self.name) >= 1:
            return self.name[0].isupper()
        else:
            return False

    def create_node():
        pass