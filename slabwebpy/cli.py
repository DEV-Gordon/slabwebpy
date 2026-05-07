#!/usr/bin/env python3
"""
SlabWebPy CLI — Command-line interface for building sites.

Usage:
    slabwebpy build <script.py> [--output OUTPUT.html]
    slabwebpy serve [--port 8000]
    slabwebpy init <project_name>
"""

import argparse
import importlib
import sys
from pathlib import Path
from . import server


def build_command(args):
    """execute a script to build a site."""
    script = Path(args.script)
    
    if not script.exists():
        print(f"Error: Script '{script}' not found.")
        sys.exit(1)
    
    print(f"Building {script}...")

    # Allow --output to override any swp.build(...) call in the script.
    slabwebpy = importlib.import_module("slabwebpy")
    original_build = slabwebpy.build

    if args.output:
        output_path = str(Path(args.output))

        def build_override(*_args, **_kwargs):
            return original_build(output_path)

        slabwebpy.build = build_override

    try:
        with open(script, encoding="utf-8") as f:
            code = f.read()
            exec(code, {"__name__": "__main__"})
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)
    finally:
        slabwebpy.build = original_build

def serve_command(args):
    """start a local server to preview the site."""
    port = args.port or 3000
    directory = args.directory or "dist"
    
    print(f"Serving {directory} on http://localhost:{port}")
    server.serve(output=str(Path(directory) / "index.html"), port=port, open_browser=True, rebuild=False)


def init_command(args):
    """Create a new SlabWebPy project."""
    project_name = args.project_name
    project_dir = Path(project_name)
    
    if project_dir.exists():
        print(f"Error: Directory '{project_name}' already exists.")
        sys.exit(1)
    
    project_dir.mkdir()
    (project_dir / "pages.py").write_text(STARTER_TEMPLATE, encoding="utf-8")
    (project_dir / ".gitignore").write_text("dist/\n__pycache__/\n*.pyc\n", encoding="utf-8")
    
    print(f"✓ Project '{project_name}' created!")
    print(f"  Run: cd {project_name} && python pages.py")


STARTER_TEMPLATE = '''#!/usr/bin/env python3
"""My SlabWebPy site."""

import slabwebpy as swp

# Title
swp.title("My Site")

# Navbar
swp.navbar("MyBrand", links=[("Home", "#"), ("About", "#")])

# Hero
swp.hero("Welcome!", subtitle="Built with SlabWebPy", color="indigo")

# Section
swp.section("Features", bg="gray")
swp.card("Fast", "Generate sites quickly", icon="⚡", color="yellow")
swp.card("Easy", "Simple Python API", icon="🎯", color="green")

# Footer
swp.footer("© 2025 My Site")

# Build
swp.build("dist/index.html")
print("✓ Built: dist/index.html")
'''


def main():
    """Start the CLI."""
    parser = argparse.ArgumentParser(
        description="SlabWebPy — Build static sites with Python",
        prog="slabwebpy",
    )
    
    subparsers = parser.add_subparsers(dest="command", help="Commands")
    
    # command: build
    build_parser = subparsers.add_parser("build", help="Build a site from a Python script")
    build_parser.add_argument("script", help="Python script to execute")
    build_parser.add_argument("-o", "--output", help="Output directory (default: dist/)")
    build_parser.set_defaults(func=build_command)
    
    # command: serve
    serve_parser = subparsers.add_parser("serve", help="Serve local preview")
    serve_parser.add_argument("-p", "--port", type=int, default=3000, help="Port (default: 3000)")
    serve_parser.add_argument("-d", "--directory", default="dist", help="Directory to serve")
    serve_parser.set_defaults(func=serve_command)
    
    # command: init
    init_parser = subparsers.add_parser("init", help="Create a new SlabWebPy project")
    init_parser.add_argument("project_name", help="Project name")
    init_parser.set_defaults(func=init_command)
    
    # Parse args
    args = parser.parse_args()
    
    if not args.command:
        parser.print_help()
        sys.exit(0)
    
    args.func(args)


if __name__ == "__main__":
    main()