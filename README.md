# SlabWebPy

SlabWebPy is a lightweight Python framework for building static websites with reusable components.

## Table of Contents

- Overview
- Features
- Installation
- Quick Start
- Project Structure
- Roadmap
- Author
- License

## Overview

SlabWebPy helps you create static pages using Python only:

- Define page structure with Python components.
- Build a final static HTML file.
- Optionally preview it with a local development server.

## Features

- Simple component API (navbar, hero, section, card, button, text, and more).
- Static HTML builder.
- Internal page state for block composition.
- Basic theme utilities (colors, sizes, backgrounds).
- Local dev server support.

## Installation

```bash
git clone https://github.com/DEV-Gordon/slabwebpy.git
cd slabwebpy
```

Optional but recommended:

```bash
python -m venv .venv
.venv\Scripts\activate
```

## Quick Start

Run the example as a module:

```bash
python -m slabwebpy.example
```

Generated output:

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



## License

This project is licensed under the MIT License.
See LICENSE for details.
