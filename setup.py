# Standard Library
import os
from typing import List

from setuptools import find_packages, setup

PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))


def load_requirements(filename: str) -> List[str]:
    with open(os.path.join(PROJECT_ROOT, filename), "r") as f:
        return f.read().splitlines()


setup(
    name="Reporter",
    version='0.1',
    setup_requires=["setuptools_scm", "pytest-runner"],
    use_scm_version={"fallback_version": "no_git"},
    description="make report for valodation models",
    author="Kirill Hiddelston",
    license='MIT',
    author_email="kkhiddleston@gmail.com",
    url="https://github.com/KirillHiddleston/reporter.git",
    packages=find_packages(exclude="tests"),
    include_package_data=True,
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Operating recursive-include package *System :: POSIX :: Linux",
        "Topic :: Scientific/Engineering",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.9",
    ],
    tests_require=["pytest-runner==6.0.0", "pytest-cov"],
    install_requires=load_requirements("requirements/requirements.txt"),
    extras_require={
        "format": load_requirements("requirements/requirements-format.txt"),
        "lint": load_requirements("requirements/requirements-lint.txt"),
        "test": load_requirements("requirements/requirements-test.txt"),
    },
    python_requires=">=3.9",
)
