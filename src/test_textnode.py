import unittest

from textnode import TextNode, split_nodes_delimiter


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "bold")
        self.assertEqual(node, node2)

    def test_eq2(self):
        node = TextNode("This is a text node", "bold", None)
        node2 = TextNode("This is a text node", "bold", None)
        self.assertEqual(node, node2)


    def test_eq3(self):
        node = TextNode("This is a text node", "bold", "www.google.com")
        node2 = TextNode("This is a text node", "bold", "www.google.com")
        self.assertEqual(node, node2)

    def test_eq4(self):
        node = TextNode("This is a text node", "bold", "www.google.com")
        node2 = TextNode("This is a text node", "italic", "www.google.com")
        self.assertNotEqual(node, node2)

    def test_test_split_delimiter1(self):
        node = TextNode("This is a text block with a `code block` word", "text")
        correct = [
            TextNode("This is a text block with a ", "text"),
            TextNode("code block", "code"),
            TextNode(" word", "text")
        ]
        new_nodes = split_nodes_delimiter([node], '`', "code")
        self.assertEqual(new_nodes, correct)

if __name__ == "__main__":
    unittest.main()

