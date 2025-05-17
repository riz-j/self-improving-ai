from typing import List
from self_improving_ai import parse_html, ElementInfo

html: str = """
<div class="main-container">
    <div>
        <button>Sign Up</button>
        <input type="email" placeholder="Enter your email">
    </div>
</div>
"""

expected_output: List[ElementInfo] = [
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

def test_html_parser():
    assert parse_html(html) == expected_output