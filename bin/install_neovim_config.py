#!/usr/bin/env python3.8

import sys

from consts import (
    NEOVIM_CONFIG_PATH,
    NEOVIMRC_PATH,
    NEOVIM_PLUG_URI,
)
from utils import tasks
from utils.colors import Colors


print(f'{Colors.INFO}---Installing NEOVIM config---{Colors.RESET}')

try:
    tasks.check_dependencies(['nvim'])
    tasks.create_directory(NEOVIM_CONFIG_PATH)
    tasks.create_directory(f'{NEOVIM_CONFIG_PATH}/autoload')
    tasks.copy(NEOVIMRC_PATH, f'{NEOVIM_CONFIG_PATH}/init.vim')
    tasks.download_file(NEOVIM_PLUG_URI, f'{NEOVIM_CONFIG_PATH}/autoload/plug.vim')
except Exception as e:
    print(f'{Colors.ERROR}{e}{Colors.RESET}', file=sys.stderr)
    print(f'{Colors.ERROR}---NEOVIM config installation Failed---{Colors.RESET}')
    sys.exit(1)

print(f'{Colors.INFO}---NEOVIM config Installed---{Colors.RESET}')
print(f'{Colors.IMPORTANT}Open vim and run :PlugInstall{Colors.RESET}')
