import unittest

from markdown_to_html import markdown_to_html_node
from htmlnode import HTMLNode

class TestMarkdownToHtmlNode(unittest.TestCase):
"""
Used to test the larger test_markdown_to_html.py
"""
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
            """<div><pre><code>x = 5
print(x)</code></pre><p>Some paragraph after code.</p></div>"""
        )
        self.assertEqual(html, expected_html)

if __name__ == "__main__":
    unittest.main()
