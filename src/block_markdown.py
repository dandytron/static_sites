from text_node import TextNode

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