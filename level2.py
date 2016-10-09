#!/usr/bin/python
#
#visit the below url to see the problem
#http://www.pythonchallenge.com/pc/def/ocr.html
#

import re

with open("level2.html") as f:
    contents = f.read()

#another way to open files
#contents = open("ocr.html","r").read()

start = contents.rfind("<!--")+len("<!--")
end = contents.rfind("-->")

targetCont = contents[start+1:end-1]
#print(re.findall("[a-zA-Z]", targetCont))
print("".join(re.findall("[a-zA-Z]", targetCont)))
