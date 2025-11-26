import unittest

from extract_links_and_images import extract_markdown_images, extract_markdown_links

class TestExtraction(unittest.TestCase):
    def test_extract_markdown_images(self):
        matches = extract_markdown_images(
        "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
        )
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)

    def test_multiple_images(self):
        matches = extract_markdown_images(
            "Look ![one](url1) and ![two](url2) and ![three](url3)"
        )
        self.assertListEqual(
            [("one", "url1"), ("two", "url2"), ("three", "url3")],
            matches
        )

    def test_no_images(self):
        matches = extract_markdown_images("This text has no images at all.")
        self.assertListEqual([], matches)

    def test_image_with_spaces(self):
        matches = extract_markdown_images(
            "Here is ![ spaced alt ]( spaced_url ) in weird formatting"
        )
        self.assertListEqual(
            [(" spaced alt ", " spaced_url ")],
            matches
        )

    def test_image_with_parentheses_in_url(self):
        matches = extract_markdown_images(
            "Image: ![alt](https://example.com/image(1).png)"
        )
        self.assertListEqual(
            [],
            matches
        )
    # Testing Links
    def test_single_link(self):
        matches = extract_markdown_links(
            "Visit [Google](https://google.com) for info."
        )
        self.assertListEqual(
            [("Google", "https://google.com")],
            matches
        )

    def test_multiple_links(self):
        matches = extract_markdown_links(
            "Links: [one](url1) and [two](url2) and [three](url3)."
        )
        self.assertListEqual(
            [("one", "url1"), ("two", "url2"), ("three", "url3")],
            matches
        )

    def test_no_links(self):
        matches = extract_markdown_links("This has no links.")
        self.assertListEqual([], matches)

    def test_link_with_spaces(self):
        matches = extract_markdown_links(
            "Here is a [ spaced text ]( spaced_url ) example."
        )
        self.assertListEqual(
            [(" spaced text ", " spaced_url ")],
            matches
        )

    def test_nested_brackets_in_link_text(self):
        matches = extract_markdown_links(
            "Nested: [click [here]](https://example.com)"
        )
        # Regex won't handle nested perfectly, but it should match everything lazily
        self.assertListEqual(
            [],
            matches
        )

    def test_link_with_parentheses_in_url(self):
        matches = extract_markdown_links(
            "Look: [image](https://example.com/img(1).png)"
        )
        self.assertListEqual(
            [],
            matches
        )

    def test_ignores_images(self):
        matches = extract_markdown_links(
            "This is an image: ![alt](https://example.com/img.png)"
        )
        # Your regex *will match it*, since it doesn't check for '!'
        # If you want it to ignore images, update the regex with (?<!!)
        # I updated ...
        self.assertListEqual(
            [],
            matches
        )

    def test_broken_missing_paren(self):
        matches = extract_markdown_links(
            "Broken [google]https://google.com)"
        )
        self.assertListEqual([], matches)

    def test_broken_missing_bracket(self):
        matches = extract_markdown_links(
            "Broken google](https://google.com)"
        )
        self.assertListEqual([], matches)

    def test_link_at_start(self):
        matches = extract_markdown_links(
            "[start](url) is the first thing."
        )
        self.assertListEqual([("start", "url")], matches)

    def test_link_at_end(self):
        matches = extract_markdown_links(
            "Ends with a link [end](url)"
        )
        self.assertListEqual([("end", "url")], matches)

    # def test_adjacent_links(self):
    #  matches = extract_markdown_links(
    #       "Two links: "
    #   )
    #   self.assertListEqual([("a", "1"), ("b", "2")], matches)

if __name__ == "__main__":
    unittest.main()
