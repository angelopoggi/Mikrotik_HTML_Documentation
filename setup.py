from setuptools import setup, find_packages

import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="mikrotikhtml",
    version="0.0.1",
    author="Angelo Poggi",
    author_email="angelo.poggi@webair.com",
    description="Simple script that exports Mikrotik config in HTML so that it can be uploaded to a Markdown supported documentation system or just share as a web page.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/purplecomputer/Mikrotik_HTML_Documentation",
    project_urls={
        "Bug Tracker": "https://github.com/purplecomputer/Mikrotik_HTML_Documentation/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "mt_html"},
    packages=setuptools.find_packages(where="mt_html"),
    python_requires=">=3.6",
    py_modules=['main'],
    include_package_data=True,
    install_requires=[
        'click',
        'routeros_api',
        'json2html',
    ],
    entry_points='''
        [console_scripts]
        mikrotikhtml=mt_html.cli:cli
    ''',
)


