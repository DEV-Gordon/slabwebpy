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

## Roadmap

### Implemented Now (v0.1.x)

Everything below is already available.

| Area | Current Status | Included |
|---|---|---|
| Core Engine | Implemented | - [x] Static HTML build engine<br>- [x] Internal page state management<br>- [x] Public package API |
| Components | Implemented | - [x] Base component system<br>- [x] Navbar, Hero, Section, Grid, Card, Button, Text, Badge, Divider, Spacer, Footer |
| Styling | Implemented | - [x] Theme helpers and style utilities |
| Development | Implemented | - [x] Local development server |
| Example | Implemented | - [x] Functional landing page example |

### Planned (Not Implemented Yet)

Everything below is planned for future versions and is not available yet.

| Horizon | Version / Focus | Planned Additions |
|---|---|---|
| Short Term | v0.2.0 - Usability and Product Foundation | Official packaging with pyproject.toml; editable local install flow; initial CLI commands (build, serve, new); component parameter validations; clearer and more actionable error messages; improved and expanded official examples |
| Short Term | v0.2.1 - Quality and Reliability | Unit tests for build and internal state; render tests for core components; formatting and linting conventions; contributor guide |
| Mid Term | v0.3.0 - Framework Scalability | Multi-page support (home, about, contact, etc.); reusable layouts (header, footer, global shell); centralized site configuration |
| Mid Term | v0.3.1 - Content and SEO | SEO metadata support (title, description, og tags); favicon and social cards support; optional Markdown content workflow |
| Mid Term | v0.4.0 - Ecosystem and Extensibility | Plugin/hook system; static asset pipeline (images, fonts, css); advanced components (FAQ, pricing table, testimonials, gallery) |

### Backlog (No Scheduled Version)

- Configurable dark mode
- Starter templates
- Basic internationalization
- Incremental page generation
- CI integration for automated releases

### Prioritization Criteria

- End-user impact
- Implementation effort
- Reduction of common usage errors
- Foundation value for future features

### Progress Metrics

- Time to create a functional landing page
- Number of stable components
- Test coverage
- Issues closed per version
- Average build time

## Author

- Name: DEV-Gordon (Carlos Zarate)
- GitHub: https://github.com/DEV-Gordon
- Project: https://github.com/DEV-Gordon/slabwebpy

## License

This project is licensed under the MIT License.
See LICENSE for details.
