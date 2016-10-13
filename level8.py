#!/usr/bin/python
#
#visit http://www.pythonchallenge.com/pc/def/integrity.html to see the problem
#visit https://the-python-challenge-solutions.hackingnote.com/level-8.html to see the solution

import bz2

username = 'BZh91AY&SYA\xaf\x82\r\x00\x00\x01\x01\x80\x02\xc0\x02\x00 \x00!\x9ah3M\x07<]\xc9\x14\xe1BA\x06\xbe\x084'
password = 'BZh91AY&SY\x94$|\x0e\x00\x00\x00\x81\x00\x03$ \x00!\x9ah3M\x13<]\xc9\x14\xe1BBP\x91\xf08'

un = bz2.decompress(username)
pw = bz2.decompress(password)
print un
print pw
