import unittest

from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_props_to_html(self):
        test_node = HTMLNode(
            "div",
            "Hello, world!",
            None,
            {"class": "greeting", "href": "https://boot.dev/"},
        )
        self.assertEqual(
            test_node.props_to_html(),
            ' class="greeting" href="https://boot.dev/"',
        )
    def test_none_props_to_html(self):
        test_node = HTMLNode(
            None,
            None,
            None,
            None,
        )
        self.assertEqual(
            test_node.props_to_html(),
            "",
        )
    
    def test_to_html_no_children(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_to_html_no_tag(self):
        node = LeafNode(None, "Hello, world!")
        self.assertEqual(node.to_html(), "Hello, world!")
    

if __name__ == "__main__":
    unittest.main()