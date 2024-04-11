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

def text_to_textnodes(text):
    node = TextNode(text, text_type_text)
    delimiters = ['**', '*', '`']
    types = [text_type_bold, text_type_italic, text_type_code]
    nodes = [node]
    for delim_type in list(zip(delimiters, types)):
        nodes = split_nodes_delimiter(nodes, delim_type[0], delim_type[1])
    nodes = split_nodes_image(nodes)
    nodes = split_nodes_link(nodes)
    return nodes

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != text_type_text:
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

def split_nodes_image(old_nodes):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != text_type_text:
            new_nodes.append(old_node)
            continue
        image_tups = extract_markdown_images(old_node.text)
        if len(image_tups) == 0:
            new_nodes.append(old_node)
            continue
        rem_txt = old_node.text
        for image_tup in image_tups:
            sections = rem_txt.split(f"![{image_tup[0]}]({image_tup[1]})", 1)
            if len(sections) != 2:
                raise ValueError("Invalid Markdown")
            pre, rem_txt = sections
            if pre:
                new_nodes.append(TextNode(pre, text_type_text))
            new_nodes.append(TextNode(image_tup[0], text_type_image, image_tup[1]))
        if rem_txt:
            new_nodes.append(TextNode(rem_txt, text_type_text))
    return new_nodes

def split_nodes_link(old_nodes):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != text_type_text:
            new_nodes.append(old_node)
            continue
        link_tups = extract_markdown_links(old_node.text)
        if len(link_tups) == 0:
            new_nodes.append(old_node)
            continue
        rem_txt = old_node.text
        for link_tup in link_tups:
            sections = rem_txt.split(f"[{link_tup[0]}]({link_tup[1]})", 1)
            if len(sections) != 2:
                raise ValueError("Invalid Markdown")
            pre, rem_txt = sections
            if pre:
                new_nodes.append(TextNode(pre, text_type_text))
            new_nodes.append(TextNode(link_tup[0], text_type_link, link_tup[1]))
        if rem_txt:
            new_nodes.append(TextNode(rem_txt, text_type_text))
    return new_nodes

