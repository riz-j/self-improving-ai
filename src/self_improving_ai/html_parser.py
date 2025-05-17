from typing import List
from pydantic import BaseModel

class ElementInfo(BaseModel):
    element: str
    text: str
    selector: str

def parse_html(html: str) -> List[ElementInfo]:
    from html.parser import HTMLParser

    class _HTMLParser(HTMLParser):
        def __init__(self):
            super().__init__()
            self.stack: list[dict] = []
            self.results: list[ElementInfo] = []

        def handle_starttag(self, tag: str, attrs: list[tuple[str, str]]):
            attrs_dict = dict(attrs)
            if tag == "input":
                element = "input"
                text = attrs_dict.get("placeholder", "")
                selector = self._build_selector(self.stack, tag, attrs_dict)
                self.results.append(ElementInfo(element=element, text=text, selector=selector))
                return
            self.stack.append({"tag": tag, "attrs": attrs_dict, "text": ""})

        def handle_data(self, data: str):
            if not self.stack:
                return
            text = data.strip()
            if not text:
                return
            current = self.stack[-1]
            current["text"] += text

        def handle_endtag(self, tag: str):
            if not self.stack or self.stack[-1]["tag"] != tag:
                return
            current = self.stack.pop()
            if tag == "button":
                element = "btn"
                text = current.get("text", "")
                selector = self._build_selector(self.stack, tag, current["attrs"])
                self.results.append(ElementInfo(element=element, text=text, selector=selector))

        def _build_selector(self, ancestors: list[dict], tag: str, attrs: dict) -> str:
            parts: list[str] = []
            for ctx in ancestors:
                name = ctx["tag"]
                cls = ctx["attrs"].get("class")
                if cls:
                    class_name = cls.split()[0]
                    parts.append(f".{class_name}")
                else:
                    parts.append(name)
            if tag == "input" and attrs.get("type"):
                parts.append(f"{tag}[type='{attrs['type']}']")
            else:
                parts.append(tag)
            return " > ".join(parts)

    parser = _HTMLParser()
    parser.feed(html)
    parser.close()
    return parser.results