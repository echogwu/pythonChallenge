#!/usr/bin/python
#
#visit https://the-python-challenge-solutions.hackingnote.com/level-16.html to see the problem
#visit http://www.pythonchallenge.com/pc/return/mozart.html for the solution
#strategy
#    get properties of the original image: size, the most pixel and pink pixel
#    align the first pink pixels of each row to make get them straight on the left

from PIL import Image
import numpy as np

#get properties of the original image: size, the most pixel and pink pixel
img = Image.open("level16_mozart.gif")
(width, height) = img.size
print("size of original image: (%d, %d)" % (width, height))
#print(img.histogram())  #statistic about each each 1-byte pixel(0-255)

#max and enumerate functions
(most_pixel, most_count) = max(enumerate(img.histogram()),key=lambda x:x[1])
print("the pixel with the most count is %d, it repeated %d times" % (most_pixel, most_count))
'''
The following code tries to show a image with pure color, but the function 
frombytes() won't work as expected. The arg is '[60, 60, 60, ...]' So the 
bytes consisting the image is asciic value of '[','6','0','','6','0','',..... 
It is not exactly what we want which should be an array of 60.
tmp=img.copy()
tmp.frombytes(bytes([pixel]*(tmp.width*tmp.height)))
tmp.show()
'''
tmp = img.copy()
tmp.putdata([most_pixel]*(width*height))
tmp.show()
#that is not pink

pink_count = [x for x in img.histogram() if x % img.height == 0 and x != 0]
pink_pixel = img.histogram().index(pink_count[0])
print("pink_pixel = %d, pink_count=%d" % (pink_pixel, pink_count[0]))
'''
tmp2=img.copy()
tmp2.frombytes(bytes([pink_pixel]*(img.width*img.height)))
tmp2.show()
'''
tmp2 = img.copy()
tmp2.putdata([pink_pixel]*(width*height))
tmp2.show()

#align the first pink pixels of each row to make get them straight on the left
list_of_pixels = list(img.getdata())
index = 0
raw = []  #a 2-dimension array with width*height
row = []  #a list for each row in the image
while index < len(list_of_pixels):
    for i in range(width):
        row.append(list_of_pixels[index])
        index += 1
    raw.append(row)
    row = []
print(raw)

out = []   # a 1-dimension list of all the pixels of the image
# the below line should have a "tolist()" because np.roll returns a ndarray, not a list
for row in [np.roll(row, -row.index(pink_pixel)).tolist() for row in raw]:
    print(row)
    out += row
tmp3 = img.copy()
tmp3.putdata(out)
tmp3.show()

'''
shifted = [bytes(np.roll(row, -row.tolist().index(pink_pixel)).tolist()) for row in np.array(img)]
print(len(shifted))
print(shifted[0])
Image.frombytes(img.mode, img.size, ''.join(shifted)).show()
'''
