import os
import requests
import shutil
import sys
from pathlib import Path

from utils.colors import Colors


def check_dependencies(binaries):
    print(f'Checking dependencies: {", ".join(binaries)}... ', end='')
    missing_binaries = [binary for binary in binaries if not shutil.which(binary)]
    if missing_binaries:
        print(f'{Colors.ERROR}[ERROR]{Colors.RESET}')
        raise Exception(f'Missing dependencies: {", ".join(missing_binaries)}')
    print(f'{Colors.OK}[OK]{Colors.RESET}')


def copy(src, dst):
    print(f'Copying {src}... ', end='')
    try:
        shutil.copyfile(src, dst)
    except Exception as e:
        print(f'{Colors.ERROR}[ERROR]{Colors.RESET}')
        raise Exception(f'Cannot create {dst}: {e}')
    print(f'{Colors.OK}[OK]{Colors.RESET}')


def create_directory(path):
    print(f'Creating {path} directory... ', end='')
    try:
        os.makedirs(path, exist_ok=True)
    except Exception as e:
        print(f'{Colors.ERROR}[ERROR]{Colors.RESET}')
        raise Exception(f'Cannot create {path}: {e}')
    print(f'{Colors.OK}[OK]{Colors.RESET}')


def remove_directory(path):
    print(f'Removing {path} directory... ', end='')
    try:
        shutil.rmtree(path)
    except Exception as e:
        print(f'{Colors.ERROR}[ERROR]{Colors.RESET}')
        raise Exception(f'Cannot remove {path}: {e}')
    print(f'{Colors.OK}[OK]{Colors.RESET}')


def download_file(uri, path):
    print(f'Downloading {Path(path).name}... ', end='')
    try:
        res = requests.get(uri)
        open(path, 'wb').write(res.content)
    except Exception as e:
        print(f'{Colors.ERROR}[ERROR]{Colors.RESET}')
        raise Exception(f'Cannot download {Path(path).name}: {e}')
    print(f'{Colors.OK}[OK]{Colors.RESET}')


def remove_file(path):
    print(f'Removing {path}... ', end='')
    try:
        os.remove(path)
    except Exception as e:
        print(f'{Colors.ERROR}[ERROR]{Colors.RESET}')
        raise Exception(f'Cannot remove {path}: {e}')
    print(f'{Colors.OK}[OK]{Colors.RESET}')
