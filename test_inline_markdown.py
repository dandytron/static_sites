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
        new_nodes = split_nodes_delimiter([node], "?", text_type_bold)
        self.assertListEqual([
            TextNode("This", text_type_text),
            TextNode("test", text_type_bold),
            TextNode("text", text_type_text),
            TextNode("has", text_type_bold),
            TextNode("bolded words.", text_type_text),
        ],
        new_nodes,
        )
        with self.assertRaises(ValueError)
