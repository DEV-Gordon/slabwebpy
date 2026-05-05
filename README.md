# SlabWebPy

**Build static websites with Python — no HTML, no CSS, no JavaScript required.**

SlabWebPy is a lightweight Python framework for students and developers who want to create real static websites using only Python. Write components, run one command, get a ready-to-deploy HTML file.

> 🎓 Built for learning. Designed so you never have to touch the web stack directly.

---

## Quick Start

```bash
git clone https://github.com/DEV-Gordon/slabwebpy.git
cd slabwebpy
python -m venv .venv && .venv\Scripts\activate  # Windows
# source .venv/bin/activate                     # Mac/Linux
```

Create your first site:

```python
# my_site.py
import slabwebpy as swp

swp.title("My First Site")
swp.navbar("MySite", links=[("Home", "#"), ("About", "#about")])
swp.hero("Hello, World!", subtitle="Built with Python", cta_label="Learn More", cta_url="#about")
swp.section("About", bg="gray")
swp.text("This site was built entirely in Python.", size="lg", align="center")
swp.footer("© 2025 My Site")

swp.build("dist/index.html")
```

```bash
python my_site.py
# ✓ Built -> dist/index.html
```

Open `dist/index.html` in your browser. Done.

---

## CLI

SlabWebPy includes a command-line tool for common workflows:

```bash
# Build a site from a Python script
slabwebpy build my_site.py

# Start a local preview server
slabwebpy serve --port 3000

# Scaffold a new project
slabwebpy init my-project
```

---

## Components

Every component is a Python function. Call them in order — SlabWebPy assembles the page top to bottom.

### Layout

| Component | Description |
|-----------|-------------|
| `navbar(brand, links, color, sticky)` | Top navigation bar |
| `hero(title, subtitle, cta_label, cta_url, color)` | Full-width banner section |
| `section(title, subtitle, bg, centered)` | Section wrapper with heading |
| `grid(columns, gap)` | Opens a responsive CSS grid (close with `grid_end()`) |
| `grid_end()` | Closes a grid |
| `divider(margin)` | Horizontal rule |
| `spacer(size)` | Vertical whitespace |
| `footer(text, bg)` | Page footer |

### Content

| Component | Description |
|-----------|-------------|
| `title(text)` | Sets the browser `<title>` |
| `text(content, size, color, align, bold, tag)` | Paragraph / heading text |
| `card(title, body, icon, color, variant)` | Content card |
| `badge(label, color)` | Small inline tag |
| `button(label, url, color, size, variant)` | Link button |
| `image(src, alt, size, rounded, caption, aspect, shadow, link)` | Responsive image with caption |
| `code_block(code, language, title, copy_button, line_numbers, theme)` | Syntax-highlighted code block |

### Interactive (pure HTML, no JS required)

| Component | Description |
|-----------|-------------|
| `alert(message, kind, title, dismissable, icon, timeout)` | Info / success / warning / error alert |
| `faq(items, title, color, bg, open_first)` | Accordion FAQ (`<details>` / `<summary>`) |
| `form(fields, action, submit_label, title, color, columns)` | Contact / data-entry form |

---

## Multi-Page Sites

Each page is a Python function. Share components like the navbar across pages:

```python
import slabwebpy as swp

NAV = [("Home", "index.html"), ("Docs", "docs.html"), ("Contact", "contact.html")]

def build_home():
    swp.title("Home — MySite")
    swp.navbar("MySite", links=NAV)
    swp.hero("Welcome", subtitle="A multi-page static site")
    swp.footer("© 2025 MySite")
    swp.build("dist/index.html")

def build_docs():
    swp.title("Docs — MySite")
    swp.navbar("MySite", links=NAV)
    swp.section("Documentation", bg="gray")
    swp.text("Getting started guide...")
    swp.footer("© 2025 MySite")
    swp.build("dist/docs.html")

if __name__ == "__main__":
    build_home()
    build_docs()
    print("Site built in dist/")
```

---

## Colors

All color-accepting components use these names:

`blue` `indigo` `purple` `pink` `red` `green` `yellow` `gray` `white` `black`

---

## Examples

The `examples/` folder includes ready-to-run demos:

| File | What it shows |
|------|---------------|
| `example.py` | Basic single-page site |
| `example_multipage.py` | Three-page site with shared navbar |
| `example_alert.py` | Alert variants (info, success, warning, error) |
| `example_code_block.py` | Code blocks with themes and line numbers |
| `example_faq_image.py` | FAQ accordion + image component |

Run any example:

```bash
python examples/example_multipage.py
# Open dist/index.html in your browser
```

---

## Project Structure

```
slabwebpy/
├── slabwebpy/
│   ├── __init__.py      # Public API
│   ├── components.py    # All visual components
│   ├── builder.py       # HTML assembly and file output
│   ├── state.py         # Internal page state
│   ├── themes.py        # Color and size system
│   ├── server.py        # Local dev server
│   └── cli.py           # Command-line interface
├── examples/            # Ready-to-run demos
├── dist/                # Generated output (git-ignored)
└── README.md
```

---

## Roadmap

Upcoming components: `table`, `pricing_card`, `stats_card`, `video`, `timeline`, `gallery`.

---

## License

MIT License — see [LICENSE](./LICENSE) for details.

---

*SlabWebPy — by [DEV-Gordon (Carlos Zarate)](https://github.com/DEV-Gordon)*
