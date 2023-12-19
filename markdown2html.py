#!/usr/bin/python3
""" write a script markdown2html.py that takes an argument 2 strings:
First argument is the name of the Markdown file
Second argument is the output file name """

import sys
import os


def convert_markdown_to_html(md_file, html_file):
    """ function to convert Markdown file to HTML."""

    if not os.path.isfile(md_file):
        print(f"Missing {md_file}", file=sys.stderr)
        sys.exit(1)

    with open(md_file, 'r') as markdown_file:
        md_content = markdown_file.read()

    html_content = f"<html><body>{md_content}</body></html>"

    with open(html_file, 'w') as html_file:
        html_file.write(html_content)

    sys.exit(0)


if __name__ == "__main__":

    if len(sys.argv) < 3:
        """print("Usage: ./markdown2html.py README.md README.html")"""
        sys.exit(1)

    md_file = sys.argv[1]
    html_file = sys.argv[2]

    convert_markdown_to_html(md_file, html_file)
