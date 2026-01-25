import unittest

from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_repr(self):
        test = "TextNode(This is a text node, bold, None)"
        node = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(str(node), test)


if __name__ == "__main__":
    unittest.main()
