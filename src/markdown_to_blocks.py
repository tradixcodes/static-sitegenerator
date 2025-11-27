def markdown_to_blocks(markdown):
    raw_blocks = markdown.split("\n\n")
    
    # for block in raw_blocks:
      #  print(f"This is a block: {block}")
    # print(f"This is raw_blocks: {raw_blocks}")

    blocks = [block.strip() for block in raw_blocks if block.strip()]

    return blocks

