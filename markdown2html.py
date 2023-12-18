#!/usr/bin/python3
""" 
convert markdown to html 
"""

import sys
import markdown2

def convert_markdown_to_html(input_file, output_file):
    """ function to convert markdown to html """

    try:
        with open(input_file, 'r', encoding='utf-8') as md_file:
            md_content = md_file.read()
            html_content = markdown2.markdown(md_content)

            with open(output_file, 'w', encoding='utf-8') as html_file:
                html_file.write(html_content)

    except FileNotFoundError:
        sys.stderr.write(f"Missing {input_file}\n")
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) < 3:
        sys.stderr.write('Usage: ./markdown2html.py README.md README.html\n')
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    convert_markdown_to_html(input_file, output_file)

    sys.exit(0)
