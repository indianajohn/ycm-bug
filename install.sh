#!/bin/sh

#backup
rm -rf backup
mkdir backup
mv ~/.vim ./backup/vim
mv ~/.vimrc ./backup/vimrc

git clone http://github.com/gmarik/vundle.git ~/.vim/bundle/vundle

cp vimrc ~/.vimrc
cp plugins.vim ~/.vim/
cp plugins_config.vim ~/.vim
cp .ycm_extra_conf.py ~/.vim/

vim -c ":BundleInstall" -c "qa"

cd ~/.vim/bundle/a.vim/plugin
mv a.vim a.vim.bak
sed '/imap/, +d' a.vim.bak > a.vim
cd ~/.vim/bundle/YouCompleteMe
./install.sh --clang-completer
cd ~/.vim/
