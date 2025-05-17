from typing import List
from self_improving_ai import parse_html, ElementInfo

html: str = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Signup Page</title>
    <script src="https://cdn.jsdelivr.net/npm/@tailwindcss/browser@4"></script>
</head>
<body class="bg-gray-50 text-gray-900">
    <header class="bg-white shadow p-4">
        <h1 class="text-3xl font-bold text-center">Welcome to Our Service</h1>
        <nav class="mt-2">
            <ul class="flex space-x-4 justify-center">
                <li><a href="/" class="hover:underline">Home</a></li>
                <li><a href="/signup" class="hover:underline">Sign Up</a></li>
            </ul>
        </nav>
    </header>

    <main class="main-container container mx-auto p-6">
        <section class="intro mb-6">
            <h2 class="text-2xl font-semibold mb-2">Create Your Account</h2>
            <p class="text-gray-700 mb-4">Please complete the form below to register.</p>
        </section>

        <section class="form-section bg-white shadow rounded p-6">
            <form id="signup-form" class="space-y-4">
                <div>
                    <label for="email" class="block text-sm font-medium">Email Address</label>
                    <input
                        type="email"
                        id="email"
                        placeholder="Enter your email"
                        class="mt-1 block w-full border border-gray-300 rounded px-3 py-2"
                    >
                </div>

                <div>
                    <label for="password" class="block text-sm font-medium">Password</label>
                    <input
                        type="password"
                        id="password"
                        placeholder="Choose a password"
                        class="mt-1 block w-full border border-gray-300 rounded px-3 py-2"
                    >
                </div>

                <div class="actions text-right">
                    <button
                        type="submit"
                        class="bg-blue-500 hover:bg-blue-600 text-white font-semibold py-2 px-4 rounded"
                    >
                        Sign Up
                    </button>
                </div>
            </form>
        </section>

        <aside class="sidebar hidden">
            <p class="text-sm">This sidebar is hidden by default.</p>
        </aside>
    </main>

    <footer class="text-center text-sm text-gray-500 py-4">
        <p>© 2025 Company Name. All rights reserved.</p>
    </footer>
</body>
</html>
"""

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
