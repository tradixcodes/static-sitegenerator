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
        tn = TextNode(TextType.BOLD, "Bold Text")
        node = text_node_to_html_node(tn)
        self.assertEqual(node.tag, "b")
        self.assertEqual(node.value, "Bold Text")


    def test_italic_type(self):
        tn = TextNode(TextType.ITALIC, "Italic Text")
        node = text_node_to_html_node(tn)
        self.assertEqual(node.tag, "i")

    def test_code_type(self):
        tn = TextNode(TextType.CODE, "print('hi')")
        node = text_node_to_html_node(tn)
        self.assertEqual(node.tag, "code")

    def test_link_type(self):
        tn = TextNode(TextType.LINK, "Google", url="https://google.com")
        node = text_node_to_html_node(tn)
        self.assertEqual(node.tag, "a")
        self.assertEqual(node.props, {"href": "https://google.com"})


    def test_image_type(self):
        tn = TextNode(TextType.IMAGE, "", url="image.png", alt="Alt Text")
        node = text_node_to_html_node(tn)
        self.assertEqual(node.tag, "img")
        self.assertEqual(node.value, "")
        self.assertEqual(node.props, {"src": "image.png", "alt": "Alt Text"})


    def test_unsupported_type(self):
        tn = TextNode(999, "Oops")
        with self.assertRaises(ValueError):
            text_node_to_html_node(tn)


if __name__ == "__main__":
    unittest.main()

