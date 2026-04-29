# Components for SlabWebPy
"""
slab.components — All visual components.
Each function appends HTML to the current page state.
"""

from . import state
from . import themes


# Legacy components 0.1 (will be refactored in future versions)

def title(text: str):
    """Sets the browser <title> of the page.

    Example:
        slab.title("Mi Landing")
    """
    state.set_title(text)

def navbar(
    brand: str = "MyBrand",
    links: list[tuple[str, str]] | None = None,
    color: str = "white",
    sticky: bool = True,
):
    """Top navigation bar.

    Args:
        brand:  Name/logo text shown on the left.
        links:  List of (label, url) tuples.
        color:  Background color name.
        sticky: Stays at the top while scrolling if True.

    Example:
        slab.navbar("MiApp", links=[("Inicio", "#"), ("Precios", "#precios")])
    """
    links = links or []
    bg       = themes.color(color, 0)
    text_cls = "text-gray-800" if color == "white" else "text-white"
    sticky_cls = "sticky top-0 z-50" if sticky else ""

    nav_links = "".join(
        f'<a href="{url}" class="{text_cls} hover:opacity-70 font-medium transition">{label}</a>'
        for label, url in links
    )
    state.add(f"""
    <nav class="{bg} shadow-md {sticky_cls}">
      <div class="max-w-6xl mx-auto px-6 py-4 flex items-center justify-between">
        <span class="{text_cls} text-xl font-bold tracking-tight">{brand}</span>
        <div class="flex gap-6">{nav_links}</div>
      </div>
    </nav>
    """)

def hero(
    title_text: str,
    subtitle: str = "",
    cta_label: str = "",
    cta_url: str = "#",
    color: str = "indigo",
    dark: bool = True,
):
    """Full-width hero / banner section.

    Args:
        title_text: Big headline text.
        subtitle:   Smaller description below the headline.
        cta_label:  Call-to-action button text (omit to hide).
        cta_url:    URL the CTA button points to.
        color:      Accent color for the gradient and button.
        dark:       Dark background with light text if True.

    Example:
        slab.hero("Bienvenido", subtitle="made with Python", cta_label="Empezar", color="blue")
    """
    bg_class   = themes.color(color, 0)
    btn_text   = themes.color(color, 1)
    text_color = "text-white" if dark else "text-gray-900"
    sub_color  = "text-white/80" if dark else "text-gray-600"
    bg_section = bg_class if dark else "bg-gray-50"

    cta_html = ""
    if cta_label:
        cta_html = (
            f'<a href="{cta_url}" class="bg-white {btn_text} font-semibold '
            f'px-8 py-3 rounded-full shadow hover:shadow-lg transition text-base">'
            f'{cta_label}</a>'
        )

    state.add(f"""
    <section class="{bg_section} py-24 px-6 text-center">
      <div class="max-w-3xl mx-auto space-y-6">
        <h1 class="{text_color} text-5xl font-extrabold tracking-tight leading-tight">{title_text}</h1>
        {"" if not subtitle else f'<p class="{sub_color} text-xl">{subtitle}</p>'}
        {cta_html}
      </div>
    </section>
    """)

def section(
    title_text: str = "",
    subtitle: str = "",
    bg: str = "white",
    centered: bool = True,
):
    """Generic section wrapper with optional title and subtitle.

    Args:
        title_text: Section heading.
        subtitle:   Description under the heading.
        bg:         Background color: "white", "gray", "black", "dark".
        centered:   Center-align content if True.

    Example:
        slab.section("Nuestros planes", subtitle="Elige el que más te convenga", bg="gray")
    """
    bg_class   = themes.bg(bg)
    dark       = bg in ("black", "dark")
    text_color = "text-white" if dark else "text-gray-900"
    sub_color  = "text-gray-400" if dark else "text-gray-500"
    align      = "text-center" if centered else "text-left"

    parts = []
    if title_text:
        parts.append(f'<h2 class="{text_color} text-3xl font-bold {align}">{title_text}</h2>')
    if subtitle:
        parts.append(f'<p class="{sub_color} text-lg {align} mt-2">{subtitle}</p>')

    state.add(f"""
    <section class="{bg_class} py-16 px-6">
      <div class="max-w-6xl mx-auto">
        {"".join(parts)}
      </div>
    </section>
    """)

def grid(columns: int = 3, gap: str = "6"):
    """Opens a responsive grid. Close it with grid_end().

    Args:
        columns: Number of columns (1–4).
        gap:     Gap between items in Tailwind scale.

    Example:
        slab.grid(3)
        slab.card(...)
        slab.grid_end()
    """
    col_map = {
        1: "grid-cols-1",
        2: "grid-cols-1 md:grid-cols-2",
        3: "grid-cols-1 md:grid-cols-2 lg:grid-cols-3",
        4: "grid-cols-1 md:grid-cols-2 lg:grid-cols-4",
    }
    cols = col_map.get(columns, col_map[3])
    state.add(f'<div class="max-w-6xl mx-auto px-6 py-10 grid {cols} gap-{gap}">')

def grid_end():
    """Closes a grid opened with grid()."""
    state.add("</div>")

