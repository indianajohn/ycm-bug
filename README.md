# vim-config

---------------------

## Dependencies

  1. [xsel](http://www.kfish.org/software/xsel/)
  2. [exuberant-ctags](http://ctags.sourceforge.net/)
  3. [ack-grep](http://betterthangrep.com/)
  4. [CMake](http://cmake.org/)
  5. [Git](http://git-scm.com/)
  6. [Python](http://python.org/)
  7. Vim version 7.3.584 or later with python support.  A Ubuntu 12.04 package is included in this repository, since the respective package is too old.
  8. A basic C++ compilation environment including GNU compilers, often included in package distributions like "build-essential" in Debian-based distributions.



## Installation

  1. Install the dependencies.
  2. Install vim from source a-la https://github.com/Valloric/YouCompleteMe/wiki/Building-Vim-from-source
  3. cd ~/; mkdir dev; cd dev
  4. git clone 'https://github.com/indianajohn/vim-config/'
  5. cd vim_config
  6. ./install.sh
  7. Build the C++ portion of YouCompleteMe (see https://github.com/Valloric/YouCompleteMe )

``` bash
# For Ubuntu 12.04 LTS on AMD 64
sudo apt-get update
sudo apt-get install xsel exuberant-ctags ack-grep gdebi python-dev cmake git build-essential python-dev pyflakes
cd ~/
mkdir dev
cd dev
sudo apt-get remove vim vim-tiny vim-gnome vim-common vim-gui-common
git clone 'https://github.com/indianajohn/vim-config/'
cd ~/dev/vim-config
sudo gdebi vim-custom.deb
ln -s /usr/bin/vim /usr/bin/gvim
./install.sh
```

## Plugins

  1. [Vundle](https://github.com/gmarik/vundle) - The plug-in manager for Vim
  2. [Molokai](https://github.com/tomasr/molokai) - Molokai color scheme for Vim
  3. [PrettyGuides](https://github.com/adonis0147/prettyGuides) - Indent guides - displaying indent levels by vertical lines for Vim editor
  4. [Ack.vim](https://github.com/mileszs/ack.vim) -Vim plugin for the Perl module / CLI script 'ack'
  5. [Vim-easymotion](https://github.com/Lokaltog/vim-easymotion) - Allows for quick movement
  6. [Nerdtree](https://github.com/scrooloose/nerdtree) - A tree explorer plugin for vim
  7. [Tagbar](https://github.com/majutsushi/tagbar) - Vim plugin that displays tags in a window, ordered by class etc
  8. [Syntastic](https://github.com/scrooloose/syntastic) -Syntax checking hacks for vim
  9. [Nerdcommenter](https://github.com/scrooloose/nerdcommenter) - Automation for commenting.
  10. [Ultisnips](https://github.com/SirVer/ultisnips) - This is an implementation of TextMates Snippets for the Vim Text Editor
  11. [sudo.vim](https://github.com/vim-scripts/sudo.vim) - Allows one to edit a file with privileges from an unprivileged session
  12. [YouCompleteMe](https://github.com/Valloric/YouCompleteMe) - Very good auto-completion.
  13. [vim-airline](https://github.com/bling/vim-airline) - Good statusline with no configuration needed.

## Shortcuts

  - `,e`  ==> quit
  - `,E`  ==> quit all without saving
  - `,<enter>`  ==> don't highlight the search results
  - Easier moving between windows:
    + `ctrl-j`  ==> down
    + `ctrl-k`  ==> up
    + `ctrl-h`  ==> left
    + `ctrl-l`  ==> right
  - Easier moving between tabs
    + `,n`  ==> previous tab
    + `,m`  ==> next tab
  - Copy content to clipboard
    1. Select the content
    2. In visual mode, press `ctrl-c`
  - `,f`  ==> toggle ctrlp
  - `<F3>`  ==> toggle nerdtree
  - `<F4>`  ==> toggle tagbar
  - `<F5>`  ==> build a project
  - `<F9>`  ==> build and run(only available for a single source code file)
  - ack a word which is under the cursor
    1. `,a` ==> toggle ack command
    2. Edit the command
    3. Press `enter`
  - `ctrl-j`  ==> UltiSnipsExpandTrigger

## Plugins Management

### Install

  1. Edit *~/.vim/plugins.vim*
  2. Add the name of the plugin you want to install
  3. In normal mode, type `:BundleInstall`
  4. Press `enter`

### Uninstall

  1. Edit *~/.vim/plugins.vim*
  2. Comment the name of the plugin you want to uninstall
  3. In normal mode, type `:BundleClean`
  4. Press `enter`

### Update

  1. In normal mode, type `:BundleInstall!`
  2. Press `enter`

For details, you can see [https://github.com/gmarik/vundle](https://github.com/gmarik/vundle).

## Remarks

  1. To edit a file with privileges from an unprivileged session.
    ``` bash
    # For example, we want to edit /etc/sudoers and type it in terminal:
    sudo vim /etc/sudoers
    # We will get a prompt - neocomplcache disabled: "sudo vim" is detected and $HOME is set to your user's home. You may want to use the sudo.vim plugin, the "-H" option with "sudo" or set always_set_home in /etc/sudoers instead.

    # Instead of typing "sudo vim /etc/sudoers" in terminal, we should type:
    vim sudo:/etc/sudoers
    ```
  2. To check the syntax of some programing languages, we should install the check tools for those languages.
    ```bash
    # For example, Python requires either flake8, pyflakes or pylint.
    # For Debian/Ubuntu
    sudo apt-get install pyflakes
    ```
    For details, you can see [https://github.com/scrooloose/syntastic](https://github.com/scrooloose/syntastic).

## References

  1. [https://github.com/amix/vimrc](https://github.com/amix/vimrc)
  2. [https://github.com/mbrochh/vim-as-a-python-ide](https://github.com/mbrochh/vim-as-a-python-ide)
  3. [https://github.com/humiaozuzu/dot-vimrc](https://github.com/humiaozuzu/dot-vimrc)

