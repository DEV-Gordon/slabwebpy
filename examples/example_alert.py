#!/usr/bin/env python3
"""
Example showcasing the alert() component with all 4 kinds: info, success, warning, error.
Demonstrates dismissable alerts, optional timeout, and custom titles.

Run: python -m slabwebpy.example_alert
Output: dist/example_alert.html
"""

import slabwebpy as swp

# Title
swp.title("SlabWebPy — Alert Component Examples")

# Navbar
swp.navbar("SlabWebPy", links=[("Home", "#"), ("Docs", "#")])

# Hero
swp.hero(
    "Alert Component",
    subtitle="4 visual kinds with optional dismiss and auto-timeout",
    cta_label="View Docs",
    color="indigo",
)

# Section: Info Alert
swp.section("Info Alert", subtitle="For informational messages", bg="white")
swp.spacer("4")
swp.alert(
    "This is an informational message. Use it to provide helpful context or instructions.",
    kind="info",
    title="Information",
    icon=True,
    dismissable=True,
)
swp.spacer("6")

# Section: Success Alert
swp.section("Success Alert", subtitle="For confirmations and positive outcomes", bg="gray")
swp.spacer("4")
swp.alert(
    "Your changes have been saved successfully.",
    kind="success",
    title="Success!",
    icon=True,
    dismissable=True,
)
swp.spacer("6")

# Section: Warning Alert
swp.section("Warning Alert", subtitle="For cautions and potential issues", bg="white")
swp.spacer("4")
swp.alert(
    "This action is irreversible. Please review before proceeding.",
    kind="warning",
    title="Warning",
    icon=True,
    dismissable=True,
)
swp.spacer("6")

# Section: Error Alert
swp.section("Error Alert", subtitle="For errors and critical issues", bg="gray")
swp.spacer("4")
swp.alert(
    "Something went wrong. Please try again or contact support.",
    kind="error",
    title="Error",
    icon=True,
    dismissable=True,
)
swp.spacer("6")

# Section: Auto-dismiss Demo
swp.section("Auto-dismiss Alert", subtitle="This alert closes after 5 seconds", bg="white")
swp.spacer("4")
swp.alert(
    "This alert will automatically close in 5 seconds.",
    kind="info",
    title="Auto-dismiss Demo",
    icon=True,
    timeout=5,
)
swp.spacer("6")

# Section: Alert without Icon or Dismiss
swp.section("Minimal Alert", subtitle="Simple message without icon or dismiss button", bg="gray")
swp.spacer("4")
swp.alert(
    "A minimal alert message.",
    kind="info",
    icon=False,
    dismissable=False,
)
swp.spacer("6")

# Section: Stacked Alerts
swp.section("Multiple Alerts", subtitle="Stacking different kinds together", bg="white")
swp.spacer("4")
swp.alert("First notification", kind="info", dismissable=True)
swp.spacer("3")
swp.alert("Second notification", kind="success", dismissable=True)
swp.spacer("3")
swp.alert("Third notification", kind="warning", dismissable=True)
swp.spacer("6")

# Footer
swp.footer("© 2025 SlabWebPy · made with Python · https://github.com/DEV-Gordon/slabwebpy")

# Build and save
swp.build("dist/example_alert.html")
print("✓ Built: dist/example_alert.html")
