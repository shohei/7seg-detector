#!/bin/sh
./ssocr -d -1 bwimage.jpg | cat | perl -ne 'print substr($_,0,length($_)-2);print ".";print substr($_,-2);' > z_height.txt
