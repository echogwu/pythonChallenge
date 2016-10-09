#!/usr/bin/python
#
#visit http://www.pythonchallenge.com/pc/def/channel.html to see the problem
#

import zipfile
import urllib
import sys
import os
import re

#first download the zip file from http://www.pythonchallenge.com/pc/def/channel.zip
urllib.urlretrieve("http://www.pythonchallenge.com/pc/def/channel.zip", "channel.zip") # or we can use commad line "url -o channel.zip http://www.pythonchallenge.com/pc/def/channel.zip"

if not os.path.isfile("channel.zip"):
    print "channel.zip does not exit in current dir"
    sys.exit(1)

comment = []

zf = zipfile.ZipFile("channel.zip")
filename = re.search("start from (\d+)", zf.read("readme.txt")).group(1) + ".txt"
while True:
    #can't use open() because it is a zip file
    #text = open(filename).read()
    text = zf.read(filename)
    try:
        filename = re.search("Next nothing is (\d+)", text).group(1)+".txt"
    except:
        print("file %s:\n%s" % (filename, text))
        break
    comment.append(zf.getinfo(filename).comment)

print "".join(comment)

#it will print a "hockey", when input the url: http://www.pythonchallenge.com/pc/def/hockey.html, it says "it's in the air. look at the letters.". Turned out that each letter from "HOCKEY" is made of letters "o,x,y,g,e,n" respectively




