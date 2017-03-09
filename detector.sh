#!/bin/sh
./ssocr -d -1 bwimage.jpg | cat | perl -pe 's/_/-/g' | perl -ne 'if ($_=~/\./) {print $_} else {print substr($_,0,length($_)-2);print ".";print substr($_,-2);}'  > z_height.txt
cat z_height.txt
