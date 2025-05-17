from typing import List
from self_improving_ai import parse_html, ElementInfo

html: str = open("tests/test_html_parser.html", "r").read()

expected_output: List[ElementInfo] = [
    ElementInfo(
        element="heading",
        text="Welcome to Our Service",
        selector="header > h1"
    ),
    ElementInfo(
        element="link",
        text="Home",
        selector="header > nav > ul > li:nth-of-type(1) > a"
    ),
    ElementInfo(
        element="link",
        text="Sign Up",
        selector="header > nav > ul > li:nth-of-type(2) > a"
    ),
    ElementInfo(
        element="heading",
        text="Create Your Account",
        selector=".main-container > section.intro > h2"
    ),
    ElementInfo(
        element="text",
        text="Please complete the form below to register.",
        selector=".main-container > section.intro > p"
    ),
    ElementInfo(
        element="input",
        text="Enter your email",
        selector=".main-container > section.form-section > form > div:nth-of-type(1) > input[type='email']"
    ),
    ElementInfo(
        element="input",
        text="Choose a password",
        selector=".main-container > section.form-section > form > div:nth-of-type(2) > input[type='password']"
    ),
    ElementInfo(
        element="btn",
        text="Sign Up",
        selector=".main-container > section.form-section > form > .actions > button"
    ),
    ElementInfo(
        element="text",
        text="© 2025 Company Name. All rights reserved.",
        selector="footer > p"
    ),
]

def test_html_parser():
    assert parse_html(html) == expected_output
