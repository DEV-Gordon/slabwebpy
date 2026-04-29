"""
slab.state — Internal page state.
Holds all blocks added during a build session.
"""

_blocks: list[str] = []
_page_title: str = "My Page"


def add(html: str):
    """Append an HTML block to the current page."""
    _blocks.append(html)


def set_title(title: str):
    """Set the browser <title> for the page."""
    global _page_title
    _page_title = title


def get_title() -> str:
    return _page_title


def get_blocks() -> list[str]:
    return _blocks


def reset():
    """Clear all state. Called automatically after build()."""
    global _blocks, _page_title
    _blocks = []
    _page_title = "My Page"


"""*Autor: DEV-Gordon (Carlos Zarate) — https://github.com/DEV-Gordon/slabwebpy*"""