#/usr/bin/python
#/Library/Frameworks/Python.framework/Versions/3.5/bin/python3
#
#visit http://www.pythonchallenge.com/pc/return/disproportional.html huge/file to see the problem
#visit https://the-python-challenge-solutions.hackingnote.com/level-13.html for the solution

#must use python3 level13.py to run it, cuz python2 doesn't have module xmlrpc.client

import xmlrpc.client

conn = xmlrpc.client.ServerProxy("http://www.pythonchallenge.com/pc/phonebook.php")
print(conn.system.listMethods())
print(conn.system.methodHelp("phone"))
print(conn.system.methodSignature("phone"))
print(conn.phone("Bert"))


