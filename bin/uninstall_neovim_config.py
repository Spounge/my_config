#!/usr/bin/env python3.8

import sys

from consts import NEOVIM_CONFIG_PATH
from utils import tasks
from utils.colors import Colors


print(f'{Colors.INFO}---Uninstalling NEOVIM config---{Colors.RESET}')

try:
    tasks.remove_directory(NEOVIM_CONFIG_PATH)
except Exception as e:
    print(f'{Colors.ERROR}{e}{Colors.RESET}', file=sys.stderr)
    print(f'{Colors.ERROR}---NEOVIM config uninstallation Failed---{Colors.RESET}')
    sys.exit(1)


print(f'{Colors.INFO}---NEOVIM config Uninstalled---{Colors.RESET}')
