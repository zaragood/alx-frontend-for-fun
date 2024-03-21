#!/usr/bin/python3
"""imported sys, markdown"""


import sys
import markdown


def markdown_to_html(readme_md, readme_html):
    """
    Converts a Markdown file to HTML.

    Args:
        readme_md (str): The path to the input Markdown file.
        readme_html (str): The path to the output HTML file.

    Raises:
        FileNotFoundError: If the input Markdown file does not exist.
    """
    try:
        with open(readme_md, 'r', encoding='utf-8') as md_file:
            markdown_content = md_file.read()    
        html_content = markdown.markdown(markdown_content)
        with open(readme_html, 'w', encoding='utf-8') as html_file:
            html_file.write(html_content)
    except FileNotFoundError:
        print(f"Missing {readme_md}", file=sys.stderr)
        sys.exit(1)
    else:
        sys.exit(0)


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: ./markdown2html.py README.md README.html")
        sys.exit(1)
    else:
        readme_md = sys.argv[1]
        readme_html = sys.argv[2]
        markdown_to_html(readme_md, readme_html)
