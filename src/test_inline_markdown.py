import unittest
from inline_markdown import (
    extract_markdown_images,
    extract_markdown_links,
    split_nodes_delimiter,
)

from textnode import (
    TextNode,
    text_type_text,
    text_type_bold,
    text_type_italic,
    text_type_code,
    text_type_image,
    text_type_link,
)

class TestInlineMarkdown(unittest.TestCase):
    def test_test_split_delimiter1(self):
        node = TextNode("This is a text block with a `code block` word", text_type_text)
        correct = [
            TextNode("This is a text block with a ", text_type_text),
            TextNode("code block", text_type_code),
            TextNode(" word", text_type_text)
        ]
        new_nodes = split_nodes_delimiter([node], '`', "code")
        self.assertEqual(new_nodes, correct)

    def test_test_split_delimiter2(self):
        node = TextNode("**This is a bold text block** with other words", text_type_text)
        correct = [
            TextNode("This is a bold text block", text_type_bold),
            TextNode(" with other words", text_type_text)
        ]
        new_nodes = split_nodes_delimiter([node], '**', text_type_bold)
        self.assertEqual(new_nodes, correct)

    def test_extract_markdown1(self):
        text = "This is text with an ![image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png) and ![another](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/dfsdkjfd.png)"
        image_parts_correct = [("image", "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png"), ("another", "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/dfsdkjfd.png")]
        self.assertEqual(extract_markdown_images(text), image_parts_correct)

    def test_extract_link(self):
        text = "This is text with a [link](https://www.example.com) and [another](https://www.example.com/another)"
        link_correct = [("link", "https://www.example.com"), ("another", "https://www.example.com/another")]
        self.assertEqual(extract_markdown_links(text), link_correct)

    
