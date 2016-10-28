#!/usr/bin/python
#
#visit http://www.pythonchallenge.com/pc/return/evil.html huge/file to see the problem
#visit https://the-python-challenge-solutions.hackingnote.com/level-12.html for the solution

data = open("level12.gfx", "rb").read()
print len(data)
for i in range(5):
    open("level12_%d.jpg" % i, "wb").write(data[i::5])


