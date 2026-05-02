# Components for SlabWebPy
"""
slab.components — All visual components.
Each function appends HTML to the current page state.
"""

import html
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

def image(
    src: str,
    alt: str = "",
    size: str = "full",
    rounded: str = "md",
    align: str = "center",
    caption: str = "",
    aspect: str = "",
    shadow: bool = False,
    link: str = "",):

    """Image component with optional caption and link.
    Args:
        src:     URL or relative path to the image.
        alt:     Alternative text (recommended for accessibility).
        size:    Width of the image: "full", "xl", "lg", "md", "sm", "xs".
        rounded: Corner rounding: "none", "sm", "md", "lg", "xl", "full".
        align:   Horizontal alignment: "left", "center", "right".
        caption: Optional text shown below the image.
        aspect:  Aspect ratio container: "video" (16:9), "square", "portrait" (4:5).
                    Leave empty to use the image's natural dimensions.
        shadow:  Add a soft shadow if True.
        link:    Wrap the image in an anchor tag if provided.
    Example:
        swp.image(
            "https://routetest/800/400",
            alt="A random photo",
            size="lg",
            rounded="xl",
            caption="A placeholder image",
            shadow=True,
        )
        swp.image(
            "hero.jpg",
            alt="Hero banner",
            size="full",
            aspect="video",
            rounded="lg",
        )
    """
    
    # Sizes
    size_map = {
        "full": "w-full",
        "xl": "max-w-4xl",
        "lg": "max-w-2xl",
        "md": "max-w-xl",
        "sm": "max-w-sm",
        "xs": "max-w-xs",
    }

    # Rounded corners
    rounded_map = {
        "none": "rounded-none",
        "sm": "rounded-sm",
        "md": "rounded-md",
        "lg": "rounded-lg",
        "xl": "rounded-xl",
        "full": "rounded-full",
    }

    # Aspect ratios map
    aspect_map = {
        "video": "aspect-video",
        "square": "aspect-square",
        "portrait": "aspect-[4/5]",
    }

    # alignment map for the container
    align_map = {
        "left": "mr-auto",
        "center": "mx-auto",
        "right": "ml-auto",
    }

    w_cls = size_map.get(size, "w-full")
    r_cls = rounded_map.get(rounded, "rounded-md")
    a_cls = align_map.get(align, "mx-auto")
    shadow_cls = "shadow-lg" if shadow else ""
    aspect_cls = aspect_map.get(aspect, "")

    # inner <img> tag
    img_cls = f"w-full h-full object-cover {r_cls} {shadow_cls}".strip()
    
    # Wrap in aspect ratio container if needed
    if aspect_cls:
        inner = (
            f'<div class="{aspect_cls} overflow-hidden {r_cls} {shadow_cls}">'
            f'<img src="{src}" alt="{alt}" class="w-full h-full object-cover" loading="lazy" />'
            f'</div>'
        )
    else:
        inner = f'<img src="{src}" alt="{alt}" class="{img_cls}" loading="lazy" />'

    # Wrap in link if provided
    if link:
        inner = (
            f'<a href="{link}" target="_blank" rel="noopener noreferrer" '
            f'class="block hover:opacity-90 transition">'
            f'{inner}</a>'
        )

    # Caption
    caption_html = ""
    if caption:
        caption_html = (
            f'<p class="text-gray-400 text-sm text-center mt-2 italic">{caption}</p>'
        )

    state.add(
        f'<div class="px-6 py-4">'
        f'<figure class="{w_cls} {a_cls}">'
        f'{inner}'
        f'{caption_html}'
        f'</figure>'
        f'</div>'
    )

