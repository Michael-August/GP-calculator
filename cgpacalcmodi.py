#CGPA calculator.

#assigning weight to grades
A, B, C, D, E, F = 5, 4, 3, 2, 1, 0

#for first semester

#collecting grade  and unit from user

English = eval(input("please input your   grade in English: ").upper())
Maths =  eval(input("please input your grade in maths: ").upper())
Physics =  eval(input("please input your grade in physics: ").upper())
Chemistry =  eval(input("please input your grade in chemistry: ").upper())
Biology =  eval(input("please input your grade in biology: ").upper())


English_unit, Maths_unit, Physics_unit, Chemistry_unit, Biology_unit = 3, 4, 4, 4, 3

#Calculating the points.
points = [English*English_unit, Maths*Maths_unit, Physics*Physics_unit, Chemistry*Chemistry_unit, Biology*Biology_unit ]

#summing the points
total_point = 0
for sum in points:
	total_point += sum
	
#summing the units
unit = [3, 4, 4, 4, 3]
total_unit = 0
for sums in unit:
	total_unit += sums

#calculating first semester GP
GP = total_point / total_unit
print(f"Your first semester GP is {GP}")

#second semester

#collecting grades
_2English = eval(input("please input your   grade in English: ").upper())
_2Maths =  eval(input("please input your grade in maths: ").upper())
_2Physics =  eval(input("please input your grade in physics: ").upper())
_2Chemistry =  eval(input("please input your grade in chemistry: ").upper())
_2Biology =  eval(input("please input your grade in biology: ").upper())

#calculating second semester point
_2points = [_2English*English_unit, _2Maths*Maths_unit, _2Physics*Physics_unit, _2Chemistry*Chemistry_unit, _2Biology*Biology_unit ]

#summing the points
_2total_point = 0
for _2sum in _2points:
	_2total_point += _2sum

#calculating second semester GP
_2GP = _2total_point / total_unit
print(f"Your first semester GP is {_2GP}")

#calculating the CGPA
CGP = (_2total_point + total_point) / (total_unit + total_unit)
print(f"Your CGPA is {CGP}")