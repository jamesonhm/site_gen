import os
import pathlib
import shutil

from copystatic import copy_static, copy_static_recursive
from md_to_html import generate_page
from textnode import TextNode


root_dir = pathlib.Path(__file__).parent.parent.resolve()
dir_path_static = str(root_dir) + '/static'
dir_path_public = str(root_dir) + '/public'


def main():
    node = TextNode("this is a text node", "bold", "https://boot.dev")
    # print(node)
    # print(f"root: {root_dir}")
    print("Deleting public directory...")
    if os.path.exists(dir_path_public):
        shutil.rmtree(dir_path_public)

    print("Copying static files to public dir...")
    copy_static_recursive(dir_path_static, dir_path_public)

    generate_page('./content/index.md', 'template.html', './public/index.html')

if __name__ == "__main__":
    main()

