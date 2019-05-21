#!/usr/bin/python
# -*- coding: utf-8 -*-
import math

myH = [5,12,64,1,37,90,91,97,]

def getLeftSon(pos):
    value = pos * 2 + 1
    try:
        return myH[value], value
    except :
        return float('-inf'),value


def getRightSon(pos):
    value = pos * 2 + 2
    try: 
        return myH[value], value
    except :
        return float('-inf'),value
    
def getMaxSom(j):
    l, vl = getLeftSon(j)
    r, vr = getRightSon(j)
    if l<r:
        return r, vr
    return l, vl

def maxHeap(i):  #i  start postion
    for j in range(i,-1,-1):        
        father = myH[j]
        maxSon, sPos  = getMaxSom(j)
        
        if maxSon > father:            
            myH[j] = maxSon
            myH[sPos] = father
            maxHeap(sPos)
    #print(myH)
    return myH

            
if __name__ == "__main__":
    i = math.ceil(len(myH)/2)-1 #start position
    maxHeap(i)
    print(myH)
