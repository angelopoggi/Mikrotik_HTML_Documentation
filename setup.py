from setuptools import setup

setup(
    name="mikrotikhtml",
    version='1.0',
    py_modules=['main'],
    install_requires=[
        'click',
        'routeros_api',
        'json2html'
    ],
    entry_points='''
        [console_scripts]
        mikrotikhtml=mt_html.cli:cli
    ''',
)
