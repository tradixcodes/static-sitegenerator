import os
import shutil
from pathlib import Path

def clean_directory(directory: Path):
    if not directory.exists():
        print(f"Directory doesn't exist!")
        return

    for item in directory.iterdir():
        if item.is_dir():
            shutil.rmtree(item)
        else:
            item.unlink()

def copy_recursive(src: Path, dest: Path):
    if not src.exists():
        raise FileNotFoundError(f"Source directory does not exist: {src}")

    dest.mkdir(parents=True, exist_ok=True)

    for item in src.iterdir():
        src_path = item
        dest_path = dest / item.name

        if src_path.is_dir():
            copy_recursive(src_path, dest_path)
        else:
            print(f"Copying: {src_path} -> {dest_path}")
            shutil.copy2(src_path, dest_path)


def sync_static_to_public():
    """Clean the public folder, then copy static → public."""
    src = Path("~/Projects/static-sitegenerator/static/").expanduser()
    dest = Path("~/Projects/static-sitegenerator/public/").expanduser()

    print("🧹 Cleaning destination directory...")
    clean_directory(dest)

    print("📁 Copying static → public...")
    copy_recursive(src, dest)

    print("✅ Sync complete!")
