#!/usr/bin/python
#
#visit the below url to see the problem
#http://www.pythonchallenge.com/pc/def/equality.html
#

import re

content = open("level3.html","r").read()
targetCon = content[content.rfind("<!--")+4:content.rfind("-->")].replace("\n","")

#print re.findall("[^A-Z][A-Z]{3}[a-z][A-Z]{3}[^A-Z]",targetCon)
#the output of the above is: ['qIQNlQSLi', 'eOEKiVEYj', 'aZADnMCZq', 'bZUTkLYNg', 'uCNDeHSBj', 'kOIXdKBFh', 'dXJVlGZVm', 'gZAGiLQZx', 'vCJAsACFl', 'qKWGtIDCj']

#print re.findall("[^A-Z][A-Z]{3}([a-z])[A-Z]{3}[^A-Z]", targetCon)
#the output of the above is:['l', 'i', 'n', 'k', 'e', 'd', 'l', 'i', 's', 't']

print "".join(re.findall("[^A-Z][A-Z]{3}([a-z])[A-Z]{3}[^A-Z]", targetCon))
