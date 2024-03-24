class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None, data_custom=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
        self.data_custom = data_custom
    
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