def form(
    fields: list[dict],
    action: str = "#",
    method: str = "post",
    submit_label: str = "Send",
    title: str = "",
    description: str = "",
    color: str = "indigo",
    bg: str = "white",
    columns: int = 1,
):
    """Contact / data-entry form component.

    Args:
        fields:       List of field dicts. Each dict supports:
                        "type"        — "text" | "email" | "password" | "number" | "tel" |
                                        "url" | "date" | "textarea" | "select" | "checkbox" | "radio"
                        "name"        — HTML name attribute (required for all).
                        "label"       — Visible label text.
                        "placeholder" — Placeholder for text inputs / textarea.
                        "required"    — True to mark field as required (adds * to label).
                        "rows"        — Number of visible rows for textarea (default: 4).
                        "options"     — List of strings for select / radio inputs.
                        "value"       — Pre-filled default value.
                        "helper"      — Small hint text shown below the field.
                        "half"        — True to make this field half-width in a 2-col layout.
        action:       Form action URL.
        method:       HTTP method: "post" or "get".
        submit_label: Text inside the submit button.
        title:        Optional heading above the form.
        description:  Optional subtext below the title.
        color:        Accent color for the submit button and focus rings.
        bg:           Background of the form card: "white", "gray", "dark".
        columns:      Layout columns for fields: 1 or 2.

    Example:
        swp.form(
            title="Contact us",
            description="We'll get back to you within 24 hours.",
            color="indigo",
            columns=2,
            fields=[
                {"type": "text",     "name": "name",    "label": "Full name",
                "placeholder": "Jane Doe", "required": True},
                {"type": "email",    "name": "email",   "label": "Email",
                "placeholder": "jane@example.com", "required": True},
                {"type": "tel",      "name": "phone",   "label": "Phone",
                "placeholder": "+1 555 000 0000"},
                {"type": "select",   "name": "plan",    "label": "Plan",
                "options": ["Free", "Pro", "Teams"], "required": True},
                {"type": "textarea", "name": "message", "label": "Message",
                "placeholder": "How can we help?", "rows": 5,
                "helper": "Minimum 20 characters."},
                {"type": "checkbox", "name": "tos",     "label": "I accept the Terms of Service",
                "required": True},
            ],
            submit_label="Send message",
        )
    """

    # palette
    btn_bg    = themes.color(color, 0)           # e.g. "bg-indigo-600"
    btn_hover = themes.color(color, 3)           # e.g. "hover:bg-indigo-700"
    ring      = f"focus:ring-2 focus:ring-{color}-400 focus:outline-none"

    bg_map = {
        "white": ("bg-white",   "text-gray-900", "text-gray-500", "text-gray-700",
                    "bg-white border-gray-200 text-gray-900",
                    "bg-white border-gray-200 text-gray-900"),
        "gray":  ("bg-gray-50", "text-gray-900", "text-gray-500", "text-gray-700",
                    "bg-white border-gray-200 text-gray-900",
                    "bg-white border-gray-200 text-gray-900"),
        "dark":  ("bg-gray-900","text-white",    "text-gray-400", "text-gray-300",
                    "bg-gray-800 border-gray-700 text-white placeholder-gray-500",
                    "bg-gray-800 border-gray-700 text-white"),
    }
    card_bg, title_col, desc_col, label_col, input_cls_base, select_cls_base = (
        bg_map.get(bg, bg_map["white"])
    )

    # shared input classes
    base_input = (
        f"w-full border rounded-lg px-4 py-2.5 text-sm transition "
        f"{input_cls_base} {ring} "
        f"disabled:opacity-50 disabled:cursor-not-allowed"
    )
    base_select = (
        f"w-full border rounded-lg px-4 py-2.5 text-sm transition "
        f"appearance-none cursor-pointer "
        f"{select_cls_base} {ring}"
    )

    # header 
    header_html = ""
    if title:
        header_html += (
            f'<h2 class="{title_col} text-2xl font-bold mb-1">{title}</h2>'
        )
    if description:
        header_html += (
            f'<p class="{desc_col} text-sm mb-6">{description}</p>'
        )
    if header_html:
        header_html = f'<div class="mb-6">{header_html}</div>'

    # field builder 
    def _label(field: dict) -> str:
        lbl  = field.get("label", "")
        req  = field.get("required", False)
        name = field.get("name", "")
        star = f' <span class="text-red-500">*</span>' if req else ""
        return (
            f'<label for="{name}" '
            f'class="{label_col} text-sm font-medium block mb-1">'
            f'{lbl}{star}</label>'
        )

    def _helper(field: dict) -> str:
        hint = field.get("helper", "")
        if not hint:
            return ""
        return f'<p class="text-gray-400 text-xs mt-1">{hint}</p>'

    def _required_attr(field: dict) -> str:
        return 'required' if field.get("required") else ''

    def _build_field(field: dict) -> str:
        ftype = field.get("type", "text")
        name  = field.get("name", "")
        ph    = field.get("placeholder", "")
        val   = field.get("value", "")
        req   = _required_attr(field)

        # textarea
        if ftype == "textarea":
            rows = field.get("rows", 4)
            return (
                f'{_label(field)}'
                f'<textarea id="{name}" name="{name}" rows="{rows}" '
                f'placeholder="{ph}" {req} '
                f'class="{base_input} resize-y min-h-[80px]">'
                f'{val}</textarea>'
                f'{_helper(field)}'
            )

        # select 
        if ftype == "select":
            options = field.get("options", [])
            opts_html = "".join(
                f'<option value="{o}" {"selected" if o == val else ""}>{o}</option>'
                for o in options
            )
            return (
                f'{_label(field)}'
                f'<div class="relative">'
                f'<select id="{name}" name="{name}" {req} '
                f'class="{base_select}">'
                f'<option value="" disabled {"selected" if not val else ""}>'
                f'{ph or "Choose an option"}</option>'
                f'{opts_html}'
                f'</select>'
                # custom chevron
                f'<span class="pointer-events-none absolute inset-y-0 right-3 '
                f'flex items-center text-gray-400 text-xs">▾</span>'
                f'</div>'
                f'{_helper(field)}'
            )

        # checkbox 
        if ftype == "checkbox":
            lbl  = field.get("label", "")
            req  = _required_attr(field)
            return (
                f'<label class="flex items-start gap-3 cursor-pointer group">'
                f'<input type="checkbox" id="{name}" name="{name}" {req} '
                f'class="mt-0.5 h-4 w-4 rounded border-gray-300 '
                f'accent-{color}-600 cursor-pointer" />'
                f'<span class="{label_col} text-sm">{lbl}</span>'
                f'</label>'
                f'{_helper(field)}'
            )

        # radio group 
        if ftype == "radio":
            options = field.get("options", [])
            radios  = ""
            for opt in options:
                checked = "checked" if opt == val else ""
                radios += (
                    f'<label class="flex items-center gap-2 cursor-pointer">'
                    f'<input type="radio" name="{name}" value="{opt}" {checked} '
                    f'class="h-4 w-4 accent-{color}-600 cursor-pointer" />'
                    f'<span class="{label_col} text-sm">{opt}</span>'
                    f'</label>'
                )
            return (
                f'{_label(field)}'
                f'<div class="flex flex-col gap-1.5 mt-1">{radios}</div>'
                f'{_helper(field)}'
            )

        # all other <input> types 
        return (
            f'{_label(field)}'
            f'<input type="{ftype}" id="{name}" name="{name}" '
            f'placeholder="{ph}" value="{val}" {req} '
            f'class="{base_input}" />'
            f'{_helper(field)}'
        )

    # field layout 
    if columns == 2:
        # Two-column grid; individual fields can opt into half-width
        grid_items = []
        for f in fields:
            ftype = f.get("type", "text")
            # checkboxes / radios always span full width for clarity
            full = ftype in ("checkbox", "radio", "textarea") or not f.get("half", True)
            col_span = "col-span-2" if full else "col-span-1"
            grid_items.append(
                f'<div class="{col_span}">{_build_field(f)}</div>'
            )
        fields_html = (
            f'<div class="grid grid-cols-2 gap-x-6 gap-y-5">'
            f'{"".join(grid_items)}'
            f'</div>'
        )
    else:
        fields_html = (
            f'<div class="flex flex-col gap-5">'
            + "".join(f'<div>{_build_field(f)}</div>' for f in fields)
            + "</div>"
        )

    # submit 
    submit_html = (
        f'<div class="mt-6">'
        f'<button type="submit" '
        f'class="{btn_bg} {btn_hover} text-white font-semibold '
        f'px-6 py-2.5 rounded-lg transition text-sm w-full sm:w-auto">'
        f'{submit_label}'
        f'</button>'
        f'</div>'
    )

    #  assemble 
    state.add(
        f'<section class="{card_bg} py-16 px-6">'
        f'<div class="max-w-2xl mx-auto">'
        f'<form action="{action}" method="{method}" novalidate>'
        f'{header_html}'
        f'{fields_html}'
        f'{submit_html}'
        f'</form>'
        f'</div>'
        f'</section>'
    )

