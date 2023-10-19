---
this-is-a-valid-fromtmatter-key: true;
this__is-a-valid_fromtmatter_key: true;
-this_is__a_valid_frontmatter---key: true;
---this-is-a-valid__frontmatter-key: false; # may not start with more than 2 hyphens.
+this_is-a-valid_frontmatter--key: false; # must only use alphanum (insenstaivee) with hyphens (-) and underscores (_).
2_this_is_a_valid_frontmatter_key: false; # must not start with a number
this_is_a_valid_frontmatter_key(): false; # again alphanum only

[category]
valid: true; # this.frontmatter["category"]["valid"]

[category.subcategory]
valid: true; # this.frontmatter["category"]["subcategory"]["valid"]

[category.subcategory.sub-subcategory]
valid: true; # this.frontmatter["category"]["subcategory"]["sub-subcategory"]["valid"]

[c2]
valid: true; # this.frontmatter["c2"]["valid"]

[2c2]
valid: false; # must not start with a nuber

[c2.2c]
valid: false; # must not start with a number

[@builder]
valid: false; # must only be alphanum
---

# Markdown Syntax Guide

That was a heading 1. The following is also a heading 1

===
Also a heading one
===

You should not have more than one heading one, so that should have given you a warning. This should do the same. The number of equals does not matter so long as they are both more than 3.

# Do not use more than 1 heading 1

You can also use other headings

## This is a heading 2

It is, isn't it?

This is also a heading 2
===

Once again, the number of equals does not matter so long as it is more than 3.

### This is a heading 3

It is!

This is also a heading 3
---

Once again, the number does not matter so long as it is more than three. This is where it gets tricky though becayse

---

that was a horisontal rule, not a heading 3. This is also a hr

+++

and so is this

***

headings continue up to 6, but only with hashes.

#### Heading 4

##### Heading 5

###### Heading 6

Those should have given you a lint (warning) because they had no content. You can also add IDs or classes to something with emmet-aligned syntax by using `[]{}`. For example [this text should have the class `.red`]{.red}. This only works when exporting to HTML.

This is a citation[^cite]. This is a footnote[^cite2]. If you click them it should take you to a bit at the end with it.

[cite]: this is the citations definition. It should appear at the bottom.
[cite2]: actually: theya re both footnotes!

This is ^superscript^, you follow? ^^this is subscript^^. _this is also subscript_, but you can change that in your config to be italics instead. __this is underlined__, but once again you can make this something else! **this is bold**. (this has no formatting). *this is italics*. \*this is not, because we escaped them\*. This last asterisk should appear as-is despite not being escaped since it has no partner *.

You can escape \[^cite] anything.

\## Even headings

> this is a blockquote

I wonder who said that???

> this is a blockquote
> - I did! [^quoter]

<!-- If a blockquote ends with a single hyphen, asterisk, or plus it will be formatted diffrently. -->

<!-- builder.py sucks! > -->

That was commented out, because its not true. This is also commented out %%commented%%.

> [!info] You can also create admontations.
> Thats cool!
>
> > [!question] But can you nest them?
> > Yes!!!!
>
> Thats so neat.

> [!tip]+ You can also make them collapseable.
> its true!

> [!tip] Or collapsed by default
> This is useful for Q+A things!

Unordered lists can be created with *, -, or +. 

- Ul irtem
- ul item 2
- ul item 3

You can also mix them

- ul item
* ul item 2
+ ul item 3

And they can be nested indefintely

- Wow!
- its cool!
+ and practical
	* because maybe you have sublistys
	+ I don't know why you would want to mix tokens though
		+ but it was easy to add!
		- so we kept it
	+ meow
	* what?
	- meow!
	- okay kitten
+ (she needed food)

Ordered lists are created with `1.`. You can have them count up or go in any order, so long as it starts with 1.

1. Meow
1. This is all 1!
1. It will automatically count up in the produced document
1. HTML + CSS really are magic!
1. (or in any other produced format, but this compiler just goes to HTML)
13. this is still vlaid though
1. even this
1923190. this is too
420. and the counting never gets scrwed up
69. not even once

They can of course be nested inside each other!

- wowie!
	1. What?
		- Wowie!
			1. Okay pixie
		+ she is a cat
		* and also this is a stress test
	2. meow

you cannot however mix orde5red and unordered lists

1. Meow
* this is invalid
1. because this cannot be both ordered and unordered.

This is a `<math>` block $$Epg = (1/2)(m)(h)$$. We also intend to support block math

$$$
With LaTeX!
(its not a prioirty tho, try implementing it yourself!)
$$$

You saw that `<math>`? That was a code block! We create  them with ``` backticks, single or doubble. ``meow``. Content inside code blocks is formatted exactly and other syntax cannot be used.

```
**meow**
<this is safe />
<main>
	because nothing is ever injected
</main>

Its all plain text!

\*even this!
```

You can also create fenced code blocks with three tildes instead of three backticks.

~~~
its a legacy markdown thing that is common enough to keep
~~~

But inline tildes mean ~~strikethrough~~. They are diffrent from -~del~- and ++ins++ though! You don't need to match the tildes to one side of del, ~-this~- is just as valid as -~this-~ is just as valid as ~-this-~. The importnat part is there is 1 tilde and 1 hyphen!

For code blocks you can specify a language

```python
it_adds_a_class = ".language-NAMEDBLOCK"
this_does_nothing_on_its_own = True
# but extensions can use it for syntax higlighting!
```

it is also common to be able to use the file extension only (but its still just `language-py` in this example, just something extensions should integrate!)

```py
def meow():
	print("Meow!")
```

And thats not even to mention [links](https://en.wikipedia.org)! You can also embed them ![and this is alt text](https://en.wikipedia.org/wiki/File:Flag_of_Canada_(Pantone).svg). Notice that file name had brackets: it should still work!

Depending on your prefrences, this will either produce:

```html
<figure>
	<img alt="and this is alt text" src="https://en.wikipedia.org/wiki/File:Flag_of_Canada_(Pantone).svg">
	<figcaption>
		and this is alt text
	</figcaption>
</figure>
```

Or just simply `<img alt="and this is alt text" src="https://en.wikipedia.org/wiki/File:Flag_of_Canada_(Pantone).svg">`. It will do that by default.

It should also adapt to the medias MIME type, and dynamically use `<video>` or `<audio>` instead. You can set figure prefrences on a per-mime basis.

If your slot is considered `safe` and has `allow-components` you can use <Components>. If not you should get an error and it will appear as raw text.

If your slot is considered `safe` and has `allow-html` you can embed <b>your own html</b>. Note that you can `allow-components` to inject html without being able to inject it yourself--this is a safety measure to prevent againt invalid HTML, sicne components tend to be more rigoursly checked.

[meow]: This footnote is not used anywhere, but should still work.

And this footnote[^non-existant] does not havea  definition, it should get the `.builder--no-definition` and `.builder--dead-link` classes added to it.