# -*- coding: utf-8 -*-
"""
Created on Fri Aug 28 13:30:12 2015

@author: Michael J. Currie
"""

from pylab import *

def initialBalance(duration, rate, withdrawal):
    if rate < 1:
        rate +=1
    if rate == 1:
        initialBalance = duration*withdrawal;
    else:
        equilibrium = -withdrawal/(1-rate)
        initialBalance = -equilibrium * (rate) ** (-duration) + equilibrium
    
   
    
    return initialBalance