#!/usr/bin/python
# -*- coding: utf-8 -*-
import math

#myH = [90,60,40,12,3,15,18]
myH = [5,12,64,1,90,37,91,97]
#myH = [5,12,64,1,37,90,91,97]


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
    return myH

def insertHeap(elemt):
    myH.append(elemt)
    i2 = math.ceil(len(myH)/2)-1
    if getLeftSon(i2)[0] < getRightSon(i2)[0]:
        return  myH
    return maxHeap(i2)
    
#Solo remover el root, pues como el Heap es una cola de prioridad y  el root tiene el mayor valor, entonces no se necesita remover otro que no sea el root 
def remove():
    if len(myH) == 1:
        del myH[0]
        return 
    #Swap con el ultimo elemento del array
    myH[0], myH[ len(myH)-1] = myH[ len(myH)-1] , myH[0]
    del myH[ len(myH)-1 ]
    i = math.ceil(len(myH)/2)-1    
    maxHeap(i)
               
if __name__ == "__main__":
    i = math.ceil(len(myH)/2)-1 #start position
    maxHeap(i)
    print(myH)
    insertHeap(8)
    print(myH)
