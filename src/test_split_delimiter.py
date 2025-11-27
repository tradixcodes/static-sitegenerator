import unittest

from split_nestedtexttypesfromtext_to_their_respective_types import split_nodes_delimiter, split_nodes_image, split_nodes_link
from textnode import TextNode, TextType

class TestSplitNodesDelimiter(unittest.TestCase):
    def test_code_split(self):
        node = TextNode("This is text with a `code block` word", TextType.TEXT)
        result = split_nodes_delimiter([node], "`", TextType.CODE)

        self.assertEqual(len(result), 3)
        self.assertEqual(result[0].text, "This is text with a ")
        self.assertEqual(result[0].text_type, TextType.TEXT)
        self.assertEqual(result[1].text, "code block")
        self.assertEqual(result[1].text_type, TextType.CODE)
        self.assertEqual(result[2].text, " word")
        self.assertEqual(result[2].text_type, TextType.TEXT)
    
    def test_bold_split(self):
        node = TextNode("This is **bold** text", TextType.TEXT)
        result = split_nodes_delimiter([node], "**", TextType.BOLD)

        self.assertEqual(len(result), 3)
        self.assertEqual(result[0].text, "This is ")
        self.assertEqual(result[1].text, "bold")
        self.assertEqual(result[1].text_type, TextType.BOLD)
        self.assertEqual(result[2].text, " text")

    def test_italic_split(self):
        node = TextNode("This is _italic_ text", TextType.TEXT)
        result = split_nodes_delimiter([node], "_", TextType.ITALIC)

        self.assertEqual(len(result), 3)
        self.assertEqual(result[1].text, "italic")
        self.assertEqual(result[1].text_type, TextType.ITALIC)

    def test_multiple_occurrences(self):
        node = TextNode("**bold1** text **bold2**", TextType.TEXT)
        result = split_nodes_delimiter([node], "**", TextType.BOLD)

        self.assertEqual(len(result), 3)
        self.assertEqual(result[0].text, "bold1")
        self.assertEqual(result[0].text_type, TextType.BOLD)
        self.assertEqual(result[2].text, "bold2")
        self.assertEqual(result[2].text_type, TextType.BOLD)

    def test_no_closing_delimiter(self):
        node = TextNode("This is a `broken code text", TextType.TEXT)
        with self.assertRaises(Exception) as context:
            split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertIn("Invalid Markdown syntax", str(context.exception))

    def test_non_text_nodes_are_unchanged(self):
        node = TextNode("hello", TextType.CODE)
        result = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertEqual(result, [node])  # should not split CODE node

# Testing split_nodes_image and split_nodes_link
class TestSplitNodes(unittest.TestCase):
    def test_split_single_link(self):
        node = TextNode(
            "Visit [Boot.dev](https://www.boot.dev) now!",
            TextType.TEXT
        )
        result = split_nodes_link([node])
        self.assertEqual(len(result), 3)
        self.assertEqual(result[0].text, "Visit ")
        self.assertEqual(result[0].text_type, TextType.TEXT)
        self.assertEqual(result[1].text, "Boot.dev")
        self.assertEqual(result[1].text_type, TextType.LINK)
        self.assertEqual(result[1].url, "https://www.boot.dev")
        self.assertEqual(result[2].text, " now!")
        self.assertEqual(result[2].text_type, TextType.TEXT)

    def test_split_multiple_links(self):
        node = TextNode(
            "Links: [Boot.dev](https://www.boot.dev) and [YouTube](https://youtube.com)",
            TextType.TEXT
        )
        result = split_nodes_link([node])
        # print(f"This is the node: {result}")
        self.assertEqual(len(result), 4)
        self.assertEqual(result[0].text, "Links: ")
        self.assertEqual(result[1].text, "Boot.dev")
        self.assertEqual(result[2].text, " and ")
        self.assertEqual(result[3].text, "YouTube")

    def test_split_link_at_start_and_end(self):
        node = TextNode(
            "[Start](https://start.com) middle [End](https://end.com)",
            TextType.TEXT
        )
        result = split_nodes_link([node])
        self.assertEqual(result[0].text, "Start")
        self.assertEqual(result[0].text_type, TextType.LINK)
        self.assertEqual(result[1].text, " middle ")
        self.assertEqual(result[1].text_type, TextType.TEXT)
        self.assertEqual(result[2].text, "End")
        self.assertEqual(result[2].text_type, TextType.LINK)

    def test_split_single_image(self):
        node = TextNode(
            "Here is an image ![Cat](cat.png) in text",
            TextType.TEXT
        )
        result = split_nodes_image([node])
        self.assertEqual(len(result), 3)
        self.assertEqual(result[0].text, "Here is an image ")
        self.assertEqual(result[1].text, "Cat")
        self.assertEqual(result[1].text_type, TextType.IMAGE)
        self.assertEqual(result[1].url, "cat.png")
        self.assertEqual(result[2].text, " in text")

    def test_split_multiple_images(self):
        node = TextNode(
            "![Cat](cat.png)![Dog](dog.png)",
            TextType.TEXT
        )
        result = split_nodes_image([node])
        self.assertEqual(len(result), 2)
        self.assertEqual(result[0].text, "Cat")
        self.assertEqual(result[0].text_type, TextType.IMAGE)
        self.assertEqual(result[1].text, "Dog")
        self.assertEqual(result[1].text_type, TextType.IMAGE)

    def test_no_links_or_images(self):
        node = TextNode(
            "Just plain text",
            TextType.TEXT
        )
        result_links = split_nodes_link([node])
        result_images = split_nodes_image([node])
        self.assertEqual(len(result_links), 1)
        self.assertEqual(result_links[0].text, "Just plain text")
        self.assertEqual(len(result_images), 1)
        self.assertEqual(result_images[0].text, "Just plain text")

    def test_non_text_nodes_ignored(self):
        node = TextNode(
            "Bold text",
            TextType.BOLD
        )
        result_links = split_nodes_link([node])
        result_images = split_nodes_image([node])
        self.assertEqual(len(result_links), 1)
        self.assertEqual(len(result_images), 1)
        self.assertEqual(result_links[0].text_type, TextType.BOLD)
        self.assertEqual(result_images[0].text_type, TextType.BOLD)

if __name__ == "__main__":
    unittest.main()
