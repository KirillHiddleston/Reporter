import markdown2
from weasyprint import CSS, HTML
from os import PathLike
from typing import Union


def markdown2pdf(render_content: str, output_pdf_path: Union[PathLike, str]) -> None:
    html_text = markdown2.markdown(render_content, extras=["tables", "fenced-code-blocks"])

    # Define some basic CSS to style the tables and code blocks
    css = CSS(
        string="""
        body {
            font-family: Arial, sans-serif;
        }
        table {
            width: 100%;
            border-collapse: collapse;
            margin-bottom: 20px;
        }
        th, td {
            border: 1px solid #dddddd;
            text-align: left;
            padding: 8px;
        }
        th {
            background-color: #f2f2f2;
        }
        pre, code {
            background-color: #f8f8f8;
            border: 1px solid #cccccc;
            border-radius: 3px;
            font-size: 16px;
        }
    """
    )

    # Convert HTML to PDF with CSS
    HTML(string=html_text).write_pdf(output_pdf_path, stylesheets=[css])
