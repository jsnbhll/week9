# Jason Bhalla
# I pledge my honor that I have abided by the Stevens Honor System.

from html.parser import HTMLParser
from urllib.parse import urlparse

class LinkParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.links = []

    def handle_starttag(self, tag, attributes):
        if tag == "a":
            for name, value in attributes:
                if name == "href" and value:
                    address = urlparse(value)
                    if address.scheme in ("http", "https") and address.netloc:
                        self.links.append(value)


filename = input("Enter the HTML file name: ")

try:
    with open(filename, "r", encoding="utf-8") as file:
        parser = LinkParser()
        parser.feed(file.read())

    parser.links.sort(key=lambda link: urlparse(link).netloc.lower())

    if not parser.links:
        print("No web links found.")
    else:
        for link in parser.links:
            print(link)

except OSError:
    print("Could not open the HTML file:", filename)
