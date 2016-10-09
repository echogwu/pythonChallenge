#!/usr/bin/python
#
# vist http://www.pythonchallenge.com/pc/def/map.html to see the problem
#

import string
from string import maketrans
import sys
import inspect

# my way of dealing with this problem
def translate1(text):
    '''input a long text and get the translation. The rule is to replace each of the letters with the letter 2 steps after it in the alphabet table. If it reaches to the end of the table, rotate it to the beginning of the table
    '''
    newText = ""
    for letter in text:
        asciiNum = ord(letter)
        if asciiNum >= 97 and asciiNum <=122:
            letter = chr(97+(asciiNum-97+2)%26) #rotate wihin the alphabet table
        newText += letter

    return newText

def translate2(text):
    '''make a tranlation table by using the method maketrans()
    '''
    #intab = 'abcdefghijklmnopqrstuvwxyz'
    #outtab = 'cdefghijklmnopqrstuvwxyzab'
    #a better way to do the letters
    intab = string.lowercase
    outtab = string.lowercase[2:] + string.lowercase[:2]
    trantab = maketrans(intab, outtab)
    newText = text.translate(trantab)
    return newText

text = ''
#text = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."
if not text:
    try:
        text = sys.argv[1]
    except:
        print("orgininal text NOT provided, append that to \"python %s\"" % inspect.stack()[0][1] ) #get the current file name
print("the original text is: %s" % text)
print("solution 1 result: %s" % translate1(text))
print("solution 2 result: %s" % translate2(text))
