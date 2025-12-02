import re

from markdown_to_blocks import markdown_to_blocks
from blocknode import BlockType, block_to_block_type

def extract_title(markdown: str) -> str:
    # Extracts the markdown to blocks seperated by a double line \n\n
    blocks = markdown_to_blocks(markdown)
    # headings will most probably be at the beginning of the block list {but I won't specify
    # we'll use a for loop to check all the blocks and extract them. For now we'll stop at the first h1 tag}

    for block in blocks:
        # Not effective since it kinda is o(n): it depends on the number of blocks in the blocks list
        # But it catches H1 headings
        block_type = block_to_block_type(block)

        if block_type == BlockType.HEADING:
            # print(f"This is block(h1): {block}\n")
            match = re.match(r"(^#{1} (.+))", block)
            if match:
                level = len(match.group(1))
                text = match.group(2)
                title = text.strip()
                # print(f"This is h1: {match}\n")
                
                # This function only return the first match, and ignores the other ones, which kinda reduces it's time complexity
                # to something like 0(m) but worst case is an 0(n)
                # if we want all the h1 tag we have to store them in a list and return the list
                return title
            else:
                raise Exception ("Missing h1 tag")
