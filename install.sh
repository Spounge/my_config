# Install neovim, tmux with minimum version

# checkout stow / yadm for symlinks

## nvim
# create ~/.config/nvim/
# create ~/.config/nvim/autoload
# https://raw.githubusercontent.com/junegunn/vim-plug/master/plug.vim in ~/.config/nvim/autoload/plug.vim
ln -s $(readlink -f neovim/vimrc) ~/.config/nvim/init.vim
ln -s $(readlink -f neovim/vimwiki) ~/.config/nvim/vimwiki

## Tmux
# xdg ?
ln -s $(readlink -f tmux/tmux.conf) ~/.tmux.conf
