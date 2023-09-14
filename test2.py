from html.parser import HTMLParser as HtmlParser

class MyHtmlParser(HtmlParser):
    preformatted_depth = 0
    depth = 0

    component_content = ""
    component = [] # Lists of components, in order. Last is most recent.

    def _is_component(self, name):
        if len(name) >= 1:
            return name[0].isupper()
        else:
            return False

    def handle_starttag(self, tag, attrs):
        self.depth += 1

        if tag == 'slot':
            # Manage inserting content
            print("WARNING: `slot` MUST be self closing, try `<slot />`")
            return
        if tag == 'pre':
            print(f"IsPre, depth = {self.preformatted_depth}")
            self.preformatted_depth += 1
        else:
            print("Encountered a start tag:", tag)

    def handle_endtag(self, tag):
        self.depth -= 1

        if tag == 'slot':
            return # Its handled when you open it, so nothing to do!
        if tag == 'pre':
            print(f"IsPre, depth = {self.preformatted_depth}")
            self.preformatted_depth -= 1
        else:
            print("Encountered a end tag:", tag)

    def handle_data(self, data):
        if self.preformatted_depth >= 1:
            return # Do not parse any contents
        elif self.preformatted_depth <= 0:
            # Print error cause we closing more than we openin' here
            return

        # girls if your data starts with "{"
        # And ends with "}"
        # THIS ONLY READS THE START/END THIS WAY! We NEED to be able
        # to find variables inside longer strings like {api.page.title} * mywebsite.tld
        if data.startswith("{") and data.endswith("}"):
            # Thats not your data
            # Thats a variable!
            pass

        print("Encountered some data  :", data)
    
    def handle_startendtag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        if tag == "slot":
            print("Found a slot <3")
        print(f"Found startend tag! {tag}")

# HTCL Process:
# - Get docuemnt to compile
# - When you handle a starttag, if it is capitalised we want to insert

components = {
    'Button': "<a class='button'>{text}</a>",
    'Navigation': "<nav><ul><li><a>Meow</a></li></ul></nav>",
}

parser = MyHtmlParser()

answer = parser.feed("""
<html>
    <head>
        <title>Test</title>
    </head>
    <body>
        <h1>Parse me!</h1>
        <p><slot /></p>
        <pre>
            <p>Meow<span> Purr</span></p>
            <pre>
                Test Case <p>UwU</p>
            </pre>
        </pre>
    </body>
</html>""")

print(answer)

# parser.feed('<html><head><title>Test</title></head>'
#             '<body><h1>Parse me!</h1><p><slot /></body></html>')