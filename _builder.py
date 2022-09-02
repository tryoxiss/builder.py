markdown_names_list = open('__templates/build_list.txt', 'r')
markdown_names_list = markdown_names_list.readlines()
for i in range(len(markdown_names_list)):
    markdown_names_list[i] = markdown_names_list[i].rstrip('\n')

base_html = open('__templates/base.html', 'r')  # this file needs to also exist in the directory, its what we will copy code from while building the new file. it is also read only
base_html_list = base_html.readlines()

percent = '\033[90m'
addinfo = '\033[90m'
warning = '\033[93m'
build_error = '\033[91m'
success = '\033[92m' 
fatal = '\033[91m' 
impinfo = '\033[97m'
body = '\033[0m' 
# blue = '\033[94m'

ABORTED = False
files_to_delete = len(markdown_names_list)
files_to_build = len(markdown_names_list)
files_built = 0
percent_complete = 0


def styletag_warning(style_type):
    print(f'{warning}WARNING:{body} file {impinfo}{markdown_names_list[n]}{body} on line {impinfo}{j}{body} there is only an opening set of {style_type}, it will show up as itself instead of turning into the appropriate style tags.')

def styletag_change(current_line, md_tag, style_type, html_tag, html_closing_tag, error_byte):
    current_count = 0
    for k in range(0,40):
        if current_count == 1 and f'{md_tag}' in current_line:
            current_line = current_line.replace(f'{md_tag}', f'{html_closing_tag}', 1)
            current_count = 0
        elif current_count == 1 and f'{md_tag}' not in current_line:
            styletag_warning(style_type)
            current_line = error_byte.join(current_line.rsplit(f'{html_tag}', 1))
            break
        elif f'{md_tag}' in current_line:
            current_line = current_line.replace(f'{md_tag}', f'{html_tag}', 1)
            current_count += 1
    return current_line







print(f'{addinfo}INFO: {body} builder.py will DELETE and then REBUILD ALL files.')
print(f'{fatal}{files_to_delete}{body} will be {fatal}DELETED{body}')
print(f'{success}{files_to_build}{body} will be {success}BUILT{body}')
changes_ok = input(f'Are these changes OK ({success}Y{body}/{fatal}n{body}): ')

if 'Y' in changes_ok: print(f'{success}Process Started!{body}')
else: ABORTED = True 

if ABORTED == True: 
    print(f'{fatal}Process Ending...{body}')
    exit()
#     print(f'{warning}WARNING: {body} The document DOCUMENT has more than one heading 1, the seccond one will be ommitted.')
#     print(f'{build_error}BUILD ERROR:{body} This document contained an invalid character, it will be skipped. {addinfo}(INVALID CHARACTERS: / \ : * ? " > < |){body}')
#     print(f'{fatal}FATAL ERROR: A document contained a backdoor to the main frame and the process could not continue.{body}')

