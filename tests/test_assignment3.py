#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `assignment3` package."""


import sys
sys.path.append('.')
import pytest
from click.testing import CliRunner
from assignment3 import assignment3
from assignment3 import cli
from assignment3 import utils


def test_command_line_interface():
    ifile = "./data/input.txt"
    N, instructions = utils.parseFile(ifile)
    assert N == 10
    assert instructions == ['turn on 0,0 through 9,9\n', 'turn off 0,0 through 9,9\n','switch 0,0 through 9,9\n', 'turn off 0,0 through 9,9\n', 'turn on 2,2 through 7,7']
