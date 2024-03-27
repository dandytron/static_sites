from htmlnode import ParentNode
from textnode import text_node_to_html_node
from inline_markdown import text_to_text_nodes

import re

block_type_paragraph = "paragraph"
block_type_heading = "heading"
block_type_code = "code"
block_type_quote = "quote"
block_type_ul = "unordered list"
block_type_ol = "ordered list"


def markdown_to_blocks(markdown):
    blocks = []
    # split the text into blocks by /n newline characters
    split_markdown = markdown.split("\n\n")
    # if any block is an empty character, do not include it
    for piece in split_markdown:
        if piece == "":
            continue
            # strip leading and trailing whitespace from each split piece, add to blocks list
        piece = piece.strip()
        blocks.append(piece)
    return blocks

def block_to_block_type(block):
    # Headings start with 1-6 # characters, followed by a space and then the heading text.
    if re.match(r'^#{1,6} .', block):
        return block_type_heading
    # Some of the other conditions require checks line-by-line.
    lines = block.split('\n')
    # Code blocks must start with 3 backticks and end with 3 backticks.
    if len(lines) > 1 and lines[0].startswith('```') and lines[-1].endswith('```'):
        return block_type_code
    # Every line in a quote block must start with a > character.
    if block.startswith('>'):
        for line in lines:
            if not line.startswith('>'):
                return block_type_paragraph
        return block_type_quote
    # Every line in an unordered list block must start with a * or - character.
    if block.startswith('*'):
        for line in lines:
            if not line.startswith('*'):
                return block_type_paragraph
        return block_type_ul
    if block.startswith('-'):
        for line in lines:
            if not line.startswith('-'):
                return block_type_paragraph
        return block_type_ul
    # Every line in an ordered list block must start with a number followed by a . character. The number must start at 1 and increment by 1 for each line.
    if block.startswith('1. '):
        i = 1
        for line in lines:
            if not line.startswith(f'{i}. '):
                return block_type_paragraph
            i += 1
        return block_type_ol
    # If none of the above conditions are met, the block is a normal paragraph.
    return block_type_paragraph
    
def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    children = []
    for block in blocks:
        html_node = block_to_html_node(block)
        children.append(html_node)
    return ParentNode("div", children, None)

def block_to_html_node(block):
    block_type = block_to_block_type(block)
    if block_type == block_type_paragraph:
        return paragraph_to_html_node(block)
    if block_type == block_type_heading:
        return heading_to_html_node(block)
    if block_type == block_type_code:
        return code_to_html_node(block)
    if block_type == block_type_quote:
        return quote_to_html_node(block)
    if block_type == block_type_ul:
        return ul_to_html_node(block)
    if block_type == block_type_ol:
        return ol_to_html_node(block)
    raise ValueError("Not a valid block type.")

def text_to_children(text):
    text_nodes = text_to_text_nodes(text)
    children = []
    for text_node in text_nodes:
        html_node = text_node_to_html_node(text_node)
        children.append(html_node)
    return children

def paragraph_to_html_node(block):
    lines = block.split('\n')
    paragraph = " ".join(lines)
    children = text_to_children(paragraph)
    return ParentNode("p", children)

def heading_to_html_node(block):
    level = 0
    for char in block:
        if char == "#":
            level += 1
        else:
            break
    if level + 1 >= len(block):
        raise ValueError(f"Invalid heading level: {level}")
    text = block[level + 1:]
    children = text_to_children(text)
    return ParentNode(f"h{level}", children)

def code_to_html_node(block):
    if not block.startswith('```') or not block.endswith('```'):
        raise ValueError("Invalid code block")
    text = block[4:-3]
    children = text_to_children(text)
    code = ParentNode("code", children)
    return ParentNode("pre", [code])

def quote_to_html_node(block):
    lines = block.split('\n')
    new_lines = []
    for line in lines:
        if not line.startswith('>'):
            raise ValueError("Invalid quote block")
        new_lines.append(line.strip().lstrip('> '))
    text = ' '.join(new_lines)
    children = text_to_children(text)
    return ParentNode("blockquote", children)

def ul_to_html_node(block):
    items = block.split('\n')
    html_items = []
    for item in items:
        text = item[2:]
        children = text_to_children(text)
        html_items.append(ParentNode("li", children))
    return ParentNode("ul", html_items)

def ol_to_html_node(block):
    items = block.split('\n')
    html_items = []
    # Only difference between this and above is that we need to slice off the first 3 chars: a number, a period and a whitespace.
    for item in items:
        number_match = re.match(r'^([0-9]+)\. ', item)
        if not number_match == None:
            number = number_match.group(0)
            text = item[len(number):]
            children = text_to_children(text)
            html_items.append(ParentNode("li", children))
    return ParentNode("ol", html_items)