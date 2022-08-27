markdown_names_list = open('__templates/build_list.txt', 'r')
markdown_names_list = markdown_names_list.readlines()
for i in range(len(markdown_names_list)):
    markdown_names_list[i] = markdown_names_list[i].rstrip('\n')

base_html = open('__templates/base.html', 'r')  # this file needs to also exist in the directory, its what we will copy code from while building the new file. it is also read only
base_html_list = base_html.readlines()

print(len(markdown_names_list))

for n in range(len(markdown_names_list)):
    markdown = open(f'{markdown_names_list[n]}', "r")    # sets the file you wanted to be edited into the variable "markdown" and sets it to be read-only (so we dont break it)
    markdown_list = markdown.readlines()
    markdown_names_list[n] = markdown_names_list[n].rstrip('.md')
    markdown_names_list[n] = markdown_names_list[n].lstrip('_mystuff/')
    html_export = open(f'mystuff/{markdown_names_list[n]}.html', "w")

    for i in range(len(base_html_list)):
        if '{title}' in base_html_list[i]:
            html_export.write(base_html_list[i].replace('{title}', markdown_names_list[n].replace('-', ' '))) # remove - and replace with ' '
        elif '{background_image_url}' in base_html_list[i]:
            for j in range(0, len(markdown_list)):
                if 'background_image: ' in markdown_list[j]:
                    html_export.write(base_html_list[i].replace('{background_image_url}', (markdown_list[j].lstrip('background_image: ')).rstrip(") \n")))
                    break
        elif '{h1}' in base_html_list[i]:
            for j in range(0, len(markdown_list)):
                if '# ' in markdown_list[j]:
                    if ': ' in markdown_list[j]:
                        html_export.write((base_html_list[i].replace('{h1}',(markdown_list[j].lstrip("# ")).split(': ')[0])).replace('{aft_colon}',': ' + (markdown_list[j].split(': ')[1].rstrip('\n'))))
                        break
                    else:
                        html_export.write((base_html_list[i].replace('{h1}',((markdown_list[j].lstrip("# ")).rstrip('\n')))).replace('<span>{aft_colon}</span>',''))
                        break

        elif '{content}' in base_html_list[i]:

            temp_count = 0
            for j in range(len(markdown_list)):
                if '---' in markdown_list[j]:
                    temp_count += 1
                    continue
                if temp_count == 2:
                    start_pos = j
                    break

            temp_count = 0
            for j in range(start_pos, len(markdown_list)):
                if temp_count > 0:
                    if '```' in markdown_list[j]:
                        html_export.write('</code></pre>')
                        temp_count = 0
                        continue
                    else: 
                        html_export.write(markdown_list[j])
                        continue
                elif '<!--' and '-->' in markdown_list[j]:
                    continue
                elif '###### ' in markdown_list[j]: # header 6
                    continue
                elif '##### ' in markdown_list[j]: # header 5
                    continue
                elif '#### ' in markdown_list[j]: # header 4
                    continue
                elif '### ' in markdown_list[j]: # header 3
                    html_export.write("        <h3>" + (markdown_list[j].lstrip('### ')).rstrip(' \n') + "</h3>\n")
                    continue
                elif '## ' in markdown_list[j]: # header 2
                    html_export.write("        <h2>" + (markdown_list[j].lstrip('## ')).rstrip(' \n') + "</h2>\n")
                    continue
                elif '# ' in markdown_list[j] and '\# ' not in markdown_list[j]: # header 1
                    print("\n(possibly)TWO HEADERS IN THIS, FILE: " + markdown_names_list[n].lstrip('\n') + ", LINE: " + markdown_list[j])
                    continue
                elif markdown_list[j].startswith('> '): # blockquote
                    html_export.write("        <blockquote>" + (markdown_list[j].lstrip('> ')).rstrip(' \n') + "</blockquote>\n")
                    continue
                elif '---' in markdown_list[j]: # horisontal rule
                    html_export.write("        <hr>\n")
                    continue
                elif '```' in markdown_list[j]: # codeblock
                    temp_count += 1
                    html_export.write('<pre><code class="' + (markdown_list[j].strip('```')).strip('\n') + '">')
                    continue
                elif markdown_list[j] != '\n':
                    html_export.write("        <p>" + markdown_list[j].rstrip('\n') + "</p>\n")
                    continue


        #         # if '![' and '(' in markdown_list[j]: # image

        #         #     split_image_alt = markdown_list[j].split("[","(")
        #         #     alt_unedited = markdown_list[j].rstrip(" \n")
        #         #     alt = author_unedited.lstrip("")
        #         #     image_link = (markdown_list[j].lstrip("![")).rstrip(" \n")

        #         #     if alt_unedited == 'alt=':
        #         #         html_export.write(f'<img src="{image_link}"')
        #         #     else:
        #         #         html_export.write(f'<img src="{image_link}" alt={alt}')
        #         #     pass


        #         # if '- ' in markdown_list[j]: # unordered list item
        #         #     pass
        #         # if '- ``' in markdown_list[j]: # bugfix
        #         #     pass
        #         # if '***' in markdown_list[j]: # bold and italics
        #         #     pass
        #         # if '**' in markdown_list[j]: # bold
        #         #     pass
        #         # if '*' in markdown_list[j]: # italics
        #         #     pass
        #         # if '__' in markdown_list[j]: # underline
        #         #     pass
        #         # if '`' in markdown_list[j]: # inline codeblock
        #         #     pass
        #         # if '```' in markdown_list[j]: # multiline codeblock
        #         #     pass
        #         # if '~~' in markdown_list[j]: # strike-through
        #         #     pass
        #         # if '$$' in markdown_list[j]: # mathmatical formula (use same as codeblock for now but that might change later)
        #         #     pass
        #         # if '[' and '(' in markdown_list[j]: # embeded link  # THIS MAY NOT WORK
        #         #     pass
        #         # if '[' or '[[' in markdown_list[j]: # wiki link
        #         #     pass
        #         # if '||' in markdown_list[j]: # spoiler
        #         #     pass
        #         # if '--'  in markdown_list[j]: # em dash
        #         #     pass
        #         # for b in range(0, 99):
        #         #     if f'{i}. ' in markdown_list[j]:
        #         #         pass
            continue
        
        else: 
            html_export.write(base_html_list[i])


# × 
# At some point I want to make mathmatical forumulas display how they would be written, for example 1+2(3 / (2 / 3) would display as)
#  1 + 2 x ( 3 )
#           ---
#           22
#           ---
#           3.5
# but like, actually nice and not plain text obviously. 
# also make multiplcation either the cirlce or the symbol, probably the circle. 


# -==-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-= THIS IS FOR AUTHOR_DATE_READTIME (for when I do it later)
        # elif '{author_date_readtime}' in base_html_list[i]:
        #     for j in range(0, len(markdown_list)):
        #         if 'author=' in markdown_list[j]:
        #             author_unedited = markdown_list[j].rstrip(" \n")
        #             author = author_unedited.lstrip("author=")
        #             continue
        #         elif 'readtime=' in markdown_list[j]:
        #             readtime = (markdown_list[j].lstrip("readtime=")).rstrip(" \n")
        #             continue
        #     _date = markdown_date.replace('-', ' ')
        #     if author_unedited == 'author=':
        #         html_export.write(base_html_list[i].replace('{author_date_readtime}', f'Posted on {_date}. Read time is about {readtime}'))
        #     else:
        #         html_export.write(base_html_list[i].replace('{author_date_readtime}', f'Posted by {author} on {_date}. About a {readtime}'))