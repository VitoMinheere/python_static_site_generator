import unittest

from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):

    def test_repr(self):
        test = 'HTMLNode(b, This is a text node, None,  href="https://www.google.com" target="_blank")'
        node = HTMLNode(
                "b",
                "This is a text node",
                None,
                {
                    "href": "https://www.google.com",
                    "target": "_blank",
                })
        self.assertEqual(str(node), test)

    def test_props_to_html(self):
        node = HTMLNode(
                "b",
                "This is a text node",
                None,
                {
                    "href": "https://www.google.com",
                    "target": "_blank",
                })
        result = node.props_to_html()
        self.assertEqual(result, ' href="https://www.google.com" target="_blank"')

if __name__ == "__main__":
    unittest.main()
