def compile(string: str, *, config):
    """
    The compiler interface for Modern Markdown.
    """

    compiler = HTCLTemplate(config=config)
    compiler.compile(string)


class HTCLTemplateConfig:
    pass