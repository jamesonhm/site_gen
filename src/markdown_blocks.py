
from htmlnode import ParentNode
from inline_markdown import text_to_textnodes
from textnode import text_node_to_html_node

block_type_paragraph = "paragraph"
block_type_heading = "heading"
block_type_code = "code"
block_type_quote = "quote"
block_type_ulist = "unordered_list"
block_type_olist = "ordered_list"


def markdown_to_blocks(markdown):
    blocks = markdown.split("\n\n")
    blocks = [block.strip() for block in blocks]
    final = []
    for block in blocks:
        final.append('\n'.join([line.strip() for line in block.split('\n')]))
    return final

def block_to_block_type(markdown):
    lines = markdown.split('\n')
    if (markdown.startswith('# ')
        or markdown.startswith('## ')
        or markdown.startswith('### ')
        or markdown.startswith('#### ')
        or markdown.startswith('##### ')
        or markdown.startswith('###### ')
            ):
        return block_type_heading
    elif len(lines) > 1 and lines[0].startswith('```') and lines[-1].startswith('```'):
        return block_type_code
    elif markdown.startswith('>'):
        for line in lines:
            if not line.startswith('>'):
                return block_type_paragraph
        return block_type_quote
    elif markdown.startswith('* '):
        for line in lines:
            if not line.startswith('* '):
                return block_type_paragraph
        return block_type_ulist
    elif markdown.startswith('- '):
        for line in lines:
            if not line.startswith('- '):
                return block_type_paragraph
        return block_type_ulist
    elif markdown.startswith('1. '):
        i = 1
        for line in lines:
            if not line.startswith(f"{i}. "):
                return block_type_paragraph
            i += 1
        return block_type_olist
    else:
        return block_type_paragraph

def text_to_children(text):
    text_nodes = text_to_textnodes(text)
    children = []
    for node in text_nodes:
        html_node = text_node_to_html_node(node)
        children.append(html_node)
    return children

def paragraph_to_html(block):
    lines = block.split('\n')
    paragraph = ' '.join(lines)
    children = text_to_children(paragraph)
    return ParentNode("p", children)

def heading_to_html(block):
    level = block.count('#')
    header = block[level+1:]
    children = text_to_children(header)
    return ParentNode(f"h{level}", children)

def code_to_html(block):
    inner = block[4:-4]
    children = text_to_children(inner)
    return ParentNode("pre", [ParentNode("code", children)])

def quote_to_html(block):
    lines = block.split('\n')
    lines = ' '.join([line.lstrip('>').strip() for line in lines])
    children = text_to_children(lines)
    return ParentNode("blockquote", children)

def ulist_to_html(block):
    lines = block.split('\n')
    html_items = []
    for line in lines:
        text = line[2:]
        children = text_to_children(text)
        html_items.append(ParentNode("li", children))
    return ParentNode('ul', html_items)

def olist_to_html(block):
    lines = block.split('\n')
    html_items = []
    for line in lines:
        text = line[3:]
        children = text_to_children(text)
        html_items.append(ParentNode("li", children))
    return ParentNode('ol', html_items)

def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    types = [block_to_block_type(block) for block in blocks]
    nodes = []
    for block, block_type in list(zip(blocks, types)):
        match block_type:
            case "paragraph":
                nodes.append(paragraph_to_html(block))
            case "heading":
                nodes.append(heading_to_html(block))
            case "code":
                nodes.append(code_to_html(block))
            case "quote":
                nodes.append(quote_to_html(block))
            case "unordered_list":
                nodes.append(ulist_to_html(block))
            case "ordered_list":
                nodes.append(olist_to_html(block))
            case _:
                raise Exception(f"Not a block type {block_type}")
    return ParentNode('div', nodes)

