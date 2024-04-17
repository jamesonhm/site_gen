import os
import shutil


def copy_static_recursive(source, dest):
    if not os.path.exists(dest):
        os.mkdir(dest)

    for file in os.listdir(source):
        from_path = os.path.join(source, file)
        dest_path = os.path.join(dest, file)
        if os.path.isfile(from_path):
            print(f"- Copying from {from_path}")
            shutil.copy(from_path, dest_path)
        else:
            copy_static_recursive(from_path, dest_path)

def copy_static(source: str, dest: str):
    if os.path.exists(dest):
        shutil.rmtree(dest)
    # os.mkdir(dest)
    source_files = os.listdir(source)
    for file in source_files:
        fpath = source + '/' + file
        print(f"file: {fpath}")
        # shutil.copy(fpath, dest)
    shutil.copytree(source, dest)

