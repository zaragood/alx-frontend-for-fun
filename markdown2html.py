#!/usr/bin/python3
import sys
import markdown
"""
    Write a script markdown2html.py that takes an argument 2 strings:

    First argument is the name of the Markdown file
    Second argument is the output file name
    Requirements:

    If the number of arguments is less than 2: print in STDERR
    Usage: ./markdown2html.py README.md README.html and exit 1
    If the Markdown file doesn’t exist: print in STDER
    Missing <filename> and exit 1
    Otherwise, print nothing and exit 0
"""

if len(sys.argv) < 3:
    print("Usage: ./markdown2html.py README.md README.html", file=sys.stderr)
    sys.exit(1)

input_file = sys.argv[1]
output_file = sys.argv[2]

try:
    with open(input_file, 'r') as f:
        markdown_text = f.read()
except FileNotFoundError:
    print(f"Missing {input_file}", file=sys.stderr)
    sys.exit(1)

html_text = markdown.markdown(markdown_text)

with open(output_file, 'w') as f:
    f.write(html_text)

sys.exit(0)
