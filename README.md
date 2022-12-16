# builder.py
An extensible static site generation package for the real world. 

> [!warning]
> This project is INACTIVE. We had a few design goals going in: 
> 1. Simple, easy, no dependancy hell. 
> 2. Easy for programmers and non programmers alike, we had both tried upwards of 5 static site generators and they were all verycomplicated or had thier own annoying quirks. We wanted a strightforward quirk-free site generator
> 
> We have since left the project. We left not because we didn't like it--we did like it, but we found other projects that met our needs. [makesite.py](https://github.com/sunainapai/makesite) shares a lot of our design goals and excutes on them beautifully, we suggest if this project interested you that you use that instead.
> We cannot vouch fully for its quality, but it has served us so far in our (admittedly limited) testing, and we fork if needed. In the meantime we are working on more interesting projects, notibly treeview.js, where we have learned from our mistakes and made sure it didnt exist before we started it. 

## Quick Start Guide

1. **Add a folder that starts with an `_`** (just `_` works too!) contents will be put into that folder but with the `_` stripped, so `_/blog` will be put into `/blog/`. `_` goes to the root directory and they all preserve file structure! (This works well if you make the build to folder for these the subdomain, and thats how it will likely be interpreted. 
2. **Add `builder.py` and `builder.config` to your root directory** (you can just copy the defult, it will work in most cases) 
3. **Run builder.py** (`python builder.py` using a terminal) 

**Thats it!** You can now do with them what you want, commit them to your web server, use them for whatever you want! Builder.py supports a wide range of markdown, and if its missing something you can just modify the code or add an extension for it!

## Suported Markdown 

- `*italics*`  
- `**bold**`  
- `__underlined__`  
- `[links](url "label")`'  
- `# Headers` (Number of hashtags specifies trhe level, `# ` is h1, `## ` is h2, etc. The space IS NEEDED, otherwise its a tag)   
- `--` emdash (`—`)  
- `> ` blockquotes

### Work in Progress Markdown
- `[id links][id]` (make sire you add `[id]: url "label"` somewhere in your document!)  
- `[[Pipeable Wikilinks|wikilinks]]` -- Takes the content inside of it and links to that! You can use a pipe (`|` character to specify otherwise (`this content will be displayed|and-it-will-link-here`). You can use absolute (`[[/path/to/file]]`) relative from base (`[[thing]]`) For example if you are on example.com/blog/post-1 and there is a wikilink to `[[post-2]]` you will go to example.com/blog/post-2, but if it was `[[/post-2]]` you would go to example.com/post-2!
- `[abbrs]("Abbriviations")` -- WARNING: The label is NOT VISBLE to screen readers  
- `^superscript`  
- `^^subscript`  
- `#tags` or indexing  
- `[HTML Obfuscated emails](mailto:email@example.co,)`   
- `![image label](url)`
- `![id images][id]`

```
> [!callouts] 
> are not currently
> supported :(
```

```
- nested
  - unordered
  - lists 
- are a 
  - work 
    - in 
      - progress
```

```
1. nested
  1. ordered
  2. lists 
2. are 
  1. a
  2. work 
  3. in 
    1. progress
```

### With Extensions... 
- `:emojis: and :unicode: character auto replacement!`  
