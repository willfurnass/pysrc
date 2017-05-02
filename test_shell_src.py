#!/usr/bin/env python
import os
from shell_src import shell_src


def test_set_env():
    shell_src('./test_shell_src.sh')
    os.environ['somekey'] == 'somevalue'
