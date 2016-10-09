#!/usr/bin/python
#
#visit http://stackoverflow.com/questions/642154/how-to-convert-strings-into-integers-in-python to see the problem
#
T1 = (('13', '17', '18', '21', '32'),
      ('07', '11', '13', '14', '28'),
      ('01', '05', '06', '08', '15', '16'))
T2 = [map(int,x) for x in T1]
print T2

#explain how line 8 works
#see help(map)
#x is a list, in this case, it is the tuples in the tuple T1
#If T1 is only one ordinary tuple, without nested tuples inside it, it is going to be different
#T1=("12","34")
#T2=[map(int,x) for x in T1]
#output: [[1, 2], [3, 4]], not what we would expect
