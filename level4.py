#!/usr/bin/python
#
#visit ?? to see the problem
#

import urllib
import re

num_suffix = "12345"
while True:
    text = urllib.urlopen("http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=%s" % num_suffix).read()
    print text
    pat = "the next nothing is (\d+)"
    matchObj = re.search(pat, text)
    if not matchObj:
        if text.find("Divide by two and keep going") != -1:
            num_suffix = str(int(num_suffix) / 2)
            continue
        break
    num_suffix = matchObj.group(1)
    #print num_suffix


