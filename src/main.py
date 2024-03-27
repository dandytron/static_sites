import os
import shutil
from textnode import TextNode
from copystatic import recursive_copy_static

public_dir_path = "./public"
static_dir_path = "./static"

def main():
    print("...deleting /public directory")
    if os.path.exists(public_dir_path):
        shutil.rmtree(public_dir_path)
    
    print("...copying /static directory")
    recursive_copy_static(static_dir_path, public_dir_path)

if __name__ == "__main__":
    main()