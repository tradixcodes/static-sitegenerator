import os
# Shutil provides high-level file operations (copying files/directories, removing directory trees, etc ...)
import shutil
from pathlib import Path

def clean_directory(directory: Path):
    # This is a function that checks the given path, if it exists deletes 
    # the contents inside the given directory, if it doesn't exist it return None
    if not directory.exists():
        print(f"Directory doesn't exist!")
        return

    for item in directory.iterdir():
        # iterates over each entry inside the directory
        if item.is_dir():
            #. if item is a directory 
            shutil.rmtree(item)
            # delete directory and all its contents(remove the entire directory tree rooted at item)
        else:
            # if not a directory
            item.unlink()
            # delete the file or symlink represented by item

def copy_recursive(src: Path, dest: Path):
    # This function takes two arguements src(path) and dest(path)
    # checks if the src path exists, if it does makes a dest(path) if it doesn't exist
    # Then iterates over every item in the src directory, gives item as a path object pointing to the child to be stored as a variable src_path
    # if the src_path is a directory, it calls the function to itself again(check src.iter() comments for more understanding)
    # if not it uses shutil.copy2 to copy the file to the destination file
    # the recursion allows the file tree to remain intact as it was in the src folder

    # If the src file path doesn't exist returns a FileNotFoundError
    if not src.exists():
        raise FileNotFoundError(f"Source directory does not exist: {src}")
    
    # Creates the destination directory and any missing parent directories.
    # parents=True allows creation of intermediate directories if they don't exist
    # exist_ok=True suppresses an error if the destination already exists
    dest.mkdir(parents=True, exist_ok=True)

    for item in src.iterdir():
        #. iterate over each child inside the source directory
        #. src.iterdir() gives each item as a path object, not as a the object itself
        #. thats why we use item.name in the dest_path
        src_path = item
        # print(f"This is the src path: {src_path}")
        dest_path = dest / item.name
        # print(f"This is the dest path: {dest_path}")

        if src_path.is_dir():
            # This recursive call uses the new src path that is made a directory
            # in the dest path by thid line: dest.mkdir(parents=True, exist_ok=True)
            copy_recursive(src_path, dest_path)
        else:
            print(f"Copying: {src_path} -> {dest_path}")
            # shutil.copy2 copies file data and most metadata
            shutil.copy2(src_path, dest_path)


def sync_static_to_public():
    """Clean the docs folder, then copy static → public."""
    src = Path("~/Projects/static-sitegenerator/static/").expanduser()
    dest = Path("~/Projects/static-sitegenerator/docs/").expanduser()

    print("🧹 Cleaning destination directory...")
    clean_directory(dest)

    print("📁 Copying static → public...")
    copy_recursive(src, dest)

    print("✅ Sync complete!")
