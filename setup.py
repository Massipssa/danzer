import versioneer
from setuptools import find_packages, setup

long_description = "Don't let anyone knows about your data. Use https://github.com/Massipssa/data-anonymizer.git"

with open("requirements.txt") as file:
    required_packages = file.read().splitlines()


def get_extras_require():
    pass


config = {
    "description": "Don't let anyone knows about your data",
    "author": "Massipssa Kerrache",
    "download_url": "https://github.com/Massipssa/data-anonymizer.git",
    "author_email": "massipssa.kerrache@gmail.com",
    "version": versioneer.get_version(),
    "cmdclass": versioneer.get_cmdclass(),
    "install_requires": required_packages,
    "extras_require": get_extras_require(),
    "packages": find_packages(
        exclude=["contrib*", "docs*", "tests*", "examples*", "scripts*"]
    ),
    "package_data": {"data_anonymizer": ["**/py.typed", "**/*.pyi"]},
    "name": "data_anonymizer",
    "long_description": long_description,
    "keywords": "big data anonymization pseudo anonymization",
    "include_package_data": True,
    "python_requires": ">=3.8",
    "classifiers": [
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
}

setup(**config)
