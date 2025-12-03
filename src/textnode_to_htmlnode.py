from textnode import TextNode, TextType
from htmlnode import LeafNode

def text_node_to_html_node(text_node, basepath="/"):
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
        href = text_node.url
        if href.startswith("/"):
            href = basepath + href[1:] # prepend basepath
        return LeafNode("a", text_node.text, props={"href": href})
    elif t == TextType.IMAGE:
        src = text_node.url
        if src.startswith("/"):
            src = basepath + src[1:] # prepend basepath
        return LeafNode("img", "", props={"src": src, "alt": text_node.text})
    else:
        raise ValueError(f"Unsupported TextType: {t}")
