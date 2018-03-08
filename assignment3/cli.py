# -*- coding: utf-8 -*-

"""Console script for assignment3."""

import click


@click.command()
def main(args=None):
    """Console script for assignment3."""
    click.echo("Replace this message by putting your code into "
               "assignment3.cli.main")
    click.echo("See click documentation at http://click.pocoo.org/")
    return 0


if __name__ == "__main__":
    import sys
    sys.exit(main())
