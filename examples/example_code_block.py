#!/usr/bin/env python3
"""
Example showcasing the code_block() component.
Demonstrates different languages, line numbers, themes, and copy functionality.

Run: python -m slabwebpy.example_code_block
Output: dist/example_code_block.html
"""

import slabwebpy as swp

# Title
swp.title("SlabWebPy — Code Block Component")

# Navbar
swp.navbar("SlabWebPy", links=[("Home", "#"), ("Docs", "#")])

# Hero
swp.hero(
    "Code Block Component",
    subtitle="Display source code with syntax labeling, copy button, and line numbers",
    cta_label="View Docs",
    color="indigo",
)

# Section: Python Example (Light Theme)
swp.section("Python Example — Light Theme", subtitle="With copy button and line numbers", bg="white")
swp.spacer("4")
swp.code_block(
    """def fibonacci(n: int) -> int:
    \"\"\"Calculate the nth Fibonacci number.\"\"\"
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

# Usage
result = fibonacci(10)
print(f"Fibonacci(10) = {result}")""",
    language="python",
    title="fibonacci.py",
    copy_button=True,
    line_numbers=True,
    theme="light",
)
swp.spacer("6")

# Section: JavaScript Example (Dark Theme)
swp.section("JavaScript Example — Dark Theme", subtitle="With line numbers and copy button", bg="gray")
swp.spacer("4")
swp.code_block(
    """const calculateSum = (arr) => {
    return arr.reduce((acc, num) => acc + num, 0);
};

const numbers = [1, 2, 3, 4, 5];
const sum = calculateSum(numbers);
console.log(`Sum: ${sum}`);  // Output: Sum: 15""",
    language="javascript",
    title="sum.js",
    copy_button=True,
    line_numbers=True,
    theme="dark",
)
swp.spacer("6")

# Section: HTML Example
swp.section("HTML Example", subtitle="Without line numbers", bg="white")
swp.spacer("4")
swp.code_block(
    """<div class="container mx-auto p-6">
    <h1 class="text-3xl font-bold mb-4">Welcome!</h1>
    <p class="text-gray-600">This is a sample HTML snippet.</p>
</div>""",
    language="html",
    title="index.html",
    copy_button=True,
    line_numbers=False,
    theme="light",
)
swp.spacer("6")

# Section: SQL Example
swp.section("SQL Example", subtitle="Dark theme without title", bg="gray")
swp.spacer("4")
swp.code_block(
    """SELECT users.id, users.name, COUNT(orders.id) as order_count
FROM users
LEFT JOIN orders ON users.id = orders.user_id
GROUP BY users.id, users.name
ORDER BY order_count DESC
LIMIT 10;""",
    language="sql",
    copy_button=True,
    line_numbers=True,
    theme="dark",
)
swp.spacer("6")

# Section: Bash Example
swp.section("Bash Example", subtitle="Simple script", bg="white")
swp.spacer("4")
swp.code_block(
    """#!/bin/bash
# Deploy script
echo "Building..."
npm run build
echo "Deploying to production..."
git add .
git commit -m "Deploy: $(date)"
git push origin main""",
    language="bash",
    title="deploy.sh",
    copy_button=True,
    line_numbers=True,
    theme="light",
)
swp.spacer("6")

# Section: JSON Example
swp.section("JSON Example", subtitle="Configuration file", bg="gray")
swp.spacer("4")
swp.code_block(
    """{
  "name": "slabwebpy",
  "version": "0.3.0",
  "description": "Build modern web apps with Python",
  "author": "DEV-Gordon",
  "license": "MIT",
  "repository": "https://github.com/DEV-Gordon/slabwebpy"
}""",
    language="json",
    title="package.json",
    copy_button=True,
    line_numbers=False,
    theme="dark",
)
swp.spacer("6")

# Footer
swp.footer("© 2025 SlabWebPy · made with Python · https://github.com/DEV-Gordon/slabwebpy")

# Build and save
swp.build("dist/example_code_block.html")
print("✓ Built: dist/example_code_block.html")
