import unittest

from blocknode import BlockType, block_to_block_type

class TestBlockToBlockType(unittest.TestCase):

    def test_paragraph(self):
        block = "This is a normal paragraph with some text."
        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)

    def test_heading(self):
        for i in range(1, 7):
            block = "#" * i + " Heading level " + str(i)
            self.assertEqual(block_to_block_type(block), BlockType.HEADING)

    def test_code_block(self):
        block = "```\nprint('Hello')\nx = 5\n```"
        self.assertEqual(block_to_block_type(block), BlockType.CODE)

    def test_code_block_with_language(self):
        block = "```python\nprint('Hello')\n```"
        self.assertEqual(block_to_block_type(block), BlockType.CODE)

    def test_quote_block(self):
        block = "> This is a quote\n> continuing the quote"
        self.assertEqual(block_to_block_type(block), BlockType.QUOTE)

    def test_unordered_list(self):
        block = "- item 1\n- item 2\n- item 3"
        self.assertEqual(block_to_block_type(block), BlockType.UNORDERED_LIST)

    def test_ordered_list(self):
        block = "1. first\n2. second\n3. third"
        self.assertEqual(block_to_block_type(block), BlockType.ORDERED_LIST)

    def test_ordered_list_non_incrementing(self):
        block = "1. first\n2. second\n4. fourth"
        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)

    def test_mixed_unordered_list(self):
        block = "- item 1\n- item 2\ntext not list"
        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)

    def test_mixed_quote(self):
        block = "> line 1\nnot a quote"
        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)

    def test_empty_block(self):
        block = ""
        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)

if __name__ == "__main__":
    unittest.main()
