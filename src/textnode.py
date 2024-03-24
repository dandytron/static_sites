from htmlnode import LeafNode

class TextNode:
    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, other):
        if not isinstance(other, TextNode):
            raise TypeError("Second parameter is not of the TextNode type. Please provide another TextNode to compare.")
        return self.text == other.text and self.text_type == other.text_type and self.url == other.url

    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type}, {self.url})"

def text_node_to_html_node(text_node):
    match text_node.text_type:
        case None: raise Exception(f"Invalid text type: {text_node.text_type}")
        case "text": return LeafNode(None, text_node.text)
        case "bold": return LeafNode("b", text_node.text)
        case "italic": return LeafNode("i", text_node.text)
        case "code": return LeafNode("code", text_node.text)
        case "link": 
            if not text_node.url: 
                raise Exception("Link tags require a url.")
            else:
                return LeafNode("a", text_node.text, {"href": text_node.url})
        case "image": 
            if not text_node.url: 
                raise Exception("Image tags require a url.")
            else:
                return LeafNode("img", "", {"src": text_node.url, "alt": text_node.text})
