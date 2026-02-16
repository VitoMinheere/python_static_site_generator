from htmlnode import HTMLNode

class LeafNode():
    def __init__(self,
                 tag: str,
                 value: str,
                 children: list[HTMLNode] = None,
                 props: dict = None):
        super().__init__()
        self.children = None

    def to_html(self):
        if not self.value:
            raise ValueError("Leaf must have a value")
        if not self.tag:
            return self.value


    def __repr__(self):
        return f"LeafNode({self.tag}, {self.value}, {self.props_to_html()})"
