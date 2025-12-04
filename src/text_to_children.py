from textnode import TextType, TextNode
from htmlnode import LeafNode
from text_to_textnode import text_to_textnodes
from textnode_to_htmlnode import text_node_to_html_node

def text_to_children(text: str, basepath="/") -> list["LeafNode"]:
    nodes = text_to_textnodes(text)
    
    leaf_nodes = []
    for tn in nodes:
        leaf_node = text_node_to_html_node(tn, basepath=basepath)
        leaf_nodes.append(leaf_node)
    return leaf_nodes
