import unittest

from textnode import TextNode, TextType
from htmlnode import LeafNode
from textnode_to_htmlnode import text_node_to_html_node

class TestTextNodeToHTMLNode(unittest.TestCase):
    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertIsInstance(html_node, LeafNode)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")

    def test_bold_type(self):
        tn = TextNode("Bold Text", TextType.BOLD)
        node = text_node_to_html_node(tn)
        self.assertEqual(node.tag, "b")
        self.assertEqual(node.value, "Bold Text")

    def test_italic_type(self):
        tn = TextNode("Italic Text", TextType.ITALIC)
        node = text_node_to_html_node(tn)
        self.assertEqual(node.tag, "i")

    def test_code_type(self):
        tn = TextNode("print('hi')", TextType.CODE)
        node = text_node_to_html_node(tn)
        self.assertEqual(node.tag, "code")

    def test_link_type(self):
        tn = TextNode("Google", TextType.LINK, url="https://google.com")
        node = text_node_to_html_node(tn)
        self.assertEqual(node.tag, "a")
        self.assertEqual(node.props, {"href": "https://google.com"})

    def test_image_type(self):
        tn = TextNode("Alt Text", TextType.IMAGE, url="/image.png")
        node = text_node_to_html_node(tn)
        self.assertEqual(node.tag, "img")
        self.assertEqual(node.value, "")
        self.assertEqual(node.props, {"src": "/image.png", "alt": "Alt Text"})
    
    def test_link_type_with_basepath(self):
        tn = TextNode("Google", TextType.LINK, url="/index.html")
        node = text_node_to_html_node(tn, basepath="/static-site/")
        self.assertEqual(node.tag, "a")
        self.assertEqual(node.props, {"href": "/static-site/index.html"})

    def test_image_type_with_basepath(self):
        tn = TextNode("Alt Text", TextType.IMAGE, url="/image.png")
        node = text_node_to_html_node(tn, basepath="/static-site/")
        self.assertEqual(node.tag, "img")
        self.assertEqual(node.value, "")
        self.assertEqual(node.props, {"src": "/static-site/image.png", "alt": "Alt Text"})


    def test_unsupported_type(self):
        tn = TextNode(999, "Oops")
        with self.assertRaises(ValueError):
            text_node_to_html_node(tn)


if __name__ == "__main__":
    unittest.main()