def alert(
    message: str,
    kind: str = "info",              # "info" | "success" | "warning" | "error"
    title: str | None = None,
    dismissable: bool = False,
    icon: bool = True,
    timeout: int | None = None,      # seconds, optional auto-dismiss
    allow_html: bool = False,
    classes: str = "",
):
    """Alert / notification component with optional dismiss and auto-timeout.

    Args:
        message:     Main alert text (escaped by default for security).
        kind:        Alert type: "info", "success", "warning", "error".
                     Determines color and icon.
        title:       Optional heading above the message (escaped by default).
        dismissable: Show a close button if True (uses inline onclick).
        icon:        Display an SVG icon matching the kind if True.
        timeout:     Auto-dismiss after N seconds (optional, uses inline JS).
        allow_html:  Allow raw HTML in message/title if True (XSS risk if user input).
        classes:     Extra CSS classes for the container.

    Example:
        swp.alert(
            "Your changes have been saved.",
            kind="success",
            title="Success",
            icon=True,
            dismissable=True,
        )
        swp.alert(
            "This action cannot be undone.",
            kind="warning",
            dismissable=True,
            timeout=5,
        )
    """
    # map logical kinds to theme color names
    kind_map = {
        "info": "indigo",
        "success": "green",
        "warning": "yellow",
        "error": "red",
    }
    color_name = kind_map.get(kind, "indigo")

    # palette from themes
    text_accent = themes.color(color_name, 1)  # e.g. "text-indigo-600"
    border_accent = themes.color(color_name, 2)  # e.g. "border-indigo-600"

    # semantic a11y
    aria_live = "assertive" if kind == "error" else "polite"
    role = "alert"

    # escape unless allow_html
    def esc(s: str) -> str:
        return s if allow_html else html.escape(s)

    title_html = f'<div class="font-semibold {text_accent} mb-1">{esc(title)}</div>' if title else ""
    msg_html = esc(message)

    # simple icon set (uses currentColor so it follows text_accent)
    icons = {
        "info": '<svg class="w-5 h-5" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-width="2" stroke-linecap="round" stroke-linejoin="round" d="M13 16h-1v-4h-1m1-4h.01M12 2a10 10 0 100 20 10 10 0 000-20z"/></svg>',
        "success": '<svg class="w-5 h-5" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-width="2" stroke-linecap="round" stroke-linejoin="round" d="M5 13l4 4L19 7"/></svg>',
        "warning": '<svg class="w-5 h-5" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-width="2" stroke-linecap="round" stroke-linejoin="round" d="M10.29 3.86L1.82 18a2 2 0 001.71 3h16.94a2 2 0 001.71-3L13.71 3.86a2 2 0 00-3.42 0zM12 9v4M12 17h.01"/></svg>',
        "error": '<svg class="w-5 h-5" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-width="2" stroke-linecap="round" stroke-linejoin="round" d="M6 18L18 6M6 6l12 12"/></svg>',
    }
    icon_html = f'<div class="{text_accent} mr-3 flex-shrink-0">{icons.get(kind)}</div>' if icon else ""

    # dismiss button
    dismiss_html = ""
    if dismissable:
        dismiss_html = (
            f'<button type="button" aria-label="Dismiss alert" '
            f'class="ml-auto text-gray-400 hover:text-gray-600 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-gray-300 rounded" '
            f'onclick="this.closest(\'.swp-alert\').style.display=\'none\'" '
            f'tabindex="0">'
            f'<svg class="w-5 h-5" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-width="2" stroke-linecap="round" stroke-linejoin="round" d="M6 18L18 6M6 6l12 12"/></svg>'
            f'</button>'
        )

    # optional timeout JS (in milliseconds)
    timeout_js = ""
    if timeout and isinstance(timeout, int) and timeout > 0:
        alert_id = f"swp-alert-{id(message) % 1000000}"
        timeout_js = f'<script>setTimeout(()=>{{var el=document.getElementById(\'{alert_id}\');if(el)el.style.display=\'none\';}},(timeout)*1000)</script>'.replace("(timeout)", str(timeout))

    state.add(
        f'<div class="flex justify-center px-6 py-4">'
        f'<div id="swp-alert-{id(message) % 1000000}" class="swp-alert bg-white border rounded-md p-4 flex items-start gap-3 border {border_accent} max-w-2xl w-full {classes}" role="{role}" aria-live="{aria_live}">'
        f'{icon_html}'
        f'<div class="min-w-0 flex-1">'
        f'{title_html}'
        f'<div class="text-sm text-gray-700">{msg_html}</div>'
        f'</div>'
        f'{dismiss_html}'
        f'</div>'
        f'</div>'
        f'{timeout_js}'
    )

