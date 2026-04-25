import slabwebpy as swp

# Title and Navbar
swp.title("SlapWebPy - Static Sites with Python")

swp.navbar(
    "SlabWebPy",
    links=[
        ("Home", "#"), 
        ("Features", "#features"), 
        ("Contact", "#contact")
        ],)


# Hero Section
swp.hero(
    "Welcome to SlabWebPy",
    subtitle="Build static websites with Python",
    cta_label="Get Started",
    cta_url="#features",
    color="indigo", )

swp.section("Why Choose SlabWebPy?", 
            subtitle="A powerful static site generator for Python developers",
            bg="gray")

swp.spacer("4")

swp.badge("opensource", color="green")
swp.badge("v0.1.0", color="blue")
swp.badge("Python", color="yellow")

swp.spacer("4")

swp.grid(3)

swp.card(
    "Fast and Efficient",
    "SlabWebPy Generate static sites quickly with optimized build processes.",
    icon="🏃‍♀️",
    color="yellow",)

swp.card(
    "Easy to Use",
    "Get up and running quickly with our intuitive interface.",
    icon="🎯",
    color="green",)

swp.card(
    "Flexible and Customizable",
    "Tailor your site to your needs with our flexible design options.",
    icon="🎨",
    color="blue",)

swp.card(
    "Tailwind CSS Integration",
    "Easily style your site with Tailwind CSS classes.",
    icon="🎨",
    color="purple", )

swp.card(
    "Components",
    "Use pre-built components to speed up your development.",
    icon="🧩",
    color="red", )

swp.card(
    "No build",
    "No need npm or node, just Python and Tailwind CSS", 
    icon="⚡",
    color="cyan",
)

swp.grid_end()

swp.spacer("4")
swp.button("Repository", url="https://https://github.com/DEV-Gordon/slabwebpy", color="indigo")
swp.spacer("4")

swp.spacer("12")

swp.footer("© 2024 SlabWebPy. DevGordon. For all students and developers.")

# Build the site
swp.build("dist/index.html")