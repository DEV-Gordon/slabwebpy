# Builder and write final html file

"""
slabweb.builder — build() functions.
Assembles the final HTML.
"""

from pathlib import Path

from . import state

# html template with Tailwind CSS and basic styling
_HTML_TEMPLATE = """\
<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>{title}</title>
  <script src="https://cdn.tailwindcss.com"></script>
  <style>
    html {{ scroll-behavior: smooth; }}
    body {{ font-family: 'Segoe UI', system-ui, sans-serif; }}
  </style>
</head>
<body class="bg-white text-gray-900 antialiased">
{body}
</body>
</html>"""

# Build function to generate the final HTML file
def build(output: str = "index.html"):
    
    """Generates and writes the final HTML file.

    Args:
        output: File path to write (e.g. "dist/index.html").

    Example:
        slab.build("dist/index.html")
    """

    Path(output).parent.mkdir(parents=True, exist_ok=True)

    body = "\n".join(state.get_blocks())
    html = _HTML_TEMPLATE.format(title=state.get_title(), body=body)

    Path(output).write_text(html, encoding="utf-8")
    state.reset()
    print(f"Ok,  Built -> {output}")
