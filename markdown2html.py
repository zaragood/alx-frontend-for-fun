#!/usr/bin/python3
import sys
import markdown


def markdown_to_html(readme_md, readme_html):
    try:
        with open(readme_md, 'r', encoding='utf-8') as md_file:
            readme_md = md_file.read()
        
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
        markdown_to_html(readme_md, readme_md)
