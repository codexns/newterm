# coding: utf-8
from __future__ import unicode_literals, division, absolute_import, print_function

import sys

if sys.platform == 'win32':
    from ._win import open_executable, open_powershell, open_cmd

elif sys.platform == 'darwin':
    from ._osx import open_terminal, open_iterm
    from ._posix import open_executable

else:
    from ._linux import get_default_terminal
    from ._posix import open_executable


__version__ = '0.9.0'
__version_info__ = (0, 9, 0)


def launch_terminal(cwd, env=None, terminal=None, args=None, width=1024, use_tabs=False):
    """
    Launches a terminal at the directory specified

    :param cwd:
        A unicode string of the working directory to open the terminal to

    :param env:
        A dict of unicode strings for a custom environmental variables to set

    :param terminal:
        A unicode string of the name of the terminal to execute. If None, uses
        the OS default. Special OS X values include: "Terminal.app" and
        "iTerm.app". Special Windows values include: "powershell.exe" and
        "cmd.exe". All others are launched as a subprocess and must pick up the
        cwd and env from the Python subprocess module.

    :param args:
        A list of unicode strings of the arguments to pass to the terminal
        executable. Ignored when terminal is set to any of:

         - "Terminal.app"
         - "iTerm.app",
         - "cmd.exe"
         - "powershell.exe"

    :param width:
        Windows only: an integer of the width of the terminal window when
        terminal is None, "powershell.exe" or "cmd.exe"

    :param use_tabss:
        OS X only: a boolean if tabs should be used instead of new windows when
        terminal is None, "Terminal.app" or "iTerm.app"
    """

    if sys.platform == 'darwin':
        if terminal is None or terminal == 'Terminal.app':
            open_terminal(cwd, env=env, use_tabs=use_tabs)
        elif terminal == 'iTerm.app':
            open_iterm(cwd, env=env, use_tabs=use_tabs)
        else:
            open_executable(terminal, args, cwd, env=env)

    elif sys.platform == 'win32':
        if terminal is None or terminal == 'powershell.exe':
            open_powershell(cwd, env=env, width=width)
        elif terminal == 'cmd.exe':
            open_cmd(cwd, env=env, width=width)
        else:
            open_executable(terminal, args, cwd, env=env)

    else:
        if terminal is None:
            terminal = get_default_terminal()
        open_executable(terminal, args, cwd, env=env)
