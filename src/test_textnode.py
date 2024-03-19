import unittest

from textnode import TextNode


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "bold")
        self.assertEqual(node, node2)
    def test_uneq(self):
        node = TextNode("This is one text node", "bold")
        node2 = TextNode("But this is a second text node", "italic")
        self.assertNotEqual(node, node2)
    def test_none_url(self):
        node = TextNode("This node has no url", "bold", url=None)
        node2 = TextNode("This node has no url", "bold", url=None)
        self.assertEqual(node, node2)
    def test_diff_types(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "italic")
        self.assertNotEqual(node, node2)
    def test_missing_url(self):
        node = TextNode("This is a text node", "bold", url="https://www.google.com/")
        node2 = TextNode("This is a text node", "bold")
        self.assertNotEqual(node, node2)
    def test_textype_none(self):
        node = TextNode("This is a text node", None)
        node2 = TextNode("This is a text node", None)
        self.assertEqual(node, node2)

if __name__ == "__main__":
    unittest.main()