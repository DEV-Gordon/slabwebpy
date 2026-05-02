#!/usr/bin/env python3
"""
Example: Multi-page website with SlabWebPy.

Each page is a separate function with its own content and swp.build().
This approach is scalable: add more pages by creating new functions.

Run: python examples/example.py
Output: Creates dist/index.html, dist/contact.html, dist/docs.html
"""

import slabwebpy as swp

# Navbar links (compartido en todas las páginas)
NAVBAR_LINKS = [
    ("Home", "index.html"),
    ("Contact", "contact.html"),
    ("Docs", "docs.html"),
]

# ─────────────────────────────────────────────────────────────────────────────
# PÁGINA 1: HOME
# ─────────────────────────────────────────────────────────────────────────────

def build_home():
    """Construye la página de inicio."""
    
    swp.title("SlapWebPy - Static Sites with Python")
    swp.navbar("SlabWebPy", links=NAVBAR_LINKS, sticky=True)
    
    swp.hero(
        "Welcome to SlabWebPy",
        subtitle="Build static websites with Python",
        cta_label="Get Started",
        cta_url="contact.html",
        color="indigo",
    )
    
    swp.section(
        "Why Choose SlabWebPy?",
        subtitle="A powerful static site generator for Python developers",
        bg="gray"
    )
    
    swp.spacer("4")
    swp.badge("opensource", color="green")
    swp.badge("v0.3.0", color="blue")
    swp.badge("Python", color="yellow")
    swp.spacer("4")
    
    swp.grid(3)
    swp.card("Fast and Efficient", "Generate static sites quickly.", icon="⚡", color="yellow")
    swp.card("Easy to Use", "Get up and running quickly.", icon="🎯", color="green")
    swp.card("Flexible", "Tailor your site to your needs.", icon="🎨", color="blue")
    swp.card("Tailwind CSS", "Style easily with Tailwind.", icon="💅", color="purple")
    swp.card("Components", "Pre-built components included.", icon="🧩", color="red")
    swp.card("No Build Step", "Just Python and Tailwind CDN.", icon="🚀", color="indigo")
    swp.grid_end()
    
    swp.spacer("4")
    swp.button("View on GitHub", url="https://github.com/DEV-Gordon/slabwebpy", color="indigo")
    swp.spacer("4")
    swp.footer("© 2025 SlabWebPy. Made with ❤️ for Python developers.")
    
    swp.build("dist/index.html")
    print("✓ dist/index.html")


# ─────────────────────────────────────────────────────────────────────────────
# PÁGINA 2: CONTACT
# ─────────────────────────────────────────────────────────────────────────────

def build_contact():
    """Construye la página de contacto con formulario."""
    
    swp.title("Contact — SlabWebPy")
    swp.navbar("SlabWebPy", links=NAVBAR_LINKS, sticky=True)
    
    swp.hero(
        "Get in Touch",
        subtitle="We'd love to hear from you",
        color="indigo",
    )
    
    swp.form(
        title="Send us a message",
        description="Fill out the form and we'll get back to you soon.",
        color="indigo",
        columns=2,
        fields=[
            {"type": "text", "name": "name", "label": "Full Name", "placeholder": "John Doe", "required": True},
            {"type": "email", "name": "email", "label": "Email", "placeholder": "john@example.com", "required": True},
            {"type": "tel", "name": "phone", "label": "Phone", "placeholder": "+1 (555) 000-0000"},
            {"type": "select", "name": "subject", "label": "Subject", "options": ["General", "Bug", "Feature"], "required": True},
            {"type": "textarea", "name": "message", "label": "Message", "placeholder": "Your message...", "rows": 5, "required": True},
            {"type": "checkbox", "name": "subscribe", "label": "Subscribe to newsletter"},
        ],
        submit_label="Send Message",
    )
    
    swp.spacer("4")
    swp.footer("© 2025 SlabWebPy. Made with ❤️ for Python developers.")
    
    swp.build("dist/contact.html")
    print("✓ dist/contact.html")


# ─────────────────────────────────────────────────────────────────────────────
# PÁGINA 3: DOCS
# ─────────────────────────────────────────────────────────────────────────────

def build_docs():
    """Construye la página de documentación."""
    
    swp.title("Documentation — SlabWebPy")
    swp.navbar("SlabWebPy", links=NAVBAR_LINKS, sticky=True)
    
    swp.hero(
        "Documentation",
        subtitle="Learn how to build sites with SlabWebPy",
        color="indigo",
    )
    
    swp.section("Quick Start", bg="white")
    swp.text("Get up and running in 3 steps:", size="lg", bold=True)
    swp.spacer("3")
    
    swp.code_block(
        """import slabwebpy as swp
swp.title("My Site")
swp.hero("Welcome")
swp.build("dist/index.html")""",
        language="python",
        title="quick_start.py",
        line_numbers=True,
        theme="light",
    )
    
    swp.spacer("6")
    swp.section("Components", bg="gray")
    swp.alert("Check GitHub for full component docs.", kind="info", title="Learning Resources", dismissable=True)
    
    swp.spacer("4")
    swp.footer("© 2025 SlabWebPy. Made with ❤️ for Python developers.")
    
    swp.build("dist/docs.html")
    print("✓ dist/docs.html")


# ─────────────────────────────────────────────────────────────────────────────
# MAIN
# ─────────────────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    print("Building multi-page site...\n")
    
    build_home()      # Create dist/index.html
    build_contact()   # Create dist/contact.html
    build_docs()      # Create dist/docs.html
    
    print("\n✓ Site complete! Open dist/index.html in your browser.")
