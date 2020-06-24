# -*- coding: utf-8 -*-
"""
Created on Wed Jun 24 14:00:10 2020

@author: vishal
"""


from math import tan,pi
 
 
length  = float(input("Enter the length of each side of Polygon (in meters): "))
number  = int(input("Enter the number of sides: "))
 
area = (number * length ** 2)/(4 * tan(pi/number))
 
print("The area of Polygon is  " , area)