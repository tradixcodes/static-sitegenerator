import unittest

from text_to_textnode import text_to_textnodes
from textnode import TextNode, TextType

class TestTextToTextNode(unittest.TestCase):
    def test_plain_text(self):
        text = "Just plain text"
        nodes = text_to_textnodes(text)
        self.assertEqual(len(nodes), 1)
        self.assertEqual(nodes[0].text, text)
        self.assertEqual(nodes[0].text_type, TextType.TEXT)

    def test_bold_text(self):
        text = "This is **bold** text"
        nodes = text_to_textnodes(text)
        self.assertEqual(len(nodes), 3)
        self.assertEqual(nodes[1].text, "bold")
        self.assertEqual(nodes[1].text_type, TextType.BOLD)

    def test_italic_text(self):
        text = "This is _italic_ text"
        nodes = text_to_textnodes(text)
        self.assertEqual(len(nodes), 3)
        self.assertEqual(nodes[1].text, "italic")
        self.assertEqual(nodes[1].text_type, TextType.ITALIC)

    def test_code_text(self):
        text = "Some `code` here"
        nodes = text_to_textnodes(text)
        self.assertEqual(len(nodes), 3)
        self.assertEqual(nodes[1].text, "code")
        self.assertEqual(nodes[1].text_type, TextType.CODE)

    def test_image_text(self):
        text = "Image ![Cat](cat.png) here"
        nodes = text_to_textnodes(text)
        self.assertEqual(len(nodes), 3)
        self.assertEqual(nodes[1].text, "Cat")
        self.assertEqual(nodes[1].text_type, TextType.IMAGE)
        self.assertEqual(nodes[1].url, "cat.png")

    def test_link_text(self):
        text = "Go to [Boot.dev](https://boot.dev)"
        nodes = text_to_textnodes(text)
        self.assertEqual(len(nodes), 2)
        self.assertEqual(nodes[1].text, "Boot.dev")
        self.assertEqual(nodes[1].text_type, TextType.LINK)
        self.assertEqual(nodes[1].url, "https://boot.dev")

    def test_combined_markdown(self):
        text = "This is **bold** and _italic_ and `code` and ![Cat](cat.png) and [Link](https://boot.dev)"
        nodes = text_to_textnodes(text)
        expected_types = [
            TextType.TEXT, TextType.BOLD, TextType.TEXT, TextType.ITALIC,
            TextType.TEXT, TextType.CODE, TextType.TEXT, TextType.IMAGE,
            TextType.TEXT, TextType.LINK
        ]
        self.assertEqual([n.text_type for n in nodes], expected_types)

    def test_adjacent_markdown(self):
        text = "**bold**_italic_`code`![Image](img.png)[Link](url)"
        nodes = text_to_textnodes(text)
        # Should produce exactly 5 nodes, no empty TextNode
        self.assertEqual(len(nodes), 5)
        self.assertEqual(nodes[0].text_type, TextType.BOLD)
        self.assertEqual(nodes[1].text_type, TextType.ITALIC)
        self.assertEqual(nodes[2].text_type, TextType.CODE)
        self.assertEqual(nodes[3].text_type, TextType.IMAGE)
        self.assertEqual(nodes[4].text_type, TextType.LINK)

    def test_empty_text_ignored(self):
        text = "**bold****bold2**"
        nodes = text_to_textnodes(text)
        # Should only contain the two bold nodes, no empty text nodes
        self.assertEqual(len(nodes), 2)
        self.assertEqual(nodes[0].text, "bold")
        self.assertEqual(nodes[1].text, "bold2")

if __name__ == "__main__":
    unittest.main()
