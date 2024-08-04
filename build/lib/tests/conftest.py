# Standard Library
import os.path
import shutil
import tempfile

import pytest


@pytest.fixture(scope="session")
def temp_dir():
    temp_dir = tempfile.mkdtemp()
    yield temp_dir
    shutil.rmtree(temp_dir)


@pytest.fixture(scope="session")
def yaml_config():
    config = "tests/files/test_config.yml"
    return config


@pytest.fixture(scope="session")
def template_md():
    config = "test_model.md"
    return config


@pytest.fixture(scope="session")
def report_path(temp_dir):
    path = f"{temp_dir}/test_report.pdf"
    return path
