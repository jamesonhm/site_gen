import unittest

from markdown_blocks import (
    block_to_block_type, 
    markdown_to_blocks,
    block_type_heading,
    block_type_code,
    block_type_quote,
    block_type_ulist,
    block_type_olist,
    block_type_paragraph
)


class TestMarkdownBlocks(unittest.TestCase):
    def test_markdown_to_blocks(self):
        markdown = """
            This is **bolded** paragraph

            This is another paragraph with *italic* text and `code` here
            This is the same paragraph on a new line

            * This is a list
            * with items
        """
        correct_blocks = ["This is **bolded** paragraph", "This is another paragraph with *italic* text and `code` here\nThis is the same paragraph on a new line", "* This is a list\n* with items"]
        self.assertEqual(markdown_to_blocks(markdown), correct_blocks)

    def test_block_to_block_type(self):
        md = "### Heading"
        self.assertEqual(block_to_block_type(md), block_type_heading)

    def test_block_to_block_type_code(self):
        md = "```\ncode = True\n```"
        self.assertEqual(block_to_block_type(md), block_type_code)

    def test_block_to_block_type_quote(self):
        md = ">This is a lame quote"
        self.assertEqual(block_to_block_type(md), block_type_quote)

    def test_block_to_block_type_ulist(self):
        md = "* list item"
        self.assertEqual(block_to_block_type(md), block_type_ulist)

    def test_block_to_block_type_olist(self):
        md = "1. olist item"
        self.assertEqual(block_to_block_type(md), block_type_olist)

    def test_block_to_block_type_para(self):
        md = "paragraph item"
        self.assertEqual(block_to_block_type(md), block_type_paragraph)
