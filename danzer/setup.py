import versioneer
from os import path
from setuptools import find_packages, setup

with open("requirements.txt") as file:
    required_packages = file.read().splitlines()

current_dir = path.abspath(path.dirname(__file__))
with open(path.join(current_dir, "README.MD"), encoding="utf-8") as f:
    long_description = f.read()


def get_extras_require():
    pass


config = {
    "description": "Don't let anyone knows about your data",
    "author": "Massipssa Kerrache",
    "download_url": "https://github.com/Massipssa/data-anonymizer.git",
    "author_email": "massipssa.kerrache@gmail.com",
    "version": "0.0.1", #versioneer.get_version(),
    #"cmdclass": versioneer.get_cmdclass(),
    "install_requires": required_packages,
    "extras_require": get_extras_require(),
    "packages": find_packages(
        exclude=["contrib*", "docs*", "tests*", "examples*", "scripts*"]
    ),
    "package_data": {"data_anonymizer": ["**/py.typed", "**/*.pyi"]},
    "name": "data_anonymizer",
    #"long_description": long_description,
    "long_description": "long_description",
    "long_description_content_type": "text",
    "keywords": "big data anonymization pseudo anonymization",
    "include_package_data": True,
    "python_requires": ">=3.8",
    "classifiers": [
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
}

setup(**config)
