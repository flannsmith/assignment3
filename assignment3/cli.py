# -*- coding: utf-8 -*-

"""Console script for assignment3."""


import sys
sys.path.append('.')
import click
from assignment3 import utils
from assignment3 import LEDTester
click.disable_unicode_literals_warning = True


@click.command()
@click.option("--input", default=None, help="input URI (file or URL)")
def main(input=None):
    N, instructions = utils.parseFile(input)
    ledTester = LEDTester.LEDTester(N)
    for i in instructions:
        ledTester.apply(i)
    print('#occupied: ', ledTester.count())




if __name__ == "__main__":
    import sys
    sys.exit(main())
