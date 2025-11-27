import unittest

from markdown_to_html import markdown_to_html_node
from htmlnode import HTMLNode

class TestMarkdownToHtmlNode(unittest.TestCase):
    
    def test_paragraphs_and_headings(self):
        md = """
# Heading 1

This is **bold** text and _italic_ text.

## Heading 2

Another paragraph with a [link](https://example.com)
"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        expected_html = (
            "<div><h1>Heading 1</h1><p>This is <b>bold</b> text and <i>italic</i> text.</p><h2>Heading 2</h2><p>Another paragraph with a <a href=\"https://example.com\">link</a></p></div>"
        )
        self.assertEqual(html, expected_html)
    
    def test_unordered_and_ordered_lists(self):
        md = """
- first item
- second item

1. ordered one
2. ordered two
"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        expected_html = (
            "<div><ul><li>first item</li><li>second item</li></ul><ol><li>ordered one</li><li>ordered two</li></ol></div>"
        )
        self.assertEqual(html, expected_html)
    
    def test_quotes_and_inline(self):
        md = """
> This is a quote
> Second line

Normal paragraph with `inline code` and **bold**.
"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        expected_html = (
            "<div><blockquote>This is a quote\nSecond line</blockquote><p>Normal paragraph with <code>inline code</code> and <b>bold</b>.</p></div>"
        )
        self.assertEqual(html, expected_html)
    
    def test_images_and_links(self):
        md = """
This is a paragraph with an ![image](img.png) and a [link](https://example.com)
"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        expected_html = (
            "<div><p>This is a paragraph with an <img src=\"img.png\" alt=\"image\"></img> and a <a href=\"https://example.com\">link</a></p></div>"
        )
        self.assertEqual(html, expected_html)

    def test_code_blocks(self):
        md = """
```
x = 5
print(x)
```

Some paragraph after code.
"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        expected_html = (
            "<div><pre><code>x = 5\nprint(x)</code></pre><p>Some paragraph after code.</p></div>"
        )
        self.assertEqual(html, expected_html)

if __name__ == "__main__":
    unittest.main()
