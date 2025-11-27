import re

from markdown_to_blocks import markdown_to_blocks
from blocknode import BlockType, block_to_block_type
from htmlnode import ParentNode, LeafNode
from textnode import TextNode, TextType
from text_to_children import text_to_children
from textnode_to_htmlnode import text_node_to_html_node

def markdown_to_html_node(markdown: str) -> "HTMLNode":
    """
    Convert a full markdown document into a single parent HTMLNode
    containing all child block-level HTMLNodes.
    """
    parent_node = ParentNode(tag="div", children=[])

    blocks = markdown_to_blocks(markdown)
    # print(f"This is blocks: {blocks}\n")

    # 3️⃣ Loop over each block
    for block in blocks:
        block_type = block_to_block_type(block)
        # print(f"This is block: {block} and block_type: {block_type}")
        # print("\n")

        # 4️⃣ Create block node based on type
        if block_type == BlockType.PARAGRAPH:
            children = text_to_children(block)
            # print(f"These are the children: {children}\n")
            node = ParentNode(tag="p", children=children)
            # print(f"This is the node: {node}\n")

        elif block_type == BlockType.HEADING:
            match = re.match(r"(#{1,6}) (.+)", block)
            if match:
                level = len(match.group(1))
                text = match.group(2)
                children = text_to_children(text)
                # print(f"These are the children: {children}\n")
                node = ParentNode(tag=f"h{level}", children=children)
                # print(f"This is the node: {node}\n")

        elif block_type == BlockType.CODE:
            # special case: do not parse inline
            lines = block.split("\n")
            # print(f"\nThis is lines: {lines}\n")
            code_text = "\n".join(lines[1:-1])
            # print(f"This is code_text: {code_text}\n")# remove ``` fences
            code_node = LeafNode(tag="code", value=code_text)
            # print(f"This is code_node: {code_node}\n")
            node = ParentNode(tag="pre", children=[code_node])
            # print(f"This is node: {node}\n")
            # print(f"This is the node: {node}\n")

        elif block_type == BlockType.QUOTE:
            # remove leading '>' from each line
            text = "\n".join(line[1:].strip() for line in block.split("\n"))
            children = text_to_children(text)
            node = ParentNode(tag="blockquote", children=children)
            # print(f"This is the node: {node}\n")

        elif block_type == BlockType.UNORDERED_LIST:
            # each line starts with "- "
            items = [line[2:].strip() for line in block.split("\n")]
            li_nodes = [ParentNode(tag="li", children=text_to_children(item)) for item in items]
            node = ParentNode(tag="ul", children=li_nodes)
            # print(f"This is the node: {node}\n")

        elif block_type == BlockType.ORDERED_LIST:
            # each line starts with a number + ". "
            items = [re.sub(r"^\d+\. ", "", line).strip() for line in block.split("\n")]
            li_nodes = [ParentNode(tag="li", children=text_to_children(item)) for item in items]
            node = ParentNode(tag="ol", children=li_nodes)
            # print(f"This is the node: {node}\n")

        else:
            # fallback: treat as paragraph
            children = text_to_children(block)
            node = ParentNode(tag="p", children=children)
            # print(f"This is the node: {node}\n")

        # 5️⃣ Append block node to parent
        parent_node.children.append(node)

    # print(f"\nThis is parent node: {parent_node.to_html()}\n")
    # 6️⃣ Return the parent node
    return parent_node
