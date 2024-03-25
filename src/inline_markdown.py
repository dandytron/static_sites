import re

from textnode import (
    TextNode,
    text_type_text,
    text_type_bold,
    text_type_italic,
    text_type_code,
    text_type_link,
    text_type_image,
)

def text_to_textnodes(text):
    nodes = TextNode(text, text_type_text)
    nodes = split_nodes_delimiter(nodes, "**", text_type_bold)
    nodes = split_nodes_delimiter(nodes, "*", text_type_italic)
    nodes = split_nodes_delimiter(nodes, "`", text_type_code)
    nodes = split_node_images(nodes)
    nodes = split_node_links(nodes)
    return nodes

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes =  []
    
    for old_node in old_nodes:
        if old_node.text_type != text_type_text:
            new_nodes.append(old_node)
            continue
        split_nodes = []
        sections = old_node.text.split(delimiter)
        if len(sections) % 2 != 0:
            raise ValueError("The string is missing at least one closing delimiter")
        for i in range(0, len(sections)):
            if sections[i] == "":
                continue
            if i % 2 == 0:
                split_nodes.append(TextNode(sections[i], text_type_text))
            else:
                split_nodes.append(TextNode(sections[i], text_type))
        new_nodes.extend(split_nodes)

    return new_nodes
    
def split_node_images(old_nodes):
    new_nodes = []
    for old_node in old_nodes:
        # skip this iteration if the old node is not noted as text (if it's an image or link already, say)
        if old_node.text_type != text_type_text:
            new_nodes.append(old_node)
            continue
        # This will get slowly 'chopped' down as we extract images.
        original_text = old_node.text
        images = extract_markdown_images(old_node.text)
        if len(images) == 0:
            new_nodes.append(old_node)
            continue
        for image in images:
            # The first 'section', so long as it's not empty, will be added to the new_nodes list as no other images were found in it.
            sections = original_text.split(f"![{image[0]}]({image[1]})", 1)
            if len(sections) != 2:
                raise ValueError("Markdown is invalid, image notation is not closed")
            if sections[0] != "":
                new_nodes.append(TextNode(sections[0], text_type_text))
            new_nodes.append(
                TextNode(
                    image[0],
                    text_type_image,
                    image[1],
                )
            )
            # Add the rest of the node to the original_text to slice up with the next image, if one exists.
            original_text = sections[1]
        if original_text != "":
            new_nodes.append(TextNode(original_text, text_type_text))
    return new_nodes

# The following function operates much line the image extraction function above.
def split_node_links(old_nodes):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != text_type_text:
            new_nodes.append(old_node)
            continue
        original_text = old_node.text
        links = extract_markdown_links(old_node.text)
        if len(links) == 0:
            new_nodes.append(old_node)
            continue
        for link in links:
            # The first 'section', so long as it's not empty, will be added to the new_nodes list as no other links were found in it.
            sections = original_text.split(f"[{link[0]}]({link[1]})", 1)
            if len(sections) != 2:
                raise ValueError("Markdown is invalid, image notation is not closed")
            if sections[0] != "":
                new_nodes.append(TextNode(sections[0], text_type_text))
            new_nodes.append(
                TextNode(
                    link[0],
                    text_type_link,
                    link[1],
                )
            )
            # Add the rest of the node to the original_text to slice up with the next image, if one exists.
            original_text = sections[1]
        if original_text != "":
            new_nodes.append(TextNode(original_text, text_type_text))
    return new_nodes  
            

def extract_markdown_images(text):
    matches = re.findall(r"!\[(.*?)\]\((.*?)\)", text)
    return matches

def extract_markdown_links(text):
    matches = re.findall(r"\[(.*?)\]\((.*?)\)", text)
    return matches