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
    
    def test_split_images(self):
        node = TextNode(
            "Here is some text with an ![image](https://i.imgur.com/zjjcJKZ.png)",
            text_type_text,
        )
        new_nodes = split_node_images([node])
        self.assertListEqual(
            [
                TextNode("Here is some text with an ", text_type_text),
                TextNode("image", text_type_image, "https://i.imgur.com/zjjcJKZ.png"),
            ],
            new_nodes
        )
    
    def test_split_one_image(self):
        node = TextNode(
            "![image](https://imgur.com/gallery/vkuRns6)",
            text_type_text,
        )
        new_nodes = split_node_images([node])
        self.assertListEqual(
            [
                TextNode("image", text_type_image, "https://imgur.com/gallery/vkuRns6"),
            ],
            new_nodes,
        )
    
    def test_split_many_images(self):
        node = TextNode(
            "This text has this ![image](https://imgur.com/gallery/vkuRns6) and also this ![image](https://imgur.com/t/aww/TVXCWAx) and also this one ![image](https://imgur.com/t/aww/ALyEQ13) too.",
            text_type_text,
        )
        new_nodes = split_node_images([node])
        self.assertListEqual(
            [
                TextNode("This text has this ", text_type_text),
                TextNode("image", text_type_image, "https://imgur.com/gallery/vkuRns6"),
                TextNode("and also this ", text_type_text),
                TextNode("image", text_type_image, "https://imgur.com/t/aww/TVXCWAx"),
                TextNode("and also this one ", text_type_text),
                TextNode("image", text_type_image, "https://imgur.com/t/aww/ALyEQ13"),
                TextNode("too ", text_type_text),
            ],
            new_nodes,
        )

    def test_split_one_link(self):
        node = TextNode(
            "This is a [link](https://imgur.com/gallery/vkuRns6)",
            text_type_text,
        )
        new_nodes = split_node_links([node])
        self.assertListEqual(
            [
                TextNode("This is a ", text_type_text),             
                TextNode("link", text_type_link, "https://imgur.com/gallery/vkuRns6"),
            ],
            new_nodes,
        )

    def test_text_to_textnodes(self):
        node = TextNode(
            "This is **text** with an *italic* word and a `code block` and an ![image](https://i.imgur.com/zjjcJKZ.png) and a [link](https://boot.dev)",
            text_type_text,
        )
        new_nodes = text_to_textnodes([node])
        self.assertListEqual(
            [
                TextNode("This is ", text_type_text),
                TextNode("text", text_type_bold),
                TextNode(" with an ", text_type_text),
                TextNode("italic", text_type_italic),
                TextNode(" word and a ", text_type_text),
                TextNode("code block", text_type_code),
                TextNode(" and an ", text_type_text),
                TextNode("image", text_type_image, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and a ", text_type_text),
                TextNode("link", text_type_link, "https://boot.dev"),
            ],
            new_nodes,
        )


if __name__ == "__main__":
    unittest.main()