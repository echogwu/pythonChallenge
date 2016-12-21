#!/usr/bin/python
#
#visit http://www.pythonchallenge.com/pc/return/italy.html to see the problem
#visit https://the-python-challenge-solutions.hackingnote.com/level-14.html for the solution
#draw a image in a spiraling way. First to right for 100 pixel, then down for 99 pixel, then to left for 99 pixel, then 98 pixel up, to right 98...
#(100,99,99,98),(98,97,97,96),....

from PIL import Image

im = Image.open('level14_wire.png')
# print(im.size)
# output (10000,1)
out = Image.new("RGB", [100, 100])
delta = ((1, 0), (0, 1), (-1, 0), (0, -1))
x, y, p = -1, 0, 0
d = 200
while d/2 > 0:
    for v in delta:
        steps = d//2
    	for i in range(steps):
	    x = x + v[0]
            y = y + v[1]
    	    out.putpixel((x, y), im.getpixel((p, 0)))
            p += 1
	d -= 1

out.show()





