#helps to create env file
#2021 - Angelo Poggi : angelo.poggi@webair.com
import click

@click.command()
@click.option('--createenv', '-c', help="""Helps you to create the .env file required to use this script.\n
                          mikrotikhtml --createenv <username> <password>""", required=True)
@click.argument('username')
@click.argument('password')
def create_env_file(username, password):
    """Creates the .env file which stores the firewalls username and password"""
    with open('.env', 'w') as envFile:
        envFile.write(f'username={username}')
        envFile.write(f'password={password}')
    click.echo(".env file generated, you should now be able to run the script against a firewall!")