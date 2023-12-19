#!/usr/bin/python3
""" Convert markdown to html """

import sys
import os


def convert_markdown_to_html(md_file, html_file):
    """ function to convert Markdown file to HTML."""

    if not os.path.isfile(md_file):
        print(f"Missing {md_file}", file=sys.stderr)
        sys.exit(1)

    with open(md_file, 'r') as markdown_file:
        md_content = markdown_file.readlines()

    html_content = ""
    in_list = False

    for line in md_content:
        if line.startswith("#"):
            # Cerrar la lista si está abierta antes del encabezado
            if in_list:
                html_content += "</ul>\n"
                in_list = False

            header_level = line.count("#")
            header_text = line.strip("#").strip()

            html_header = f"<h{header_level}>{header_text}</h{header_level}>"
            html_content += html_header + "\n"

        elif line.startswith("-"):
            if not in_list:
                html_content += "<ul>\n"
                in_list = True
            list_items = line.lstrip("-").strip().split()
            for item in list_items:
                html_content += f"<li>{item}</li>\n"

        else:
            # Cerrar la lista si no es una línea de encabezado o lista
            if in_list:
                html_content += "</ul>\n"
                in_list = False
            html_content += line

    # Cerrar la lista si está abierta al final del archivo
    if in_list:
        html_content += "</ul>\n"

    with open(html_file, 'w') as html_file:
        html_file.write(html_content)

    sys.exit(0)


if __name__ == "__main__":

    if len(sys.argv) < 3:
        print("Usage: ./markdown2html.py README.md README.html")
        sys.exit(1)

    md_file = sys.argv[1]
    html_file = sys.argv[2]

    convert_markdown_to_html(md_file, html_file)