def table():
    """Table component (coming soon)."""
    pass

def faq(
    items: list[dict],
    title: str = "",
    color: str = "indigo",
    bg: str = "white",
    divided: bool = True,
    open_first: bool = False,
):
    """FAQ accordion component. Uses native HTML <details>/<summary> — no JavaScript needed.

    Args:
        items:      List of dicts with keys "q" (question) and "a" (answer).
                    "a" supports basic HTML (links, <strong>, <em>, etc.).
        title:      Optional section heading above the FAQ list.
        color:      Accent color for the summary arrow and focus ring.
        bg:         Background of the section: "white", "gray", "dark".
        divided:    Show a divider line between items if True.
        open_first: Expand the first item by default if True.

    Example:
        swp.faq(
            title="Frequently Asked Questions",
            color="indigo",
            items=[
                {
                    "q": "Do I need Node.js or npm?",
                    "a": "No. SlabWebPy uses only Python and the Tailwind CDN. "
                        "No build step required.",
                },
                {
                    "q": "Can I deploy the output to GitHub Pages?",
                    "a": "Yes — the generated <code>dist/index.html</code> is a "
                        "standalone static file. Drop it anywhere.",
                },
                {
                    "q": "Is it free?",
                    "a": 'It is <a href="https://github.com/DEV-Gordon/slabwebpy" '
                        'class="text-indigo-600 underline">open source</a> under the MIT License.',
                },
            ],
            open_first=True,
        )
    """

    # Colors
    accent_text  = themes.color(color, 1)      # e.g. "text-indigo-600"
    accent_hover = themes.color(color, 3)      # e.g. "hover:bg-indigo-700"  (used for focus ring)

    # Background
    bg_map = {
        "white": ("bg-white",    "text-gray-900", "text-gray-600"),
        "gray":  ("bg-gray-50",  "text-gray-900", "text-gray-600"),
        "dark":  ("bg-gray-900", "text-white",    "text-gray-300"),
    }
    bg_cls, title_color, body_color = bg_map.get(bg, bg_map["white"])
    divider_cls = "border-b border-gray-100" if divided else ""
    dark_divider = "border-b border-gray-700" if bg == "dark" else divider_cls

    # Optional heading
    title_html = ""
    if title:
        title_html = (
            f'<h2 class="{title_color} text-2xl font-bold text-center mb-8">{title}</h2>'
        )

    # Build <details> items
    # The CSS triangle rotates on [open] using a pure-CSS trick (no JS).
    # The marker list-style is removed and a custom SVG chevron is injected via
    # a ::before pseudo-element encoded as a data URI — but since we're writing
    # inline HTML we use a Unicode arrow and rotate it with a <span>.
    detail_items = []
    for idx, item in enumerate(items):
        q = item.get("q", "")
        a = item.get("a", "")
        open_attr = "open" if (open_first and idx == 0) else ""
        dark_text = "text-white" if bg == "dark" else "text-gray-900"
        dark_body = "text-gray-300" if bg == "dark" else "text-gray-600"
        dark_bg   = "hover:bg-gray-800" if bg == "dark" else "hover:bg-gray-50"

        detail_items.append(f"""
        <details {open_attr} class="group {dark_divider}">
        <summary class="flex items-center justify-between gap-4 py-4 px-2
                        cursor-pointer list-none select-none rounded-lg
                        {dark_bg} transition
                        focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-{color}-400">
            <span class="{dark_text} text-base font-medium">{q}</span>
            <span class="{accent_text} text-lg font-bold flex-shrink-0
                        transition-transform duration-200 group-open:rotate-45">+</span>
        </summary>
        <div class="pb-4 px-2">
            <p class="{dark_body} text-sm leading-relaxed">{a}</p>
        </div>
        </details>""")

    items_html = "\n".join(detail_items)

    state.add(
        f'<section class="{bg_cls} py-16 px-6">'
        f'<div class="max-w-3xl mx-auto">'
        f'{title_html}'
        f'<div class="divide-y divide-gray-100">'
        f'{items_html}'
        f'</div>'
        f'</div>'
        f'</section>'
    )

