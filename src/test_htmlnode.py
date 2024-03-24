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
    

if __name__ == "__main__":
    unittest.main()