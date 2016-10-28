#!/usr/bin/python
#
#visit http://www.pythonchallenge.com/pc/return/5808.html username/password: huge/file to see the problem
#visit https://the-python-challenge-solutions.hackingnote.com/level-11.html for the solution

from PIL import Image

im = Image.open("level11.jpg")
(w, h) = im.size
print (w, h)
halfSize = (w/2, h/2)
oddImg = Image.new("RGB", halfSize)
evenImg = Image.new("RGB", halfSize)
for i in range(w):
    for j in range(h):
        if (i+j)%2 == 1:
            oddImg.putpixel((i/2, j/2), im.getpixel((i, j)))
        else:
            evenImg.putpixel((i/2, j/2), im.getpixel((i, j)))


evenImg.save("level11_even.jpg")
oddImg.save("level11_odd.jpg")
#evenImg.show()
#oddImg.show()


