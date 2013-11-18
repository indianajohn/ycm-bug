To reproduce:
-Install YouCompleteMe/Syntastic (Nothing else)
-Put "set hidden" in .vimrc
-Open one cpp file
-Ensure that YCM is active somehow, by feeding it proper flags through .ycm_extra_conf.py.
-Make a change to that buffer without saving it.
-Open another file.
-Start typing.  You should notice a flickering.

Or, just:
```bash
mkdir ~/dev; cd ~/dev
git clone http://github.com/indianajohn/ycm-bug/
cd ycm-bug
./install.sh
```
(wait)
```bash
gvim hello-world.cpp &
```
(insert some text without saving)
```bash
:o goodbye-cruel-world.cpp
```
(enter insert mode and start typing).
