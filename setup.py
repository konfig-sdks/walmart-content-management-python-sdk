# coding: utf-8

"""
    Content Management

    The content management feed allows you to process content for items in bulk. You can take in content via the content feeds. Use the XSDs to manage content.

    The version of the OpenAPI document: 1.0.0
    Generated by: https://konfigthis.com
"""

from setuptools import setup, find_packages  # noqa: H301

NAME = "walmart-content-management-python-sdk"
VERSION = ""
# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

# read the contents of README file
from pathlib import Path
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

REQUIRES = [
    "certifi >= 2023.7.22",
    "python-dateutil ~= 2.8.2",
    "typing_extensions ~= 4.3.0",
    "urllib3 ~= 1.26.18",
    "cryptography ~= 42.0.5",
    "frozendict ~= 2.3.4",
    "aiohttp ~= 3.9.2",
    "pydantic ~= 2.4.2"
]

setup(
    name=NAME,
    version=VERSION,
    description="Content Management",
    author="Konfig",
    author_email="engineering@konfigthis.com",
    url="https://github.com/konfig-sdks/walmart-content-management-python-sdk/tree/main/python",
    keywords=["Konfig", "Content Management"],
    python_requires=">=3.7",
    install_requires=REQUIRES,
    packages=find_packages(exclude=["test", "tests"]),
    include_package_data=True,
    license="MIT",
    long_description=long_description,
    long_description_content_type='text/markdown'
)
