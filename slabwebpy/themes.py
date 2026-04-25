"""
slab.themes — Color palettes and size scales.
All style decisions live here.
"""

COLORS = {
    "blue":   ("bg-blue-600",   "text-blue-600",   "border-blue-600",   "hover:bg-blue-700"),
    "red":    ("bg-red-500",    "text-red-500",    "border-red-500",    "hover:bg-red-600"),
    "green":  ("bg-green-600",  "text-green-600",  "border-green-600",  "hover:bg-green-700"),
    "yellow": ("bg-yellow-400", "text-yellow-500", "border-yellow-400", "hover:bg-yellow-500"),
    "purple": ("bg-purple-600", "text-purple-600", "border-purple-600", "hover:bg-purple-700"),
    "gray":   ("bg-gray-700",   "text-gray-600",   "border-gray-300",   "hover:bg-gray-800"),
    "white":  ("bg-white",      "text-white",      "border-white",      "hover:bg-gray-100"),
    "black":  ("bg-black",      "text-black",      "border-black",      "hover:bg-gray-900"),
    "indigo": ("bg-indigo-600", "text-indigo-600", "border-indigo-600", "hover:bg-indigo-700"),
    "pink":   ("bg-pink-500",   "text-pink-500",   "border-pink-500",   "hover:bg-pink-600"),
}

SIZES = {
    "sm":  ("text-sm",   "px-3 py-1.5"),
    "md":  ("text-base", "px-5 py-2.5"),
    "lg":  ("text-lg",   "px-7 py-3"),
    "xl":  ("text-xl",   "px-9 py-4"),
}

BG = {
    "white": "bg-white",
    "gray":  "bg-gray-50",
    "black": "bg-gray-900",
    "dark":  "bg-gray-800",
}

def color(name: str, index: int) -> str:
    """Get a Tailwind class from a color name and variant index.
    
    Index:
        0 = bg class       (e.g. bg-blue-600)
        1 = text class     (e.g. text-blue-600)
        2 = border class   (e.g. border-blue-600)
        3 = hover bg class (e.g. hover:bg-blue-700)
    """
    return COLORS.get(name, COLORS["blue"])[index]

def size(name: str) -> tuple[str, str]:
    """Returns (text_size_class, padding_class) for a given size name."""
    return SIZES.get(name, SIZES["md"])

def bg(name: str) -> str:
    """Returns a background Tailwind class for a given color name."""
    return BG.get(name, "bg-white")