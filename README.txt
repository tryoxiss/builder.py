
Website builder for use by Shefie Games Studios and the general public
v. 0.0.0.1

FOR HTML EDITORS:

    In '<title>' always include '{title}' to add the title, otherwise it will be missed entirely. 

    To get the background image before content you must have:  '<header style="background-image: url('{background_image_url}'); ">'
    
    The first part ({h1}) is styled differently than the second {aft_colon} as well as has a colon after it. '<h1>{h1}<span>{aft_colon}</span></h1>' must be included even if there will be no such after colon!

    ALL content will be posted EVERY time {content} is called. Likely you will not want it pasted multiple times in the base.html file.

    WORK IN PROGRESS: 'Use {author_date_name} to display the authors name, the date, and time of postage. Though will adapt if there is no author name.'
    
ADD THIS (blocks)
#                   if '- ``' in markdown_list[j]: # bugfix
#                       pass
#                   if '- ' in markdown_list[j]: # unordered list item
#                       pass

AND THESE (in line)
#                    if '[' and '(' in markdown_list[j]: # embeded link
#                        pass
#                    if '[' or '[[' in markdown_list[j]: # wiki link
#                        pass


FOR MARKDOWN EDITORS:
