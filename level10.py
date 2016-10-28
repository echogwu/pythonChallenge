#!/usr/bin/python
#
#visit http://www.pythonchallenge.com/pc/return/bull.html to see the problem
#visit https://the-python-challenge-solutions.hackingnote.com/level-10.html for the solution

import re
import itertools

#By clicking the image:
#a = [1, 11, 21, 1211, 111221,
#a look and say sequence

def solution1():
    input_str = "1"
    print input_str
    for i in range(20):
        input_str = recurse(input_str)
        print input_str

def recurse(num_str):
    '''
    startStr: a string representing a number
    out_str: the statistic output of the previous num_str
    '''
    num = 0
    current_value = num_str[0]
    out_str = ""
    for i in range(len(num_str)):
        if num_str[i] == current_value:
            num += 1
            continue
        out_str += str(num)
        out_str += current_value
        current_value = num_str[i]
        num = 1
    out_str += str(num)
    out_str += current_value

    return out_str

def solution2():
    input_str = "1"
    for i in range(20):
        input_str = "".join([str(len(j)+1)+i for i, j in re.findall(r'(\d)(\1*)',input_str)])
        '''
        re.findall(r'(\d)(\1*)', "11112231")
        [('1', '111'), ('2', '2'), ('3', ''), ('1', '')]
        re.findall(r'(\d)(\1*)(\1*)', "11112231")
        [('1', '111', ''), ('2', '2', ''), ('3', '', ''), ('1', '', '')]
        re.findall(r'(\d)(\1)(\1*)', "11112231")
        [('1', '1', '11'), ('2', '2', '')]
        re.findall(r'(\d)(\1)(\2*)', "11112231")
        [('1', '1', '11'), ('2', '2', '')]
        '''
        print input_str

def solution3():
    input_str = "1"
    print input_str
    for i in range(20):
        input_str = "".join([str(len(list(y)))+str(x) for x, y in itertools.groupby(input_str)])
        '''
        for x, y in itertools.groupby("1111221"):
        ...     print x, list(y)
        ...
        1 ['1', '1', '1', '1']
        2 ['2', '2']
        1 ['1']
        '''
        print input_str

solution2()

