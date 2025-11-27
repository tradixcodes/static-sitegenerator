import re

def markdown_to_blocks(markdown):
    raw_blocks = re.split(r"\n\s*\n", markdown)
    
    # print(f"This is raw_blocks: {raw_blocks}")
    #for block in raw_blocks:
    #    print(f"This is a block: {block}")

    blocks = [block.strip() for block in raw_blocks if block.strip()]

    return blocks

