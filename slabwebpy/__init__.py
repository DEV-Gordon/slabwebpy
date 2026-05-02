""" SlabWebPy - A simple web framework for building static websites with Python. 
    Pure python, no JavaScript or CSS required. Just write Python code to create your website!
    
    
    Usage: 
        import slabwebpy as swp
        swp.title("Welcome to My Website", size="2xl", color="blue")
        swp.build("dist/index.html")
"""

from .components import (
    title,
    navbar,
    hero,
    section,
    grid,
    grid_end,
    card,
    button,
    text,
    badge,
    divider,
    spacer,
    footer,
    faq,
    image,
)

from .builder import build
from .server import serve

__version__ = "0.1.0"
__all__ = [
    "title",
    "navbar",
    "hero",
    "section",
    "grid",
    "grid_end",
    "card",
    "button",
    "text",
    "badge",
    "divider",
    "spacer",
    "footer",
    "build",
    "serve"
]