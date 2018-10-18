# -*- coding: utf-8 -*-
"""
Created on Fri Oct 12 17:28:07 2018

@author: akait
"""

points = {"国語" : 70, "算数" : 35, "英語" : 52}
sum = 0
for key in points:
    sum += points[key]
print(int(sum))