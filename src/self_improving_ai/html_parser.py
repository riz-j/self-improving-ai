from typing import List
from pydantic import BaseModel

class ElementInfo(BaseModel):
    element: str
    text: str
    selector: str

def parse_html(html: str) -> List[ElementInfo]:
    raise NotImplementedError()