for n in range(len(markdown_names_list)):

    markdown = open(f'{markdown_names_list[n]}', "r")    # sets the file you wanted to be edited into the variable "markdown" and sets it to be read-only (so we dont break it)
    markdown_list = markdown.readlines()
    markdown_names_list[n] = markdown_names_list[n].rstrip('.md')
    markdown_names_list[n] = markdown_names_list[n].lstrip('_mystuff/')
    html_export = open(f'mystuff/{markdown_names_list[n]}.html', "w")
    language_current = ''

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
        elif '{language}' in base_html_list[i]:
            for j in range(0, len(markdown_list)):
                if 'language: ' in markdown_list[j]:
                    language_current = (markdown_list[j].lstrip('language: ')).rstrip('\n')
            for j in range(0, len(markdown_list)):
                if 'line-numbers: true' in markdown_list[j]:
                    html_export.write((base_html_list[i].replace('{language}', language_current)).replace('{line-numbers}', 'line-numbers'))

        elif '{content}' in base_html_list[i]:
            temp_count = 0
            for j in range(len(markdown_list)):
                if '---' in markdown_list[j]:
                    temp_count += 1
                    continue
                if temp_count == 2:
                    start_pos = j
                    break
            
            header_one_count = 0
            temp_count = 0
            for j in range(start_pos, len(markdown_list)):
                if markdown_list[j].startswith('\n'):
                    pass
                else: 
                    current_line = "<p>" + markdown_list[j].rstrip('\n') + "</p>\n"
                if temp_count > 0:
                    if '```' in markdown_list[j+1]:
                        html_export.write(markdown_list[j].replace('\n', ''))
                    elif '```' in markdown_list[j]:
                        html_export.write('</code></pre>\n')
                        temp_count = 0
                        continue
                    else: 
                        html_export.write(markdown_list[j])
                        continue
                elif '<!--' and '-->' in markdown_list[j]:
                    continue
                elif '####### ' in markdown_list[j]: # header 7 (DOESNT EXIST)
                    print(f'{warning}WARNING: {body}The document {impinfo}' + markdown_names_list[n].rstrip('\n') + f'{body} on line {impinfo}' + str(j) + f'{body} has a heading larger than 6, it will not be included.')
                    continue
                elif '###### ' in markdown_list[j]: # header 6
                    current = ((markdown_list[j].lstrip('###### ')).rstrip('\n')).split(' {') # 'title', 'id}'
                    if len(current) >= 2:
                        html_export.write('<h6 id="' + current[1].rstrip('}') + '">' + current[0] + '</h6>\n')
                    else: 
                        print(f'{warning}WARNING:{body} file {impinfo}{markdown_names_list[n]}{body} on line {impinfo}{j} does not have a header ID.')
                        html_export.write('<h6>' + current[0] + '</h6>\n')
                    continue
                elif '##### ' in markdown_list[j]: # header 5
                    current = ((markdown_list[j].lstrip('##### ')).rstrip('\n')).split(' {') # 'title', 'id}'
                    if len(current) >= 2:
                        html_export.write('<h5 id="' + current[1].rstrip('}') + '">' + current[0] + '</h5>\n')
                    else: 
                        print(f'{warning}WARNING:{body} file {impinfo}{markdown_names_list[n]}{body} on line {impinfo}{j} does not have a header ID.')
                        html_export.write('<h5>' + current[0] + '</h5>\n')
                    continue
                elif '#### ' in markdown_list[j]: # header 4
                    current = ((markdown_list[j].lstrip('#### ')).rstrip('\n')).split(' {') # 'title', 'id}'
                    if len(current) >= 2:
                        html_export.write('<h4 id="' + current[1].rstrip('}') + '">' + current[0] + '</h4>\n')
                    else: 
                        print(f'{warning}WARNING:{body} file {impinfo}{markdown_names_list[n]}{body} on line {impinfo}{j} does not have a header ID.')
                        html_export.write('<h4>' + current[0] + '</h4>\n')
                    continue
                elif '### ' in markdown_list[j]: # header 3
                    current = ((markdown_list[j].lstrip('### ')).rstrip('\n')).split(' {') # 'title', 'id}'
                    if len(current) >= 2:
                        html_export.write('<h3 id="' + current[1].rstrip('}') + '">' + current[0] + '</h3>\n')
                    else: 
                        print(f'{warning}WARNING:{body} file {impinfo}{markdown_names_list[n]}{body} on line {impinfo}{j} does not have a header ID.')
                        html_export.write('<h3>' + current[0] + '</h3>\n')
                    continue
                elif '## ' in markdown_list[j]: # header 2
                    current = ((markdown_list[j].lstrip('## ')).rstrip('\n')).split(' {') # 'title', 'id}'
                    if len(current) >= 2:
                        html_export.write('<h2 id="' + current[1].rstrip('}') + '">' + current[0] + '</h2>\n')
                    else: 
                        print(f'{warning}WARNING:{body} file {impinfo}{markdown_names_list[n]}{body} on line {impinfo}{j} does not have a header ID.')
                        html_export.write('<h2>' + current[0] + '</h2>\n')
                    continue
                elif '# ' in markdown_list[j] and '\# ' not in markdown_list[j]: # header 1
                    header_one_count += 1
                    if header_one_count >= 2:
                        print(f'{warning}WARNING: {body}The document {impinfo}' + markdown_names_list[n].rstrip('\n') + f'{body} on line {impinfo}' + str(j) + f'{body} has more than one heading 1, the seccond one will not be included')
                        continue
                    continue
                elif markdown_list[j].startswith('> '): # blockquote
                    html_export.write("<blockquote>" + (markdown_list[j].lstrip('> ')).rstrip(' \n') + "</blockquote>\n")
                    continue
                elif '---' in markdown_list[j]: # horisontal rule
                    html_export.write("<hr>\n")
                    continue
                elif '```' in markdown_list[j]: # codeblock
                    temp_count += 1
                    html_export.write('<pre><code class="language-' + (markdown_list[j].lstrip('``` ')).rstrip(' \n') + '">')
                    continue
                elif '![' in markdown_list[j] and '\![' not in markdown_list[j]: # image
                        split_image = markdown_list[j].split(']')
                        image_link = (split_image[1].lstrip('(')).rstrip(') \n')
                        alt = split_image[0].lstrip("![")
                        html_export.write(f'<img src="{image_link}" alt="{alt}">\n')
                        continue
                elif markdown_list[j] != '\n':
                    current_line = "<p>" + markdown_list[j].rstrip('\n') + "</p>\n"

                    # START INLINES
                    current_line = styletag_change(current_line,'**','bold','<b>', '</b>','⒝')
                    current_line = styletag_change(current_line,'*','italics','<i>','</i>','⒤')
                    current_line = styletag_change(current_line,'__','underline','<u>','</u>','⒟')
                    current_line = styletag_change(current_line,'``','inline-codeblock','<code>','</code>','⒞')
                    current_line = styletag_change(current_line,'`','inline-codeblock','<code>','</code>','⒞')
                    current_line = styletag_change(current_line,'~~','strikethough','<s>','</s>','⒳')
                    current_line = styletag_change(current_line,'$$','mathmatical formula','<span class="math">','</span>','⒨')
                    current_line = styletag_change(current_line,'||','spoiler','<spoiler>','</spoiler>','⒣')

                    for k in range(0,99): # em dash
                        if '--' in markdown_list[j]:
                            current_line = current_line.replace('--', '—', 1)
                    
                    current_line = current_line.replace('⒝', '**').replace('⒤', '*').replace('⒟', '__').replace('⒞', '`').replace('⒳', '~~').replace('⒨', '$$').replace('⒣', '||') # replace ⒪ ⒝ ⒤ ⒟ ⒞ ⒳ ⒨ ⒣ with respective '***' '**' '*' '__' '`' '~~' '$$' '||'
                    html_export.write(current_line)
                continue
        
        else: 
            html_export.write(base_html_list[i])
    
    files_built += 1
    percent_complete = files_built / files_to_build * 100
    percent_complete = percent_complete.__round__(1)
    print(f'{success}{files_built}{addinfo}/{success}{files_to_build}{body} Built {addinfo}({percent_complete}%){body}')

print(f'{success} --PROCESS FINISHED!-- {body}')
exit()






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