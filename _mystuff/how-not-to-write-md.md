---
background_image: https://techstacker.com/how-to-escape-html.html
date: 22-23-2023
creator: creator creator creator
tittle: How NOT to write markdown
line-numbers: true
---

# How NOT to write markdown 
Markdown is a commonly used markup language because it is *****simple__ and __ **easy** to* use. ***. But there are a """few""" errors people make regularly and here they are. 

# Using H1s in more than one place
asside from being semantically god awlful, they can break other systems too!!

#### Jumping down more than one heading level
###### Using lower headers as subtittles
####### and trying to use h7 and beyond

are all BIIIIIG mistakes that *SHOULD **ALWAYS*** be avoided. 

## Code Block Mistakes

you can specify a language for `code blocks` in the frontmatter (if the compiler your using suppots it) which can be used by some libraries to syntax hilight inline code blocks and save you with multiline code blocks!! But this document FROGOT TO DO THAT so this won't have any syntax hilighting :(

```
To be clear: you should still ALWAYS specify a language on multi-line code blocks, it's just a nice fallback if you froget. 
You also shouldn't put plain text in code blocks, so we should leave this *now* 
```

another common mistake is to include line numbers in the code block: IF YOU WANT THAT: USE A LIBRARY!!!

```python
1    def like_this(): 
2       print("you shouldn't do this")
3       print("it's bad for screen readers AND your sanity")
```

and putting code outside of code blocks is equally bad: it makes it hard and annoying to read. 

## NO ID Headers
The next one is--if your on the web at least--frogetting to add an ID to your heders. Most headers here don't have it. you can add one like so: 

```md
## Heading two for stuff {heading-2}
```

in the above example, the heading would get an ID for #heading-2 which can be used to direct link! Just put it in `{}`!

Frogetting to make it a .md files

## Headers with **BOLD** __UNDERLINED__ OR -- (emdash)