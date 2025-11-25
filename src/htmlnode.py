class HTMLNode():
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError("to_html must be implemented by subclass")

    def props_to_html(self):
        if not self.props:
            return ""
        return "".join([f" {key}=\"{value}\"" for key, value in self.props.items()])

    def __repr__(self):
        return(
            f"HTMLNode(tag={self.tag}, value={self.value}, children={self.children}, props={self.props})"
        )

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        if value is None:
            raise ValueError("LeafNode requires a non-None value")

        super().__init__(tag=tag, value=value, children=None, props=props)

    def to_html(self):
        if self.tag is None:
            return self.value
        return f"<{self.tag}{self.props_to_html()}>" + self.value + f"</{self.tag}>"

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        if tag is None:
            raise ValueError("ParentNode requires a tag")
        if children is None:
            raise ValueError("ParentNode requires a child value")

        super().__init__(tag=tag, value=None, children=children, props=props)

    def to_html(self):
        if self.tag is None:
            raise ValueError("Node must have a tag to render HTML")
        if self.children is None:
            raise ValueError("Node must have children to render HTML")
        children_html = ''.join([child.to_html() for child in self.children])
        return f"<{self.tag}{self.props_to_html()}>" + children_html + f"</{self.tag}>"


