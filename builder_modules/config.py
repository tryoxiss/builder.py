# This file makes use of classes to organise variables. That is why they are lowercase.

class content:
    directory:  str       = "content"
    extensions: list[str] = [".md"]

class components:
    directory:   str       = "components"
    extensions:  list[str] = [".htcl"]

class output:
    directory:     str  = "target"
    exclude_tags:  list[str] = ["#exclude", "#draft"]

max_recursion = 64