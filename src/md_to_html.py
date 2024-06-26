import os
from markdown_blocks import markdown_to_html_node


def extract_title(markdown):
    for line in markdown.split('\n'):
        if line.startswith('# '):
            return line[2:]
    raise Exception("Markdown must contain an H1 Header")

def generate_page(from_path, template_path, dest_path):
    print(f"Generating a page from {from_path} to {dest_path} using {template_path}")

    md_f = open(from_path, "r")
    md = md_f.read()
    md_f.close()
    templ_f = open(template_path, "r")
    templ = templ_f.read()
    templ_f.close()

    html = markdown_to_html_node(md).to_html()
    title = extract_title(md)
    templ = templ.replace("{{ Title }}", title)
    templ = templ.replace("{{ Content }}", html)

    dest_dir = '/'.join(dest_path.split('/')[:-1])
    os.makedirs(dest_dir, exist_ok=True)
    f = open(dest_path, "w")
    f.write(templ)
    f.close()

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    if not os.path.exists(dest_dir_path):
        os.mkdir(dest_dir_path)

    for file in os.listdir(dir_path_content):
        from_path = os.path.join(dir_path_content, file)
        if os.path.isfile(from_path):
            dest_fname = file.split('.')[0] + '.html'
            dest_path = os.path.join(dest_dir_path, dest_fname)
            generate_page(from_path, template_path, dest_path)
        else:
            dest_path = os.path.join(dest_dir_path, file)
            generate_pages_recursive(from_path, template_path, dest_path)
