import re
from textnode import (
    TextNode,
    text_type_text,
    text_type_bold,
    text_type_italic,
    text_type_code,
    text_type_image,
    text_type_link,
)


def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for old_node in old_nodes:
        if not isinstance(old_node, TextNode):
            new_nodes.append(old_node)
            continue
        delim_count = old_node.text.count(delimiter)
        if delim_count % 2 != 0:
            raise Exception(f"Missing closing delimiter {delimiter}")
        split_node = old_node.text.split(delimiter)
        for i, text in enumerate(split_node):
            if text == '':
                continue
            if i % 2 != 0:
                new_nodes.extend([TextNode(text, text_type)])
            else:
                new_nodes.extend([TextNode(text, text_type_text)])
    return new_nodes

def extract_markdown_images(text):
    matches = re.findall(r"!\[(.*?)\]\((.*?)\)", text)
    return matches

def extract_markdown_links(text):
    matches = re.findall(r"\[(.*?)\]\((.*?)\)", text)
    return matches

