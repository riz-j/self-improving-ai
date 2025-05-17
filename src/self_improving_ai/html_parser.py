from typing import List
from pydantic import BaseModel

class ElementInfo(BaseModel):
    element: str
    text: str
    selector: str

def parse_html(html: str) -> List[ElementInfo]:
    from html.parser import HTMLParser

    class Node:
        def __init__(self, tag, attrs, parent):
            self.tag = tag
            self.attrs = attrs
            self.parent = parent
            self.children = []
            self.text = ""

    class _HTMLParser(HTMLParser):
        def __init__(self):
            super().__init__()
            self.root = Node("document", {}, None)
            self.current = self.root

        def handle_starttag(self, tag: str, attrs: list[tuple[str, str]]):
            attrs_dict = dict(attrs)
            node = Node(tag, attrs_dict, self.current)
            self.current.children.append(node)
            if tag in ("input", "meta", "link", "br", "hr", "img"):
                return
            self.current = node

        def handle_data(self, data: str):
            text = data.strip()
            if text:
                self.current.text += text

        def handle_endtag(self, tag: str):
            if self.current.tag == tag and self.current.parent is not None:
                self.current = self.current.parent

    parser = _HTMLParser()
    parser.feed(html)
    parser.close()

    def has_hidden_ancestor(node: Node) -> bool:
        parent = node.parent
        while parent:
            if "hidden" in parent.attrs.get("class", "").split():
                return True
            parent = parent.parent
        return False

    def get_selector(node: Node) -> str:
        parts: list[str] = []
        ancestors = []
        cur = node.parent
        while cur and cur.tag != "document":
            ancestors.append(cur)
            cur = cur.parent
        for ctx in reversed(ancestors):
            tag = ctx.tag
            if tag in ("html", "body"):
                continue
            classes = ctx.attrs.get("class", "").split()
            if tag == "main" and classes:
                parts.append(f".{classes[0]}")
            elif tag == "section" and classes:
                parts.append(f"{tag}.{classes[0]}")
            elif tag == "div" and classes:
                parts.append(f".{classes[0]}")
            else:
                parent = ctx.parent
                siblings = [c for c in (parent.children if parent else []) if c.tag == tag]
                if len(siblings) > 1:
                    idx = siblings.index(ctx) + 1
                    parts.append(f"{tag}:nth-of-type({idx})")
                else:
                    parts.append(tag)
        if node.tag == "input":
            t = node.attrs.get("type", "")
            parts.append(f"{node.tag}[type='{t}']")
        else:
            parts.append(node.tag)
        return " > ".join(parts)

    results: list[ElementInfo] = []

    def traverse(node: Node):
        for child in node.children:
            traverse(child)
            tag = child.tag
            if tag == "input":
                text = child.attrs.get("placeholder", "")
                elem = "input"
            elif tag in ("h1", "h2", "h3", "h4", "h5", "h6"):
                text = child.text
                elem = "heading"
            elif tag == "a":
                text = child.text
                elem = "link"
            elif tag == "p":
                text = child.text
                elem = "text"
            elif tag == "button":
                text = child.text
                elem = "btn"
            else:
                continue
            if not text or has_hidden_ancestor(child):
                continue
            sel = get_selector(child)
            results.append(ElementInfo(element=elem, text=text, selector=sel))

    traverse(parser.root)
    return results