#!/usr/bin/python
#
#visit http://www.pythonchallenge.com/pc/return/uzi.html to see the problem
#visit https://the-python-challenge-solutions.hackingnote.com/level-15.html for the solution

import datetime

print [year for year in range(1016, 1996, 20) if datetime.date(year, 1, 26).isoweekday() == 1]
# try dateteime.date(year, month, day).weekday()/isocalendar()


