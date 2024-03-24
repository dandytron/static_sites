from htmlnode import HTMLNode

class LeafNode(HTMLNode):
    def __init__(self, value, tag=None, props=None):
        super().__init__(tag=tag, props=props)
    
    def to_html(self):
        if self.value == "":
            raise ValueError("No value set. All leaf nodes require a value.")
        if self.tag == None:
            return f"{self.value}"
        else:
            leaf_attributes = []
            for key, value in self.props.items():
                leaf_attributes.append(f'{key}="{value}"')
            leaf_tags = ""
            if leaf_attributes:
                leaf_tags = ' ' + ' '.join(leaf_attributes)
            return f'<{self.tag}{leaf_tags}>{self.value}</{self.tag}'