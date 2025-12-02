import os
from markdown_to_html import markdown_to_html_node
from extract_title import extract_title
from htmlnode import ParentNode, LeafNode

def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")

    # -- Read markdown --
    with open(from_path, "r", encoding="utf-8") as f:
        markdown_content = f.read()

    # -- Read template --
    with open(template_path, "r", encoding="utf-8") as f:
        template_content = f.read()

    # -- Convert markdown -> HTML ---
    html_node = markdown_to_html_node(markdown_content)
    html_content = html_node.to_html()

    # -- Extract title ---
    title = extract_title(markdown_content)

    # -- Replace placeholders in template ---
    full_html = (
        template_content
        .replace("{{ Title }}", title)
        .replace("{{ Content }}", html_content)
    )
    
    # --- Ensure directory exists ---
    dest_dir = os.path.dirname(dest_path)
    if dest_dir:
        os.makedirs(dest_dir, exist_ok=True)

    # --- Write final HTML to destination ---
    with open(dest_path, "w", encoding="utf-8") as f:
        f.write(full_html)
