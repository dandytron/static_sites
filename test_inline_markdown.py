import unittest
from inline_markdown import(
    split_nodes_delimiter
)

from text_node import (
    TextNode,
    text_type_text,
    text_type_bold,
    text_type_italic,
    text_type_code,
)

class TestInlineMarkdown(unittest.TestCase):
    def test_bold(self):
        node = TextNode("This test text has a bolded **word**.", text_type_text)
        new_nodes = split_nodes_delimiter([node], "**", text_type_bold)
        self.assertListEqual([
            TextNode("This test text has a bolded", text_type_text),
            TextNode("word", text_type_bold),
            TextNode(".", text_type_text),
        ],
        new_nodes,
        )
    
    def test_double_bold(self):
        node = TextNode("This **test text** has bolded words.", text_type_text)
        new_nodes = split_nodes_delimiter([node], "**", text_type_bold)
        self.assertListEqual([
            TextNode("This", text_type_text),
            TextNode("test text", text_type_bold),
            TextNode("has bolded words.", text_type_text),
        ],
        new_nodes,
        )

    def test_over_one_word_bold(self):
        node = TextNode("This **test** text **has** bolded words.", text_type_text)
        new_nodes = split_nodes_delimiter([node], "**", text_type_bold)
        self.assertListEqual([
            TextNode("This", text_type_text),
            TextNode("test", text_type_bold),
            TextNode("text", text_type_text),
            TextNode("has", text_type_bold),
            TextNode("bolded words.", text_type_text),
        ],
        new_nodes,
        )

    def test_invalid_delimiter(self):
        node = TextNode("This **test** text **has** bolded words.", text_type_text)
        with self.assertRaises(ValueError):
            split_nodes_delimiter([node], "?", text_type_bold)

    def test_extract_markdown_images(self):
        matches = extract_markdown_images(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
        )
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)

    def test_extract_markdown_links(self):
        matches = extract_markdown_links(
            "[This](https://www.rockpapershotgun.com/) is text with a link and so is [this](https://www.rockpapershotgun.com/dragons-dogma-2-review)"
        )
        self.assertListEqual(
            [
                ("This", "https://www.rockpapershotgun.com/"),
                ("this", "https://www.rockpapershotgun.com/dragons-dogma-2-review"),
            ],
            matches,
        )

if __name__ == "__main__":
    unittest.main()