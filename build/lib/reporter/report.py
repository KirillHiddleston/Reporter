# Standard Library
from os import PathLike
from typing import Union

from jinja2 import Environment, PackageLoader

# DomClick Internal
from reporter.config import DLConfig
from reporter.converter.html2docx import html2docx
from reporter.converter.markdown2pdf import markdown2pdf
from reporter.filter import to_html_filter


class Reporter:
    """
    Class for make report from markdonw template

    Example:
        >>> report = Reporter(templ_path='test_fieldnet.md',env_path='./validation_report/templates')
        >>> context = {'classes':['class1', 'class2']}
        >>> report.report(context=context, output_path=work_dir/'test.pdf')
    """

    def __init__(
        self,
        templ_path: Union[PathLike, str],
        package_name="validation_report",
        env_path="templates",
    ):
        env = Environment(
            loader=PackageLoader(package_name=package_name, package_path=env_path)
        )
        env.filters["to_html"] = to_html_filter
        self.template = env.get_template(templ_path)  # type: ignore

    def report_config_content(self, context: Union[PathLike, str], output_path: str):
        """
        Read yaml/json file by path
        Args:
            context: load by path yaml/json
            output_path: path save report docx/pdf/md
        Returns:
            None
        """
        try:
            template = self.template
            rendered_content = template.render(DLConfig.load(context))
            self._convert_report(rendered_content, output_path)
        except Exception as e:
            return f"An error occurred: {e}"

    def report_content(self, context: dict, output_path: str):
        """
        read context dict
        Args:
            context: load context dict
            output_path: path save report docx/pdf/md
        Returns:
            None
        """
        try:
            template = self.template
            rendered_content = template.render(context)
            self._convert_report(rendered_content, output_path)

        except Exception as e:
            return f"An error occurred: {e}"

    def _convert_report(self, rendered_content, output_path: str):
        if output_path.endswith("pdf"):
            markdown2pdf(rendered_content, output_path)
        elif output_path.endswith("docx"):
            html2docx(rendered_content, output_path)
        elif output_path.endswith("md"):
            with open(output_path, "w", encoding="utf-8") as f:
                f.write(rendered_content)
