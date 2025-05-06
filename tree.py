# For printing a basic folder tree
# Usage: python3 tree.py /path/to/folder --exclude node_modules venv

import os
import sys
import argparse

BLACK_LIST = ["venv","requirements.txt","__pycache__","all_files",".git",".DS_Store"]

def print_tree(start_path, exclude, prefix=""):
    # List all entries in the directory, sorted alphabetically
    try:
        entries = sorted(os.listdir(start_path))
    except PermissionError:
        print(prefix + "└── [Permission Denied]")
        return

    entries_count = len(entries)
    
    for index, entry in enumerate(entries):
        path = os.path.join(start_path, entry)
        # Determine the tree branch characters
        if index == entries_count - 1:
            connector = "└── "
            extension = "    "
        else:
            connector = "├── "
            extension = "│   "
        
        print(prefix + connector + entry)
        
        # If entry is a directory and not in the exclude list, recursively print its contents
        if os.path.isdir(path):
            if entry in exclude:
                print(prefix + extension + "[Excluded]")
            else:
                print_tree(path, exclude, prefix + extension)

def main():
    parser = argparse.ArgumentParser(description="Print folder structure as a tree with an option to exclude folders.")
    parser.add_argument("folder", nargs="?", default=".", help="Folder to print tree structure (default: current directory)")
    parser.add_argument("--exclude", "-e", nargs="*", default=["all_files"], help="List of folder names to exclude")
    
    args = parser.parse_args()
    
    folder = args.folder
    exclude = args.exclude + BLACK_LIST
        
    print(folder)
    print_tree(folder, exclude)

if __name__ == "__main__":
    main()
