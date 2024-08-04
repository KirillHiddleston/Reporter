# Standard Library
import os


from reporter.report import Reporter


def test_report_config(yaml_config, report_path, template_md):
    report = Reporter(
        templ_path=template_md,
        package_name="validation_report",
        env_path=os.path.abspath("tests/files"),
    )
    report.report_config_content(
        context=yaml_config,
        output_path=report_path
    )
    assert os.path.exists(report_path)


def test_report_dict(report_path, template_md):
    report = Reporter(
        templ_path=template_md,
        package_name="reporter",
        env_path=os.path.abspath("tests/files"),
    )
    config = {
        'title_report': 'Segmentation doc',
        'mleco_model_name': 'mobilenetv3',
        'training_id': '1',
        'contact_telegram': '@Barak_obama',
        'contact_email': 'Barak Obama'
    }
    report.report_content(
        context=config,
        output_path=report_path
    )
    assert os.path.exists(report_path)
