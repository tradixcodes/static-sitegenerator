from pathlib import Path
from copy_static_public import sync_static_to_public
from generate_pages_recursively import generate_pages_recursive

def main():
    print("Running static -> public sync...")
    sync_static_to_public()

    content_dir = Path("~/Projects/static-sitegenerator/content").expanduser()
    template_file = Path("~/Projects/static-sitegenerator/template.html").expanduser()
    public_dir = Path("~/Projects/static-sitegenerator/public/").expanduser()

    print("📝 Generating homepage...")
    generate_pages_recursive(
        dir_path_content=content_dir,
        template_path=template_file,
        dest_dir_path=public_dir
    )

    print("🎉 Site generation complete!")

if __name__ == "__main__":
    main()
