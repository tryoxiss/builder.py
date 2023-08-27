# The API you have access to by default in <?py/> blocks.

# Should probably be core not api? idk
# def paginate(per_page: int, posts: list):
#     """

#     """

#     pass

def htcl(string: str):
    """
    Insert the provided HTCL string into the page. This will be compiled
    fully into components in a later step.

    WARNING: NOT IMPLEMENTED!
    """

def html(string: str):
    """
    Insert the provided HTML string into the page. This will NOT be
    further compiled at a later stage, consider using `insert_htcl`
    if you want to use components.

    WARNING: NOT IMPLEMENTED!
    """

def text(string: str):
    """
    Insert the provided text string into the page. All HTML and
    HTCL

    WARNING: NOT IMPLEMENTED!
    """

def paginate(per_page: int):
    """
    Paginate the post list into multiple pages, with the `per_page` argument
    being used to determine how many are on each page.

    NOTE: This function does not actually handle pagination, and is instead
    a signal to the rest of the builder on how to paginate content, thus its
    behavour cannot be replicated.
    """

# We may need this
# class Pagination:
#     pass

# # for post in api.collections.posts.paginate()
# # for post in api.collections.<Collection Name>.paginate()

# class Collection:
#     """
#     A class that every collection should inherit from.
#     """
#     # INDEX   POURPOSE
#     # -----   --------
#     #    0    index page, same as page 1 by default
#     # [...]   replaces the `$page` variable in the path.

#     index_pages = []
#     content_pages = []

#     def __init__(self, *, content: list = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]):
#         pass

#     def paginate(self, per_page: int):
#         local_index_pages = []
#         local_content_pages = self.content_pages

#         while local_content_pages != []:
#             local_page = []

#             for page in range(per_page):
#                 local_page = local_page.append(page)
#                 local_content_pages.pop(0)
            
#             local_index_pages = local_index_pages.append(local_page)
        
#         self.index_pages = local_index_pages

# collection = Collection()
# collection.paginate(4)

# print(collection.index_pages)