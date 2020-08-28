from pathlib import Path

HOME_PATH = Path.home()

# NEOVIM

NEOVIM_BASE_DIR = '../neovim'
NEOVIMRC_PATH = f'{NEOVIM_BASE_DIR}/vimrc'
NEOVIM_PLUG_URI = 'https://raw.githubusercontent.com/junegunn/vim-plug/master/plug.vim'
NEOVIM_CONFIG_PATH = f'{HOME_PATH}/.config/nvim'


# TMUX

TMUX_BASE_DIR = '../tmux'
TMUX_CONF_PATH = f'{TMUX_BASE_DIR}/tmux.conf'
