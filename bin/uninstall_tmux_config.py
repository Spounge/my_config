#!/usr/bin/env python3.8

import sys

from consts import HOME_PATH
from utils import tasks
from utils.colors import Colors


print(f'{Colors.INFO}---Uninstalling TMUX config---{Colors.RESET}')

try:
    tasks.remove_file(f'{HOME_PATH}/.tmux.conf')
except Exception as e:
    print(f'{Colors.ERROR}{e}{Colors.RESET}', file=sys.stderr)
    print(f'{Colors.ERROR}---TMUX config uninstallation Failed---{Colors.RESET}')
    sys.exit(1)

print(f'{Colors.INFO}---TMUX config Uninstalled---{Colors.RESET}')
