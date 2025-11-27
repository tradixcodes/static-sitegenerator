from textnode import TextNode, TextType
from extract_links_and_images import extract_markdown_images, extract_markdown_links

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []

    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue

        parts = node.text.split(delimiter)

        if len(parts) % 2 == 0:
            raise Exception(f"Invalid Markdown syntax: missing closing delimiter '{delimiter}'")

        for i,part in enumerate(parts):
            if part == "":
                continue

            if i % 2 == 0:
                new_nodes.append(TextNode(part, TextType.TEXT))
            else:
                new_nodes.append(TextNode(part, text_type))

    return new_nodes

def split_nodes_image(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue

        text = node.text
        images = extract_markdown_images(text)

        if not images:
            new_nodes.append(node)
            continue

        i = 0
        # Reconstructs markdown image to find it's position on the TextType.TEXT
        for alt, url in images:
            md = f"![{alt}]({url})"
            idx = text.find(md, i)

            # Adds text before the image
            chunk = text[i:idx]
            if chunk:
                new_nodes.append(TextNode(chunk, TextType.TEXT))

            # Add the image node
            new_nodes.append(TextNode(alt, TextType.IMAGE, url))
            i = idx + len(md)
        
        chunk = text[i:]
        if chunk:
            new_nodes.append(TextNode(chunk, TextType.TEXT))

    return new_nodes

def split_nodes_link(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue

        text = node.text
        links =  extract_markdown_links(text)

        if not links:
            new_nodes.append(node)
            continue

        i = 0
        for label, url in links:
            md = f"[{label}]({url})"
            idx = text.find(md, i)

            # Add text before the link
            chunk = text[i:idx]
            if chunk:
                new_nodes.append(TextNode(chunk, TextType.TEXT))

            new_nodes.append(TextNode(label, TextType.LINK, url))
            i = idx + len(md)

        # Add remaining final text
        chunk = text[i:]
        if chunk:
            new_nodes.append(TextNode(text[i:], TextType.TEXT))

    return new_nodes
