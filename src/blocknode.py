from enum import Enum
import re

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"


def block_to_block_type(block: str) -> BlockType:
    raw_lines = block.split("\n")

    while raw_lines and raw_lines[0].strip() == "":
        raw_lines.pop(0)
    while raw_lines and raw_lines[-1].strip() == "":
        raw_lines.pop(-1)

    if not raw_lines:
        return BlockType.PARAGRAPH

    lines = raw_lines

    if len(lines) == 1 and re.match(r"^#{1,6} ", lines[0]):
        return BlockType.HEADING

    if lines[0].lstrip().startswith("```") and lines[-1].rstrip().endswith("```"):
        return BlockType.CODE

    if all(line.startswith(">") for line in lines):
        return BlockType.QUOTE

    if all(line.startswith("- ") for line in lines):
        return BlockType.UNORDERED_LIST

    ordered = True
    for i, line in enumerate(lines, start=1):
        if not re.match(rf"^{i}\. ", line):
            ordered = False
            break
    if ordered:
        return BlockType.ORDERED_LIST

    return BlockType.PARAGRAPH
