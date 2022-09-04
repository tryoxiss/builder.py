__version__ = 'v0.0.0.1'

# open buildlist and reformat
markdown_names_list = open('__templates/build_list.txt', 'r').readlines()
for i in range(len(markdown_names_list)):
    markdown_names_list[i] = markdown_names_list[i].rstrip('\n')

# open html template
base_html_list = open('__templates/base.html', 'r').readlines()

# colours for console
percent = '\033[90m'
addinfo = '\033[90m'
warning = '\033[93m'
build_error = '\033[91m'
success = '\033[92m' 
fatal = '\033[91m' 
impinfo = '\033[97m'
body = '\033[0m'

# variables for console output
files_to_delete = len(markdown_names_list)
files_to_build = len(markdown_names_list)
files_built = 0
percent_complete = 0


def styletag_warning(style_type): # style tag warning for the console, this is a function to allow for easy reuse while making warnings
    print(f'{warning}WARNING:{body} file {impinfo}{markdown_names_list[n]}{body} on line {impinfo}{j}{body} there is only an opening set of {style_type}, it will show up as itself instead of turning into the appropriate style tags.')

def header_check(md_tag, header_level): # checking different header levels to create <h#><\h#>
    current = ((markdown_list[j].lstrip(f'{md_tag} ')).rstrip('\n')).split(' {') # 'title', 'id}'
    if len(current) >= 2:
        html_export.write(f'<h{header_level} id="' + current[1].rstrip('}') + '">' + current[0] + f'</h{header_level}>\n')
    else: 
        print(f'{warning}WARNING:{body} file {impinfo}{markdown_names_list[n]}{body} on line {impinfo}{j} does not have a header ID.')
        html_export.write(f'<h{header_level}>' + current[0] + f'</h{header_level}>\n')

def styletag_change(current_line, md_tag, style_type, html_tag, html_closing_tag, error_byte): # changes a md style tag to html
    current_count = 0
    current_line = current_line.replace(f'\{md_tag}', f'⒭')
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
    current_line = current_line.replace(f'⒭', f'\{md_tag}')
    return current_line

def find_replace(current_line, md_tag, text_tag): # finds and replaces specified characters (as long as they are not before a \)
    current_line = current_line.replace(f'\{md_tag}', '⒭')
    for k in range(0,40): 
        if f'{md_tag}' in current_line:
            current_line = current_line.replace(f'{md_tag}', f'{text_tag}')
    current_line = current_line.replace('⒭', f'{md_tag}')
    return current_line


# This block asks the user if they want to start the builder giving information of what it will do
print(f'{addinfo}INFO: {body} builder.py will DELETE and then REBUILD ALL files.')
print(f'{fatal}{files_to_delete}{body} will be {fatal}DELETED{body}')
print(f'{success}{files_to_build}{body} will be {success}BUILT{body}')
changes_ok = input(f'Are these changes OK ({success}Y{body}/{fatal}n{body}): ')

# if the player allows the operation to start, this will not be aborted, reminder: ONLY CAPITAL Y will work to help prevent "auto-pilot"
if 'Y' in changes_ok: 
    print(f'{success}Process Started!{body}')
else:
    print(f'{fatal}Process Ending...{body}')
    exit(1) # 1 = aborted

