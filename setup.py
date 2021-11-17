from setuptools import setup, find_packages

setup(
    name="mikrotikhtml",
    version='1.0',
    py_modules=['main'],
    packages=find_packages(),
    include_package_data=True,
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
