# -*- coding: utf-8 -*-
"""
Created on Sun Dec  2 20:24:06 2018

@author: Lenovo
"""

states = ('E','M','F')

observations = ('H','L','N')

start_probability = {'E' : 1/3, 'M' : 1/3, 'F':1/3}

transition_probability = {
   'E' : {'E': 0.6, 'M': 0.2,'F':0.2},
   'M' : {'E': 0.01, 'M': 0.8,'F':0.19},
   'F' : {'E': 0.01, 'M': 0.09,'F':0.9},
   }

emission_probability = {
   'E' : {'H': 0.1, 'L': 0.5, 'N': 0.4},
   'M' : {'H': 0.3, 'L': 0.4, 'N': 0.3},
   'F' : {'H': 0.8, 'L': 0.19, 'N': 0.01},
   }

AB = ('L', 'N', 'N', 'L', 'H', 'N', 'N', 'N', 'N', 'N', 'N', 'H')
BC = ('N', 'H', 'L', 'L', 'L', 'N', 'L', 'N', 'L', 'N', 'N', 'L')
CA = ('H', 'L', 'H', 'N', 'N', 'L', 'H', 'N', 'L', 'L', 'L', 'N')

def p(A,B,row,col):
    p = emission_probability[row][A] * emission_probability[col][B] * start_probability[row] * transition_probability[row][col]
    
    return(p)
    
def calcP(A,B):
    pAB = 0
    for i in range(9):
        row = i//3
        col = i%3
        if (row == 0): rowS = 'E'
        if (row == 1): rowS = 'M'
        if (row == 2): rowS = 'F'
        if (col == 0): colS = 'E'
        if (col == 1): colS = 'M'
        if (col == 2): colS = 'F'
        
        pAB = pAB + p(A,B,rowS,colS)
    return pAB
    
def calc(c):
    p = 0
    for i in range(len(c)-1):
        p1 = calcP(c[i],c[i+1])
        p = p + p1
        
    print(c, ":", p)
    
calc(CA)