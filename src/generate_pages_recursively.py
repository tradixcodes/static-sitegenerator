import os
from pathlib import Path
from generate_page import generate_page

def generate_pages_recursive(dir_path_content: Path, template_path: Path, dest_dir_path: Path):
    """
    Recursively generates HTML pages from all markdown files in `dir_path_content`.
    Each markdown file is converted using `template_path` and written to `dest_dir_path`,
    preserving the folder structure.
    """
    for root, dirs, files in os.walk(dir_path_content):
        root_path = Path(root)
        for file in files:
            if file.endswith(".md"):
                md_path = root_path / file

                # Determine relative path from content folder
                relative_path = md_path.relative_to(dir_path_content)
                
                # Change extension to .html
                html_relative_path = relative_path.with_suffix(".html")

                # Destination path in public/
                dest_path = dest_dir_path / html_relative_path

                # Generate page
                generate_page(
                    from_path=md_path,
                    template_path=template_path,
                    dest_path=dest_path
                )
