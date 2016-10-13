#!/usr/bin/python
#
#visit http://www.pythonchallenge.com/pc/return/good.html un: "huge" pw: "file" to see the problem
#visit https://the-python-challenge-solutions.hackingnote.com/level-9.html for the solution

from PIL import Image, ImageDraw
import urllib

#need to use username(huge) and password(file) to open this url
content = urllib.urlopen("http://www.pythonchallenge.com/pc/return/good.html").read()
start = content.rfind("first:") + len("first:") + 1
end = content.rfind("second:") - 2
first = map(int, content[start:end].replace("\n","").split(","))
print("first:\n%s" % first)
start = content.rfind("second:") + len("second:") +1
end = content.rfind("-->") -2
second = map(int, content[start:end].replace("\n","").split(","))
print("second:\n%s" % second)

im = Image.new('RGB', (500, 500),"white")
draw = ImageDraw.Draw(im)
draw.polygon(first, fill="black")
draw.polygon(second, fill = "blue")
im.show()


