
class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def __repr__(self):
        return f"""tag: {self.tag},
                    value: {self.value},
                    children: {self.children},
                    props: {self.props}
                """

    def to_html(self):
        raise NotImplementedError()

    def props_to_html(self):
        if not self.props:
            return ''
        propls = [key + '="' + value + '"' for key, value in self.props.items()]
        return ' ' + ' '.join(propls)

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag=tag, value=value, props=props)

    def to_html(self):
        if self.value is None:
            raise ValueError("Leaf Nodes require a value")
        if self.tag is None:
            return self.value
        else:
            return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"


class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag=tag, children=children, props=props)

    def to_html(self):
        if self.tag is None:
            raise ValueError("Parent Nodes require a tag")
        if self.children is None:
            raise ValueError("Parent Nodes require children")
        return f"<{self.tag}{self.props_to_html()}>{''.join([n.to_html() for n in self.children])}</{self.tag}>"
