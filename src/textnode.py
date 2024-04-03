from htmlnode import LeafNode

text_type_text = "text"
text_type_bold = "bold"
text_type_italic = "italic"
text_type_code = "code"
text_type_link = "link"
text_type_image = "image"


class TextNode:

    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = text_type 
        self.url = url

    def __eq__(self, other):
        return self.text == other.text and self.text_type == other.text_type and self.url == other.url 

    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type}, {self.url})"


def text_node_to_html_node(text_node: TextNode):
    match text_node.text_type:
        case "text":
            return LeafNode(None, text_node.text)
        case "bold":
            return LeafNode("b", text_node.text)
        case "italic":
            return LeafNode("i", text_node.text)
        case "code":
            return LeafNode("code", text_node.text)
        case "link":
            return LeafNode("a", text_node.text, {"href": text_node.url})
        case "image":
            return LeafNode("img", '', {"src": text_node.url, "alt": text_node.text})
        case _:
            raise Exception(f"Invalid text type {text_node.text_type}")

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
        print(f"split node: {split_node}")
        for i, text in enumerate(split_node):
            if text == '':
                continue
            if i % 2 != 0:
                print(f"adding node {TextNode(text, text_type)}")
                new_nodes.extend([TextNode(text, text_type)])
            else:
                print(f"adding node {TextNode(text, text_type_text)}")
                new_nodes.extend([TextNode(text, text_type_text)])
    return new_nodes


