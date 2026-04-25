# SlabWebPy

SlabWebPy is a lightweight Python framework for building static websites with reusable components, without relying on JavaScript to define page structure.

## Table of Contents

- Description
- Features
- Installation
- Quick Start
- Project Structure
- Roadmap
- Author
- License

## Description

The goal of SlabWebPy is to let you build static pages using only Python:

- Define components in Python.
- Generate the final HTML into an output file.
- Optionally run a local development server.

## Features

- Simple component API (navbar, hero, section, card, button, etc.).
- Builder to generate static HTML.
- Internal page state to assemble blocks.
- Basic theming system (colors, sizes, and backgrounds).
- Local development server for previewing pages.

## Installation

Clone the repository:

```bash
git clone https://github.com/DEV-Gordon/slabwebpy.git
cd slabwebpy
```

Optional (recommended): create a virtual environment.

```bash
python -m venv .venv
.venv\Scripts\activate
```

## Quick Start

Run the example as a module to avoid package import issues:

```bash
python -m slabwebpy.example
```

This generates the output file at:

- dist/index.html

## Project Structure

```text
slabwebpy/
  slabwebpy/
    __init__.py
    builder.py
    components.py
    example.py
    server.py
    state.py
    themes.py
  dist/
```

## Roadmap

| Area | What we already have (checklist) | What we will add (no checklist) |
|---|---|---|
| Core | - [x] Static HTML build<br>- [x] Internal block state<br>- [x] Public API from __init__.py | Official CLI (build, serve, new), packaging with pyproject.toml |
| Components | - [x] Navbar<br>- [x] Hero<br>- [x] Section<br>- [x] Grid + Grid End<br>- [x] Card<br>- [x] Button<br>- [x] Text<br>- [x] Badge<br>- [x] Divider<br>- [x] Spacer<br>- [x] Footer | Advanced components (FAQ, pricing table, testimonials, gallery, timeline) |
| Themes and Styling | - [x] Basic color palette<br>- [x] Button size scales<br>- [x] Predefined backgrounds | Design tokens, project-level custom themes, configurable dark mode |
| Local Development | - [x] Local server with serve()<br>- [x] Build before server start | Autoreload on file changes and DX improvements for faster development |
| Quality | - [x] Functional landing page example | Unit tests, linting, CI, release flow, and changelog |
| Sites and Content | - [x] Single-page generation | Multi-page support, reusable layouts, SEO metadata, and Markdown content support |
| Extensibility | - [x] Modular codebase split by file | Plugin/hook system and static asset pipeline |

## Author

- Name: DEV-Gordon (Carlos Zarate)
- GitHub: https://github.com/DEV-Gordon
- Project: https://github.com/DEV-Gordon/slabwebpy

## License

This project is licensed under the MIT License.
See the LICENSE file for details.
