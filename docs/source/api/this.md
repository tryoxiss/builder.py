# This (API Namespace)

`this` is an API namespace variable that contains data about the current document.

- `language`
- `cannonical_url`
- `created_datetime()`
- `modified_datetime()`
- 

## Meta

Meta is a subclass which contains variables assigned in your config.py file.

## Frontmatter

Frontmatter is a variable which contains a dictionary of keys found in the documents frontmatter.

Example:

```py
api.this.frontmatter["author"]
```