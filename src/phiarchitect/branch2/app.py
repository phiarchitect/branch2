"""
run the main app
"""
from .branch2 import Branch2


def run() -> None:
    reply = Branch2().run()
    print(reply)
