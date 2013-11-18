" Automatically source the plugins.vim when it is saved
autocmd! bufwritepost plugins.vim source %

filetype off
set rtp+=~/.vim/bundle/vundle/
call vundle#rc()

" Add plugins here.
Bundle 'gmarik/vundle'
" Bundle 'scrooloose/nerdtree'
Bundle 'Valloric/YouCompleteMe'
Bundle 'scrooloose/syntastic'

filetype plugin indent on
