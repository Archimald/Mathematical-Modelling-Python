# -*- coding: utf-8 -*-
"""
Created on Tue Sep  1 17:19:27 2015

@author: Michael J. Currie
"""

from pylab import *

def effectiveAnnualRate(apr, period):
    if apr > 1:
        apr = apr/100
    cyclesPerYear = 12;
    if isinstance(period, str):
        period = period.lower();
        if period == "annually":
            cyclesPerYear = 1;
        elif period == "semi-annually":
           cyclesPerYear = 2;
        elif period == "quarterly":
            cyclesPerYear = 4;
        elif period == "monthly":
            cyclesPerYear = 12;
        elif period == "weekly":
            cyclesPerYear = 52;
        elif period == "daily":
            cyclesPerYear = 365;
    else:
        cyclesPerYear = period;
        
    rate = apr/cyclesPerYear + 1;
    
    effectiveRate= pow(rate, cyclesPerYear);
    return ((effectiveRate-1)*100);
    
    
def effectiveAnnualRateGraph(apr):
    
    cyclesList = [1,2,4,12,52,365];
    rateGraphList = []
    
    for cycle in cyclesList:
        rateGraphList.append(effectiveAnnualRate(apr, cycle));
    
    figure();
    plot(cyclesList, rateGraphList, "ro:");
    
    

