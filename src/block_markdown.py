from text_node import TextNode

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
    split_markdown = markdown.split("\n")
    # if any block is an empty character, do not include it
    for piece in split_markdown:
        if piece == "":
            continue
        else:
            # strip leading and trailing whitespace from each split piece, add to blocks list
            piece = piece.strip()
            blocks.append(piece)
    return blocks

def block_to_block_type(block):
    # Headings start with 1-6 # characters, followed by a space and then the heading text.
    if re.match(r'^\*{1,6} .', block):
        return block_type_heading
    # Some of the other conditions require checks line-by-line.
    lines = block.split('\n')
    # Code blocks must start with 3 backticks and end with 3 backticks.
    if len(lines) > 1 and lines[0].startswith('```') and lines[-1].endsswith('```'):
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
    
    