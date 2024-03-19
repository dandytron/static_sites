class TextNode:
    def __init__(self, text, texttype, url=None):
        self.text = text
        self.texttype = texttype
        self.url = url

    def __eq__(self, other):
        if not isinstance(other, TextNode):
            raise TypeError("Second parameter is not of the TextNode type. Please provide another TextNode to compare.")
        return self.text == other.text and self.texttype == other.texttype and self.url == other.url

    def __repr__(self):
        return f"TextNode({self.text}, {self.texttype}, {self.url})"