# starts opening files (need a system to auto detect md files)
for n in range(len(markdown_names_list)):

    # import current markdown file and create new html file
    markdown = open(f'{markdown_names_list[n]}', "r")    # sets the file you wanted to be edited into the variable "markdown" and sets it to be read-only (so we dont break it)
    markdown_list = markdown.readlines()
    markdown_names_list[n] = markdown_names_list[n].rstrip('.md').lstrip('_mystuff/')
    html_export = open(f'mystuff/{markdown_names_list[n]}.html', "w")
    language_current = ''

    # starts going through the template file line by line to replace the feilds in question
    for i in range(len(base_html_list)):

        # replaces {title} with the proper title, as well as looking for the background image to place it in as well
        if '{title}' in base_html_list[i]:
            html_export.write(base_html_list[i].replace('{title}', markdown_names_list[n].replace('-', ' '))) # remove - and replace with ' '
        elif '{background_image_url}' in base_html_list[i]:
            for j in range(0, len(markdown_list)):
                if 'background_image: ' in markdown_list[j]:
                    html_export.write(base_html_list[i].replace('{background_image_url}', (markdown_list[j].lstrip('background_image: ')).rstrip(") \n")))
                    break

        # replaces {h1} with the first md header for the proper title of the html file, also adds the text after the colon if applicable
        if '{h1}' in base_html_list[i]:
            for j in range(0, len(markdown_list)):
                if '# ' in markdown_list[j]:
                    if ':' in markdown_list[j]:
                        html_export.write((base_html_list[i].replace('{h1}',(markdown_list[j].lstrip("# ")).split(': ',1)[0])).replace('{aft_colon}',': ' + (markdown_list[j].split(': ',1)[1].rstrip('\n'))))
                        break
                    else:
                        html_export.write((base_html_list[i].replace('{h1}',((markdown_list[j].lstrip("# ")).rstrip('\n')))).replace('<span>{aft_colon}</span>',''))
                        break

        # WIP (language support for codeblocks)
        if '{language}' in base_html_list[i]:
            for j in range(0, len(markdown_list)):
                if 'language: ' in markdown_list[j]:
                    language_current = (markdown_list[j].lstrip('language: ')).rstrip('\n')
            for j in range(0, len(markdown_list)):
                if 'line-numbers: true' in markdown_list[j]:
                    html_export.write((base_html_list[i].replace('{language}', language_current)).replace('{line-numbers}', 'line-numbers'))

        # replaces {content} with the content specified after the front matter in the md document
        if '{content}' in base_html_list[i]:
            
            # finds the end of the front matter
            temp_count = 0
            for j in range(len(markdown_list)):
                if '---' in markdown_list[j]:
                    temp_count += 1
                    continue
                if temp_count == 2:
                    start_pos = j
                    break

            # these variables are used throughout the script and cannot be set to 0 as they are a constant in the exchange to html and warnings
            header_one_count = 0
            temp_count = 0
            # starts converting lines from md to html in document **this is the main part that edits the script**
            for j in range(start_pos, len(markdown_list)):
                
                # if the line is empty then skip it
                if markdown_list[j].startswith('\n'): continue
                
                # if the line has a comment then skip it
                if '<!--' and '-->' in markdown_list[j]: continue # we continue as we do not want to print anything that has a comment

                # if the line has ``` start a code block, when it finds another after cycling through multiple lines and printing them raw it exits the codeblock
                elif temp_count > 0:
                    if '```' in markdown_list[j+1]: # handy trick to find out if the next line is the end of a codeblock to remove the \n at the end
                        html_export.write(markdown_list[j].rstrip('\n'))
                    elif '```' in markdown_list[j]:
                        html_export.write('</code></pre>\n')
                        temp_count = 0
                        continue
                    else: 
                        html_export.write(markdown_list[j])
                        continue
                elif '```' in markdown_list[j]: # codeblock
                    temp_count += 1
                    html_export.write('<pre><code class="language-' + (markdown_list[j].lstrip('``` ')).rstrip(' \n') + '">')
                
                # handles headers for the current line, if above 6 it signals a warning
                elif '####### ' in markdown_list[j]: print(f'{warning}WARNING: {body}The document {impinfo}' + markdown_names_list[n].rstrip('\n') + f'{body} on line {impinfo}' + str(j) + f'{body} has a heading larger than 6, it will not be included.')
                elif '###### ' in markdown_list[j]: header_check('######', 6)
                elif '##### ' in markdown_list[j]: header_check('#####', 5)
                elif '#### ' in markdown_list[j]: header_check('####', 4)
                elif '### ' in markdown_list[j]: header_check('###', 3)
                elif '## ' in markdown_list[j]: header_check('##', 2)
                
                # a document should only ever have 1 header one. more can cause significant problems and as such a warning is placed
                elif '# ' in markdown_list[j] and '\# ' not in markdown_list[j]: # header 1
                    header_one_count += 1
                    if header_one_count >= 2:
                        print(f'{warning}WARNING: {body}The document {impinfo}' + markdown_names_list[n].rstrip('\n') + f'{body} on line {impinfo}' + str(j) + f'{body} has more than one heading 1, the seccond one will not be included')
                
                # if a line starts with '> ' then create it as a blockquote and do not do any formating
                elif markdown_list[j].startswith('> '): html_export.write("<blockquote>" + (markdown_list[j].lstrip('> ')).rstrip(' \n') + "</blockquote>\n")
                
                # if a line starts with '---' then create it as a blockquote and do not do any formating
                elif markdown_list[j].startswith('---'): html_export.write("<hr>\n") # horisontal rule

                # if a line has an image requested, use the <img> tag to write the image source
                elif '![' in markdown_list[j] and '\![' not in markdown_list[j]: # image
                        split_image = markdown_list[j].split(']')
                        image_link = (split_image[1].lstrip('(')).rstrip(') \n')
                        alt = split_image[0].lstrip("![")
                        html_export.write(f'<img src="{image_link}" alt="{alt}">\n')
                
                # start the inlines and prepare the current_line if no block-level elements are started
                elif markdown_list[j] != '\n':
                    # prepare the line for inline editing
                    current_line = "<p>" + markdown_list[j].rstrip('\n') + "</p>\n"
                    
                    # inline styletag changes
                    current_line = styletag_change(current_line,'**','bold','<b>', '</b>','⒝')
                    current_line = styletag_change(current_line,'*','italics','<i>','</i>','⒤')
                    current_line = styletag_change(current_line,'__','underline','<u>','</u>','⒟')
                    current_line = styletag_change(current_line,'``','inline-codeblock','<code>','</code>','⒞')
                    current_line = styletag_change(current_line,'`','inline-codeblock','<code>','</code>','⒞')
                    current_line = styletag_change(current_line,'~~','strikethough','<s>','</s>','⒳')
                    current_line = styletag_change(current_line,'$$','mathmatical formula','<span class="math">','</span>','⒨')
                    current_line = styletag_change(current_line,'||','spoiler','<spoiler>','</spoiler>','⒣')

                    # inline replacements
                    current_line = find_replace(current_line, '--', '—')
                    current_line = find_replace(current_line, '\\', '')

                    # replacing control bytes with proper md tag
                    current_line = current_line.replace('⒝', '**').replace('⒤', '*').replace('⒟', '__').replace('⒞', '`').replace('⒳', '~~').replace('⒨', '$$').replace('⒣', '||') # replace ⒪ ⒝ ⒤ ⒟ ⒞ ⒳ ⒨ ⒣ with respective '***' '**' '*' '__' '`' '~~' '$$' '||'
                    html_export.write(current_line)
        else: 
            html_export.write(base_html_list[i])
    
    # print successful builds and percentage complete to console to allow player to confirm it is running
    files_built += 1
    percent_complete = (files_built / files_to_build * 100).__round__(1)
    print(f'{success}{files_built}{addinfo}/{success}{files_to_build}{body} Built {addinfo}({percent_complete}%){body}')

# print the success and exit with a code of 0 (success)
print(f'{success} --PROCESS FINISHED!-- {body}')
exit(0) # 0 = success
