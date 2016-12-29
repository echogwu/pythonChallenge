#!/usr/bin/python

from PIL import Image, ImageChops
import numpy as np
image = Image.open("level16_mozart.gif")
shifted = [bytes(np.roll(row, -row.tolist().index(195)).tolist()) for row in np.array(image)]
#the frombytes() is not working appropriately
Image.frombytes(image.mode, image.size, b"".join(shifted)).show()
