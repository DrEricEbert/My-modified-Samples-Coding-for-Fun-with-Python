# -*- coding: utf-8 -*-
"""
Created on Mon Nov 18 23:48:28 2019

@author: wohnzimmer
"""

import random
l = [random.randint(0,1000) for i in range(500)]
print(l)

def quicksort(liste):
    if len(liste) <= 1:
        return liste
    pivotelement = liste.pop()
    links = [element for element in liste if element < pivotelement]
    rechts = [element for element in liste if element >= pivotelement]
    return quicksort(links) + [pivotelement] + quicksort(rechts)

s=quicksort(l)
print(s)