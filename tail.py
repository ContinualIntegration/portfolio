#!/usr/bin/python
'''
Background:  Linux has a tail command that shows the last portion of a file.
Sometimes you want to re-invent the wheel.  Why not have
a tail program of your own?  Seriously, Python has great native file
manipulation capabilities built-in.  This program prints out the last characters
of a file whereas Linux's tail is based on the last lines of a file.

Usage instructions:

1) identify the file you want to tail.  If you don't know,
run this command from a Linux prompt:
$ echo "abcdefghijklmnopqrstuvwxyz" > /tmp/tail.sample

2) Save this program as tail.py

3) Change the permissions like this:
$ chmod +x tail.py

4) Run this command (or replace the /tmp/tail.sample with
the file location and name of file you want to tail):

$ ./tail.py -c 10 /tmp/tail.sample
(You can replace the 10 with the number of characters you want outputted.)

Written by continualintegration.com.
'''

#!/usr/bin/python2.7
import os, sys

if len(sys.argv) == 2:
        os.system('tail ' + sys.argv[1])
elif len(sys.argv) == 3:
        os.system('tail ' + sys.argv[1] + ' ' + sys.argv[2])
elif len(sys.argv) == 4:
        os.system('tail ' + sys.argv[1] + ' ' + sys.argv[2] + ' ' + sys.argv[3])
else: print "wrong number of arguments"
