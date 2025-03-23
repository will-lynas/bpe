import os

test_strings = [
    # Emtpy string
    "",
    # Single character
    "a",
    # Two characters
    "ab",
    # Unicode characters
    "hello world!!!? (안녕하세요!) lol123 😉",
    # File (handled by unpack())
    "FILE:taylorswift.txt",
]

def unpack(text):
    """
    `pytest -v` prints arguments to the console.
    We don't want to print an entire file, so the file is loaded here.
    """
    if not text.startswith("FILE:"):
        return text
    dirname = os.path.dirname(os.path.abspath(__file__))
    file = os.path.join(dirname, text.replace("FILE:", ""))
    contents = open(file, "r", encoding="utf-8").read()
    return contents