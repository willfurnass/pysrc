#!/usr/bin/env python
"""Source a bash shell script, manipulating the current environment."""
from __future__ import print_function
import os
from subprocess import Popen, PIPE
import json


def shell_src(fpath):
    """Source a bash shell script, manipulating the current environment.

    Based on http://stackoverflow.com/a/7198338
    """
    pipe = Popen(['/bin/bash', '-c',
                  'source {} && {}'.format(fpath, __file__)],
                 stdout=PIPE)
    env = pipe.stdout.read()
    os.environ = json.loads(env)


def _print_env_as_json():
    """Helper function that prints the current environment as JSON."""
    print(json.dumps(dict(os.environ)))


if __name__ == '__main__':
    """If called as a script, print the current environment as JSON."""
    _print_env_as_json()
