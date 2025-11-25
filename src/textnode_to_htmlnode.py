from textnode import TextNode, TextType
from htmlnode import LeafNode

def text_node_to_html_node(text_node):
    t = text_node.text_type

    if t == TextType.TEXT:
        return LeafNode(None, text_node.text)
    elif t == TextType.BOLD:
        return LeafNode("b", text_node.text)
    elif t == TextType.ITALIC:
        return LeafNode("i", text_node.text)
    elif t == TextType.CODE:
        return LeafNode("code", text_node.text)
    elif t == TextType.LINK:
        return LeafNode("a", text_node.text, props={"href": text_node.url})
    elif t == TextType.IMAGE:
        return LeafNode("img", "", props={"src": text_node.url, "alt": text_node.text})
    else:
        raise ValueError(f"Unsupported TextType: {t}")
