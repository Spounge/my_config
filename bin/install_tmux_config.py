#!/usr/bin/env python3.8

import sys

from consts import (
    HOME_PATH,
    TMUX_CONF_PATH,
)
from utils import tasks
from utils.colors import Colors


print(f'{Colors.INFO}---Installing TMUX config---{Colors.RESET}')

try:
    tasks.check_dependencies(['tmux'])
    tasks.copy(TMUX_CONF_PATH, f'{HOME_PATH}/.tmux.conf')
except Exception as e:
    print(f'{Colors.ERROR}{e}{Colors.RESET}', file=sys.stderr)
    print(f'{Colors.ERROR}---TMUX config installation Failed---{Colors.RESET}')
    sys.exit(1)

print(f'{Colors.INFO}---TMUX config Installed---{Colors.RESET}')
