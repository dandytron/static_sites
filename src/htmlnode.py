class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
    
    def to_html(self):
        raise NotImplementedError("to_html method not implemented")

    def props_to_html(self):
        if self.props is None:
            return ""
        prop_string = ""
        for prop in self.props:
            prop_string = prop_string + f' {prop}="{self.props[prop]}"'
        return prop_string
    
    def __repr__(self):
        return f"HTMLNode({self.tag}),\nValue: {self.value}\nChildren: {self.children},\n{self.props}"

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)
    
    def to_html(self):
        if self.value == None:
            raise ValueError("Invalid HTML. A value is required.")
        if self.tag == None:
            return self.value
        return f'<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>'
    
    def __repr__(self):
        return f"LeafNode({self.tag}, {self.value}, {self.props})"

class ParentNode(HTMLNode):
    def __init__(self, tag, children=None, props=None):  # Allow `children` to be None by default
        super().__init__(tag, None, children, props)

    def to_html(self):
        if self.tag is None:
            raise ValueError("Invalid HTML. A tag is required for this node")
        children_html = ""
        if self.children is not None:  # Check if `self.children` is not None
            for child in self.children:
                children_html += child.to_html()
        return f"<{self.tag}{self.props_to_html()}>{children_html}</{self.tag}>"
    
    def __repr__(self):
        return f"ParentNode({self.tag}), children: {self.children}, {self.props}"