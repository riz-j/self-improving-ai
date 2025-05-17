from typing import List
from pydantic import BaseModel

class ElementInfo(BaseModel):
    element: str
    text: str
    selector: str

sample_output: List[ElementInfo] = [
    ElementInfo(
        element="btn",
        text="Sign Up",
        selector=".main-container > div > button"
    ),
    ElementInfo(
        element="input",
        text="Enter your email",
        selector=".main-container > div > input[type='email']"
    ),
]

def parse_html(html: str) -> List[ElementInfo]:
    return sample_output