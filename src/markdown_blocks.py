
from htmlnode import LeafNode, ParentNode


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

def paragraph_to_html(block):
    return LeafNode("p", block)

def heading_to_html(block):
    level = block.count('#')
    header = block[level+1:]
    return LeafNode(f"h{level}", header)

def code_to_html(block):
    inner = '\n'.join('\n'.split(block)[1:-1])
    return ParentNode("pre", [LeafNode("code", inner)])

def quote_to_html(block):
    lines = '\n'.split(block)
    lines = '\n'.join([line[1:] for line in lines])
    return LeafNode("blockquote", lines)

def ulist_to_html(block):
    lines = '\n'.split(block)
    lines = [line[2:] for line in lines]
    inner = [LeafNode('li', line) for line in lines]
    return ParentNode('ul', inner)

def olist_to_html(block):
    lines = '\n'.split(block)
    lines = [line[3:] for line in lines]
    inner = [LeafNode('li', line) for line in lines]
    return ParentNode('ol', inner)

def markdown_to_html_nodes(markdown):
    blocks = markdown_to_blocks(markdown)
    types = [block_to_block_type(block) for block in blocks]
    nodes = []
    for block, block_type in list(zip(blocks, types)):
        match block_type:
            case block_type_paragraph:
                nodes.append(paragraph_to_html(block))
            case block_type_heading:
                nodes.append(heading_to_html(block))
            case block_type_code:
                nodes.append(code_to_html(block))
            case block_type_quote:
                nodes.append(quote_to_html(block))
            case block_type_ulist:
                nodes.append(ulist_to_html(block))
            case block_type_olist:
                nodes.append(olist_to_html(block))
            case _:
                raise Exception(f"Not a block type {block_type}")
    return ParentNode('div', nodes)

