import click

from mt_html.mt_code import html_dump
from mt_html.env_creator import create_env_file

@click.group(help="""This simple tool logins to a Mikrotik and creats an HTML dump""")
def cli():
    pass

cli.add_command(html_dump)
cli.add_command(create_env_file)

if __name__ == "__main__":
    cli()