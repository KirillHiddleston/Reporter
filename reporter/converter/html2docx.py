# Standard Library
from html.parser import HTMLParser
from os import PathLike
from typing import Union

from docx import Document


class Parser(HTMLParser):
    def __init__(self, doc):
        super().__init__()
        self.doc = doc

    def handle_data(self, data):
        self.doc.add_paragraph(data)


def html2docx(html_template: str, save_path: Union[PathLike, str]) -> None:
    document = Document()
    parser = Parser(document)
    parser.feed(html_template)
    document.save(save_path)
