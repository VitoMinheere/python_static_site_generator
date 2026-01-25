class HTMLNode():
    def __init__(self,
                 tag: str = None,
                 value: str = None,
                 children: list[HTMLNode] = None,
                 props: dict = None):
        self.tag = tag
        self.vlaue = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError

    def props_to_html(self):
        prop_string = ""
        for k, v in self.props.items:
            prop_string += f' {k}="{v}"'

        return prop_string

    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props_to_html()})"
