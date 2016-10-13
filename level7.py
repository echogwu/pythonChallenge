#!/usr/bin/python
#
#visit http://www.pythonchallenge.com/pc/def/oxygen.html to see the problem
#visit https://the-python-challenge-solutions.hackingnote.com/level-7.html to see the solution

from PIL import Image
import urllib
import sys
import re

urllib.urlretrieve("http://www.pythonchallenge.com/pc/def/oxygen.png", "level7.png")

try:
    img = Image.open("level7.png")
except:
    print "downloading the image failed"
    sys.exit(1)

width = img.width
height = img.height
mid_height = round(height/2)
print("width = %d, height = %d" % (width, height))

midrow_pixs = [img.getpixel((x, mid_height)) for x in range(width)]
print("midrow_pixs:\n%s" % midrow_pixs)
value_for_each_pixel = [r for r, g, b, a in midrow_pixs if r == g == b]
print("value_for_each_pixel:\n%s" % value_for_each_pixel)
dedup_values = value_for_each_pixel[::7]
#very suspicious, the step 7 is by observing. I think to dedup using the way below is more accurate, but if I do so, the eventual answer is "i\negiy", doesn't quite make sense.
#dedup_values = []
#current_value = 0
#for v in value_for_each_pixel:
#    if current_value != v:
#        dedup_values.append(v)
#        current_value = v
print("dedup_values:\n%s" % dedup_values)
tran = "".join(map(chr, dedup_values))
print("tran = %s" % tran)
#tran = prints "smart guy, you made it. the next level is [105, 10, 16, 101, 103, 14, 105, 16, 121]"
num_list = re.findall("(\d+)", tran)
#num_list = ['105', '110', '116', '101', '103', '114', '105', '116', '121']"
print("num_list = %s" % num_list)
key = "".join(map(chr, map(int, num_list)))
print key
