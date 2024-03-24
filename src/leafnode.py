from htmlnode import HTMLNode

class LeafNode(HTMLNode):
    def __init__(self, value, tag=None, props=None):
        super().__init__(tag, value, props)
    
    def to_html(self):
        if self.value == "":
            raise ValueError("No value set. All leaf nodes require a value.")
        if self.tag == None:
            return f"{self.value}"
        elif self.tag == "a":
            return f'<a href="{self.props["href"]}">{self.value}</a>'
        else:
            return f'<{self.tag}>{self.value}</{self.tag}>'
