import re

from markdown_to_blocks import markdown_to_blocks
from blocknode import BlockType, block_to_block_type
from htmlnode import ParentNode
from textnode import TextNode, TextType
from text_to_children import text_to_children

def markdown_to_html_node(markdown: str) -> "HTMLNode":
    """
    Convert a full markdown document into a single parent HTMLNode
    containing all child block-level HTMLNodes.
    """
    parent_node = ParentNode(tag="div", children=[])

    blocks = markdown_to_blocks(markdown)

    # 3️⃣ Loop over each block
    for block in blocks:
        block_type = block_to_block_type(block)

        # 4️⃣ Create block node based on type
        if block_type == BlockType.PARAGRAPH:
            children = text_to_children(block)
            node = ParentNode(tag="p", children=children)

        elif block_type == BlockType.HEADING:
            match = re.match(r"(#{1,6}) (.+)", block)
            if match:
                level = len(match.group(1))
                text = match.group(2)
                children = text_to_children(text)
                node = ParentNode(tag=f"h{level}", children=children)

        elif block_type == BlockType.CODE:
            # special case: do not parse inline
            lines = block.split("\n")
            code_text = "\n".join(lines[1:-1])  # remove ``` fences
            code_node = textnode_to_htmlnode(TextNode(code_text, TextType.TEXT))
            node = ParentNode(tag="pre", children=[code_node])

        elif block_type == BlockType.QUOTE:
            # remove leading '>' from each line
            text = "\n".join(line[1:].strip() for line in block.split("\n"))
            children = text_to_children(text)
            node = ParentNode(tag="blockquote", children=children)

        elif block_type == BlockType.UNORDERED_LIST:
            # each line starts with "- "
            items = [line[2:].strip() for line in block.split("\n")]
            li_nodes = [ParentNode(tag="li", children=text_to_children(item)) for item in items]
            node = ParentNode(tag="ul", children=li_nodes)

        elif block_type == BlockType.ORDERED_LIST:
            # each line starts with a number + ". "
            items = [re.sub(r"^\d+\. ", "", line).strip() for line in block.split("\n")]
            li_nodes = [ParentNode(tag="li", children=text_to_children(item)) for item in items]
            node = ParentNode(tag="ol", children=li_nodes)

        else:
            # fallback: treat as paragraph
            children = text_to_children(block)
            node = ParentNode(tag="p", children=children)

        # 5️⃣ Append block node to parent
        parent_node.children.append(node)

    # 6️⃣ Return the parent node
    return parent_node