def code_block(
    code: str,
    language: str = "python",
    title: str = "",
    copy_button: bool = True,
    line_numbers: bool = False,
    theme: str = "light",
):
    """Code block / snippet display with optional syntax language label, copy button, and line numbers.

    Args:
        code:         The source code to display (will be escaped for security).
        language:     Programming language name (python, javascript, html, etc.).
                        Used for labeling; syntax highlighting requires highlight.js CDN integration.
        title:        Optional filename or label shown above the code block.
        copy_button:  Show a "Copy" button if True (uses inline onclick).
        line_numbers: Display line numbers on the left if True.
        theme:        Background theme: "light" or "dark".

    Example:
        swp.code_block(
            '''def hello(name: str):
    print(f"Hello, {name}!")
hello("SlabWebPy")''',
            language="python",
            title="hello.py",
            copy_button=True,
            line_numbers=True,
            theme="dark",
        )
    """
    # Escape code for security
    escaped_code = html.escape(code)

    # Theme mapping
    theme_map = {
        "light": ("bg-gray-50", "text-gray-900", "border-gray-200", "bg-gray-100", "text-gray-400"),
        "dark": ("bg-gray-900", "text-gray-100", "border-gray-700", "bg-gray-800", "text-gray-500"),
    }
    bg_cls, text_cls, border_cls, header_bg, line_num_cls = theme_map.get(theme, theme_map["light"])

    # Header with title and copy button
    header_html = ""
    if title or copy_button:
        title_html = f'<span class="font-mono text-sm font-semibold">{html.escape(title)}</span>' if title else ""
        copy_btn_html = ""
        if copy_button:
            code_id = f"swp-code-{id(code) % 1000000}"
            copy_btn_html = (
                f'<button type="button" aria-label="Copy code" '
                f'class="ml-auto px-3 py-1.5 text-xs font-medium rounded bg-gray-600 hover:bg-gray-700 text-white transition focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-gray-500" '
                f'onclick="var el=document.getElementById(\'{code_id}\');var text=el.textContent;navigator.clipboard.writeText(text).then(()=>{{this.textContent=\'Copied!\';setTimeout(()=>{{this.textContent=\'Copy\'}},2000)}});">'
                f'Copy</button>'
            )
        header_html = f'<div class="{header_bg} border-b {border_cls} px-4 py-3 flex items-center gap-2">{title_html}{copy_btn_html}</div>'

    # Build lines with optional line numbers
    lines = escaped_code.split('\n')
    if line_numbers:
        line_items = []
        for i, line in enumerate(lines, 1):
            line_num_html = f'<span class="{line_num_cls} inline-block w-8 text-right pr-4">{i}</span>'
            line_items.append(f'<div>{line_num_html}{line or " "}</div>')
        code_html = '\n'.join(line_items)
    else:
        code_html = escaped_code

    # Code container
    code_id = f"swp-code-{id(code) % 1000000}"
    state.add(
        f'<div class="flex justify-center px-6 py-4">'
        f'<div class="w-full max-w-4xl rounded-lg overflow-hidden border {border_cls} shadow-sm">'
        f'{header_html}'
        f'<pre id="{code_id}" class="{bg_cls} {text_cls} p-4 overflow-x-auto font-mono text-sm leading-relaxed"><code>{code_html}</code></pre>'
        f'</div>'
        f'</div>'
    )

# New Components 2/2 0.3.0
def pricing_card():
    """Pricing card component (coming soon)."""
    pass

def gallery():
    """Image gallery component (coming soon)."""
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