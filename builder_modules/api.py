# The API you have access to by default in <?py/> blocks.

# Should probably be core not api? idk
# def paginate(per_page: int, posts: list):
#     """

#     """

#     pass

def insert_htcl(string: str):
    """
    Insert the provided HTCL string into the page. This will be compiled
    fully into components in a later step.

    WARNING: NOT IMPLEMENTED!
    """

def intert_html(string: str):
    """
    Insert the provided HTML string into the page. This will NOT be
    further compiled at a later stage, consider using `insert_htcl`
    if you want to use components.

    WARNING: NOT IMPLEMENTED!
    """

def intert_text(string: str):
    """
    Insert the provided text string into the page. All HTML and
    HTCL

    WARNING: NOT IMPLEMENTED!
    """