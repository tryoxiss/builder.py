# builder.py
An extensible static site generation package with good extension support. 

## Quick Start Guide

1. **Add a folder that starts with an `_`** (just `_` works too!) contents will be put into that folder but with the `_` stripped, so `_/blog` will be put into `/blog/`. `_` goes to the root directory and they all preserve file structure!
2. **Add `builder.py` and `builder.config` to your root directory** (you can just copy the defult, it will work in most cases) 
3. **Run builder.py** (`python builder.py` using a terminal) 

**Thats it!** You can now do with them what you want, commit them to your web server, use them for whatever you want! Builder.py supports a wide range of markdown, and if its missing something you can just modify the code or add an extension for it!

## Suported Markdown 

`*italics*`  
`**bold**`  
`__underlined__`  
`[links](url "label")`'  
`# Headers` (Number of hashtags specifies trhe level, `# ` is h1, `## ` is h2, etc. The space IS NEEDED, otherwise its a tag)   
`--` emdash (`—`)  

### Work in Progress Markdown
`[id links][id]` (make sire you add `[id]: url "label"` somewhere in your document!)  
`[[wikilinks]]`  
`[abbrs]("Abbriviations")` -- WARNING: The label is NOT VISBLE to screen readers  
`^superscript`  
`^^subscript`  
`#tags` or indexing  
`[HTML Obfuscated emails](mailto:email@example.co,)`   

### With Extensions... 
`:emojis: and :unicode: character auto replacement!`  
