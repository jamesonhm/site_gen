import unittest

from markdown_blocks import (
    block_to_block_type,
    code_to_html,
    heading_to_html, 
    markdown_to_blocks,
    block_type_heading,
    block_type_code,
    block_type_quote,
    block_type_ulist,
    block_type_olist,
    block_type_paragraph,
    markdown_to_html_nodes,
    olist_to_html,
    quote_to_html,
    ulist_to_html
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

    def test_heading_to_html(self):
        md = "### Heading"
        correct = "<h3>Heading</h3>"
        self.assertEqual(heading_to_html(md).to_html(), correct)

    def test_code_to_html(self):
        md = "```\ncode = True\n```"
        correct = "<pre><code>code = True</code></pre>"
        self.assertEqual(code_to_html(md).to_html(), correct)

    def test_quote_to_html(self):
        md = ">This is a lame quote\n>the second line"
        correct = "<blockquote>This is a lame quote the second line</blockquote>"
        self.assertEqual(quote_to_html(md).to_html(), correct)

    def test_ulist_to_html(self):
        md = "* list item\n* second item"
        correct = "<ul><li>list item</li><li>second item</li></ul>"
        self.assertEqual(ulist_to_html(md).to_html(), correct)

    def test_olist_to_html(self):
        md = "1. list item\n2. second item"
        correct = "<ol><li>list item</li><li>second item</li></ol>"
        self.assertEqual(olist_to_html(md).to_html(), correct)

    def test_markdown_to_html_nodes1(self):
        md = "# Heading1\n\nparagraph text with **bold**"
        correct = "<div><h1>Heading1</h1><p>paragraph text with <b>bold</b></p></div>"
        self.assertEqual(markdown_to_html_nodes(md).to_html(), correct)

    def test_markdown_to_html_nodes(self):
        self.maxDiff = None
        md = "# Heading1\n\nparagraph text with **bold**\n\n- ulist item 1\n- ulist item \n\n```\ncode_block = True var = 1\n```\n\n>quote text\n>with multiple lines."
        correct = "<div><h1>Heading1</h1><p>paragraph text with <b>bold</b></p><ul><li>ulist item 1</li><li>ulist item</li></ul><pre><code>code_block = True var = 1</code></pre><blockquote>quote text with multiple lines.</blockquote></div>"
        self.assertEqual(markdown_to_html_nodes(md).to_html(), correct)
