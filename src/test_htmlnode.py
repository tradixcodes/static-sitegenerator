import unittest

from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_props_to_html_empty(self):
        node = HTMLNode(tag="p", value="Hello", props=None)
        self.assertEqual(node.props_to_html(), "")

    def test_props_to_html_single(self):
        node = HTMLNode(tag="a", value="Google", props={"href": "https://www.google.com"})
        self.assertEqual(node.props_to_html(), ' href="https://www.google.com"')
    
    def test_props_to_html_multiple(self):
        props = {
            "href": "https://google.com",
            "target": "_blank"
        }
        node = HTMLNode(tag="a", value="Google", props=props)
        self.assertEqual(node.props_to_html(), ' href="https://google.com" target="_blank"')

if __name__ == "__main__":
    unittest.main()
