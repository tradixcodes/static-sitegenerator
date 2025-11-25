import unittest

from htmlnode import LeafNode

class TestLeafNode(unittest.TestCase):
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_html_a_with_props(self):
        node = LeafNode("a", "Google", props={"href": "https://google.com"})
        self.assertEqual(node.to_html(), '<a href="https://google.com">Google</a>')

    def test_leaf_to_html_span(self):
        node = LeafNode("span", "Some text")
        self.assertEqual(node.to_html(), "<span>Some text</span>")

    def test_leaf_to_html_no_tag(self):
        node = LeafNode(None, "Just text")
        self.assertEqual(node.to_html(), "Just text")


if __name__ == "__main__":
    unittest.main()