def card(
    title_text: str,
    body: str = "",
    icon: str = "",
    color: str = "blue",
    variant: str = "bordered",
):
    """Content card component.

    Args:
        title_text: Card heading.
        body:       Description text.
        icon:       Optional emoji shown above the title.
        color:      Accent color.
        variant:    "bordered", "shadow", or "flat".

    Example:
        slab.card("Velocidad", "Genera páginas en milisegundos", icon="⚡", color="yellow")
    """
    accent      = themes.color(color, 0)
    border_top  = f"border-t-4 {accent.replace('bg-', 'border-')}" if variant == "bordered" else ""
    shadow_cls  = "shadow-lg" if variant in ("shadow", "bordered") else ""
    icon_html   = f'<div class="text-3xl mb-3">{icon}</div>' if icon else ""

    state.add(f"""
    <div class="bg-white rounded-xl p-6 {border_top} {shadow_cls}">
      {icon_html}
      <h3 class="text-gray-900 text-lg font-semibold mb-2">{title_text}</h3>
      <p class="text-gray-500 text-sm leading-relaxed">{body}</p>
    </div>
    """)

def button(
    label: str,
    url: str = "#",
    color: str = "blue",
    size: str = "md",
    variant: str = "solid",
    full_width: bool = False,
):
    """Standalone button / link.

    Args:
        label:      Button text.
        url:        Link destination.
        color:      Color name.
        size:       "sm", "md", "lg", or "xl".
        variant:    "solid", "outline", or "ghost".
        full_width: Stretch to full container width.

    Example:
        slab.button("Ver más", url="#features", color="indigo", size="lg")
    """
    txt, padding = themes.size(size)
    bg, text_c, border, hover = themes.COLORS.get(color, themes.COLORS["blue"])
    w = "w-full" if full_width else "inline-block"

    if variant == "solid":
        cls = f"{bg} text-white {padding} {txt} {hover} {w} rounded-lg font-medium transition"
    elif variant == "outline":
        cls = f"bg-transparent {text_c} border-2 {border} {padding} {txt} hover:opacity-70 {w} rounded-lg font-medium transition"
    else:  # ghost
        cls = f"bg-transparent {text_c} {padding} {txt} hover:underline {w} font-medium transition"

    state.add(f'<div class="px-6 py-2"><a href="{url}" class="{cls}">{label}</a></div>')

def text(
    content: str,
    size: str = "base",
    color: str = "gray-700",
    align: str = "left",
    bold: bool = False,
    tag: str = "p",
):
    """Paragraph / text block.

    Args:
        content: The text to display.
        size:    Tailwind size: "sm", "base", "lg", "xl", "2xl".
        color:   Tailwind text color (e.g. "gray-700", "red-500").
        align:   "left", "center", or "right".
        bold:    Bold text if True.
        tag:     HTML tag: "p", "span", "h3", "h4".

    Example:
        slab.text("Hola mundo", size="lg", align="center", bold=True)
    """
    weight = "font-bold" if bold else ""
    state.add(
        f'<{tag} class="text-{size} text-{color} text-{align} {weight} px-6 py-1">'
        f'{content}</{tag}>'
    )

def badge(label: str, color: str = "blue"):
    """Small inline badge / tag.

    Args:
        label: Badge text.
        color: Color name.

    Example:
        slab.badge("new", color="green")
    """
    bg = themes.color(color, 0)
    state.add(
        f'<span class="{bg} text-white text-xs font-semibold px-3 py-1 '
        f'rounded-full mx-6 my-2 inline-block">{label}</span>'
    )

def divider(margin: str = "8"):
    """Horizontal divider line.

    Args:
        margin: Vertical margin in Tailwind scale.

    Example:
        slab.divider()
    """
    state.add(f'<hr class="border-gray-200 my-{margin} mx-6" />')

def spacer(size: str = "8"):
    """Empty vertical space.

    Args:
        size: Height in Tailwind scale (4=1rem, 8=2rem, 16=4rem).

    Example:
        slab.spacer("12")
    """
    state.add(f'<div class="h-{size}"></div>')

def footer(text_content: str = "© 2025 Mi Empresa", bg: str = "gray"):
    """Page footer.

    Args:
        text_content: Footer text (HTML allowed).
        bg:           Background: "gray", "black", or "white".

    Example:
        slab.footer("© 2025 Slab · made with python")
    """
    bg_map = {
        "gray":  "bg-gray-100 text-gray-500",
        "black": "bg-gray-900 text-gray-400",
        "white": "bg-white text-gray-400",
    }
    cls = bg_map.get(bg, bg_map["gray"])
    state.add(f'<footer class="{cls} text-center text-sm py-8 px-6">{text_content}</footer>')

# New Components 1/2 0.2.0

def image():
    """Image component (coming soon)."""
    pass

def form():
    """Form component (coming soon)."""
    pass

def alert():
    """Alert / notification component (coming soon)."""
    pass

def table():
    """Table component (coming soon)."""
    pass

def pricing_card():
    """Pricing card component (coming soon)."""
    pass

def faq():
    """FAQ accordion component (coming soon)."""
    pass

# New Components 2/2 0.3.0

def faq():
    """FAQ accordion component (coming soon)."""
    pass

def gallery():
    """Image gallery component (coming soon)."""
    pass

def code_block():
    """Code block component (coming soon)."""
    pass

def stats_card():
    """Statistics card component (coming soon)."""
    pass

def video():
    """Video embed component (coming soon)."""
    pass

def timeline():
    """Timeline / roadmap component (coming soon)."""
    pass

"""*Autor: DEV-Gordon (Carlos Zarate) — https://github.com/DEV-Gordon/slabwebpy*"""