import os
import pathlib
import shutil

from copystatic import copy_static, copy_static_recursive
from md_to_html import generate_page, generate_pages_recursive
from textnode import TextNode


root_dir = pathlib.Path(__file__).parent.parent.resolve()
dir_path_static = str(root_dir) + '/static'
dir_path_public = str(root_dir) + '/public'


def main():
    print("Deleting public directory...")
    if os.path.exists(dir_path_public):
        shutil.rmtree(dir_path_public)

    print("Copying static files to public dir...")
    copy_static_recursive(dir_path_static, dir_path_public)

    generate_pages_recursive('./content/', 'template.html', './public/')

if __name__ == "__main__":
    main()

