from textnode import TextType, TextNode
from htmlnode import LeafNode
from text_to_textnode import text_to_textnodes

def text_to_children(text: str) -> list["LeafNode"]:
    nodes = text_to_textnodes(text)
    
    leaf_nodes = []
    for tn in nodes:
        if tn.text_type == TextType.TEXT:
            leaf_nodes.append(LeafNode(tag=None, value=tn.text))
        elif tn.text_type == TextType.BOLD:
            leaf_nodes.append(LeafNode(tag="b", value=tn.text))
        elif tn.text_type == TextType.ITALIC:
            leaf_nodes.append(LeafNode(tag="i", value=tn.text))
        elif tn.text_type == TextType.CODE:
            leaf_nodes.append(LeafNode(tag="code", value=tn.text))
        elif tn.text_type == TextType.LINK:
            leaf_nodes.append(LeafNode(tag="a", value=tn.text, props={"href": tn.url}))
        elif tn.text_type == TextType.IMAGE:
            leaf_nodes.append(LeafNode(tag="img", value="", props={"src": tn.url, "alt": tn.text}))
    return leaf_nodes
