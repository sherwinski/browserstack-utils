import click
from utils import *

@click.group()
def browserstack_utils():
    pass

@browserstack_utils.command()
def fetch():
    '''
        Fetches the list of currently running jobs and saves the output
        to a new file.
            - Takes no arguments
    '''
    fetch_workers()

@browserstack_utils.command()
@click.argument('filename')
def delete(filename):
    '''
        Terminates all workers described in a file passed as an option
            - Takes a filename as an argument
    '''
    delete_workers(filename)

@browserstack_utils.command()
def clean():
    '''
        Cleans up all worker files created as a result of calling fetch
    '''
    cleanup()

if __name__ == '__main__':
    browserstack_utils()
