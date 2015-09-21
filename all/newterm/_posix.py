# coding: utf-8
from __future__ import unicode_literals, division, absolute_import, print_function

import sys
import os
import subprocess


def launch_executable(executable, args, cwd, env=None):
    """
    Launches an executable with optional arguments

    :param executable:
        A unicode string of an executable

    :param args:
        A list of unicode strings to pass as arguments to the executable

    :param cwd:
        A unicode string of the working directory to open the executable to

    :param env:
        A dict of unicode strings for a custom environmental variables to set
    """

    subprocess_args = [executable]
    subprocess_args.extend(args)

    if sys.version_info >= (3,):
        subprocess_env = dict(os.environ)
    else:
        subprocess_env = {}
        for key, value in os.environ.items():
            subprocess_env[key.decode('utf-8', 'replace')] = value.decode('utf-8', 'replace')

    if env:
        for key, value in env.items():
            subprocess_env[key] = value

    if sys.version_info < (3,):
        encoded_args = []
        for arg in subprocess_args:
            encoded_args.append(arg.encode('utf-8'))
        subprocess_args = encoded_args

        encoded_env = {}
        for key, value in subprocess_env.items():
            encoded_env[key.encode('utf-8')] = value.encode('utf-8')
        subprocess_env = encoded_env

        cwd = cwd.encode('utf-8')

    subprocess.Popen(subprocess_args, env=subprocess_env, cwd=cwd)
