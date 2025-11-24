import unittest

from textnode import TextNode, TextType

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_empty_url(self):
        node = TextNode("This is a url node", TextType.LINK, "https://www.tradix.dev")
        node2 = TextNode("This is a url node", TextType.LINK)
        self.assertNotEqual(node, node2)

    def test_not_equal_different_text_type(self):
        """Test inequality when text_type is different"""
        node1 = TextNode("Same text", TextType.BOLD)
        node2 = TextNode("Same text", TextType.ITALIC)
        self.assertNotEqual(node1, node2)

    def test_not_equal_different_url(self):
        """Test inequality when url is different"""
        node1 = TextNode("Click here", TextType.LINK, url="https://a.com")
        node2 = TextNode("Click here", TextType.LINK, url="https://b.com")
        self.assertNotEqual(node1, node2)

if __name__ == "__main__":
    unittest.main()
