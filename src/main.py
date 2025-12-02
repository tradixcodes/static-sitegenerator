import sys
from pathlib import Path
from copy_static_public import sync_static_to_public
from generate_pages_recursively import generate_pages_recursive

def main():
    basepath = sys.argv[1] if len(sys.argv) > 1 else "/"
    print(f"Using basepath: {basepath}")

    print("Running static -> public sync...")
    sync_static_to_public()

    content_dir = Path("~/Projects/static-sitegenerator/content").expanduser()
    template_file = Path("~/Projects/static-sitegenerator/template.html").expanduser()
    public_dir = Path("~/Projects/static-sitegenerator/docs/").expanduser()

    print("📝 Generating pages ...")
    generate_pages_recursive(
        dir_path_content=content_dir,
        template_path=template_file,
        dest_dir_path=public_dir,
        basepath=basepath
    )

    print("🎉 Site generation complete!")

if __name__ == "__main__":
    main()
