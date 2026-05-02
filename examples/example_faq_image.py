import slabwebpy as swp

swp.title("SlabWebPy - Image + FAQ Example")

swp.navbar(
    "SlabWebPy",
    links=[
        ("Home", "#"),
        ("Gallery", "#gallery"),
        ("FAQ", "#faq"),
    ],
)

swp.hero(
    "Image and FAQ Demo",
    subtitle="Simple page using image and FAQ components",
    cta_label="See FAQ",
    cta_url="#faq",
    color="indigo",
)

swp.section("Image", subtitle="External image with caption", bg="gray")

swp.image(
    "https://images.unsplash.com/photo-1500530855697-b586d89ba3ee?auto=format&fit=crop&w=1600&q=80",
    alt="Forest landscape",
    size="lg",
    rounded="xl",
    caption="Photo from Unsplash",
    shadow=True,
    aspect="video",
)

swp.spacer("1")

swp.section("FAQ", subtitle="Common questions", bg="white")

swp.faq(
    title="Frequently Asked Questions",
    color="indigo",
    items=[
        {
            "q": "Do I need Node.js or npm?",
            "a": "No. SlabWebPy uses only Python and the Tailwind CDN.",
        },
        {
            "q": "Can I use external images?",
            "a": "Yes. Any public image URL works with the image component.",
        },
        {
            "q": "Can I deploy the output to GitHub Pages?",
            "a": "Yes. The generated HTML file is static and portable.",
        },
    ],
    open_first=True,
)

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

swp.footer("© 2026 SlabWebPy")

swp.build("dist/example_faq_image.html")
