import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode


class TestHTMLNode(unittest.TestCase):
    def test_props1(self):
        node = HTMLNode('a', 'link', [], {"href": "https://www.google.com", "target": "_blank"})
        correct = ' href="https://www.google.com" target="_blank"'
        self.assertEqual(node.props_to_html(), correct)

    def test_to_html(self):
        node = HTMLNode()
        self.assertRaises(NotImplementedError, node.to_html)

class TestLeafNode(unittest.TestCase):
    def test_html1(self):
        node = LeafNode("p", "This is a paragraph of text")
        html = "<p>This is a paragraph of text</p>"
        self.assertEqual(node.to_html(), html)

    def test_html2(self):
        node = LeafNode("a", "Click Me!", {"href": "https://www.google.com"})
        html = '<a href="https://www.google.com">Click Me!</a>'
        self.assertEqual(node.to_html(), html)
        
    def test_html3(self):
        node = LeafNode("a", None)
        self.assertRaises(ValueError, node.to_html)

class TestParentNode(unittest.TestCase):
    def test_html1(self):
        node = ParentNode("p", [LeafNode("b", "Bold Text"), LeafNode(None, "Normal Text"),],)
        html = "<p><b>Bold Text</b>Normal Text</p>"
        self.assertEqual(node.to_html(), html)

    def test_html2(self):
        pn = ParentNode("p", [LeafNode("b", "Bold Text"), LeafNode(None, "Normal Text"),],)
        node = ParentNode("div", [pn])
        html = "<div><p><b>Bold Text</b>Normal Text</p></div>"
        self.assertEqual(node.to_html(), html)

