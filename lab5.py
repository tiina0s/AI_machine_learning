# -*- coding: utf-8 -*-
"""
Created on Tue Oct  2 14:17:41 2018

@author: Lenovo
"""

import search
import itertools
import pandas as pd
import numpy as np


class TSP(search.Problem):
    matrix1 = []
    state = []
    
    def __init__(self, instance):
        inistate = []
        
        matrix = open(instance+".txt").read()[3:]
        matrix = [item.split() for item in matrix.split('\n')[:-1]]
        self.matrix1 = matrix
        print(matrix)
        
        with open(instance+".txt") as f:
            
            lines = f.readline()
            for i in range(0,int(lines)):
                inistate.append(i)
            self.initial = inistate     
        
        # laadi sisse ülesanne sobival kujul
        # genereeri algolek (võib olla list linnade indeksitest)

    def opt2Swap(self,route, i, k):
        print("i, ", i)
        print("k, ", k)
        assert i >= 0 and i < (len(route) - 1)
        assert k < len(route)
        new_route = route[0:i]
        new_route.extend(reversed(route[i:k + 1]))
        new_route.extend(route[k+1:])
        print(len(new_route),len(route))
        assert len(new_route) == len(route)
        return new_route
       #take route[0] to route[i-1] and add them in order to new_route
       #take route[i] to route[k] and add them in reverse order to new_route
       #take route[k+1] to end and add them in order to new_route

    def actions(self, state):
        actions = []
        for i in range(0,len(state)):
            if (i == len(state)-1):
                new=(0,state[i])
                actions.append(new)
            else:
                new=(state[i],state[i+1])
                actions.append(new)
        print("actions: ",actions)

        # siin genereerime võimalikud lahti ühendatavate graafi kaarte paarid 2-Opt jaoks
        print(state)
        return actions
    
    def result(self, state, action):
        # siin tekitame uue oleku, kus mingid kaared lahti ühendatakse ja teistpidi kokku ühendatakse, kasutades ülalolevat pseudokoodi.
        # action on üks i, j paar.

        actions = (action[1],action[0])
        o1 = action[0]
        o2 = action[1]
        new_route = self.opt2Swap(state, o1,o2)
     #   print("new route:",new_route)
        #self.state = new_route
        return new_route
    
    def cost(self, state):
        # arvuta (või leia muul viisil) praeguse marsruudi kogupikkus. Ära unusta, et marsruut on suletud.
        cost = 0
      #  print(self.matrix1[1][1])
        for i in range(0,len(state)-1):
            
          #  print(i,"cost",self.matrix1[state[i]][state[i+1]])
            cost = cost + int(self.matrix1[i][i+1])
       # print(cost)
         
        return cost
    def value(self, state):
        # kuna valmis otsingufunktsioonid arvavad, et mida suurem väärtus, seda parem, siis meie minimeerimisülesande TSP
        # lahendamiseks tuleb teepikkusest pöördväärtus võtta.
        return 1/(self.cost(state)+1)
    
    
   
p = search.InstrumentedProblem(TSP("gr17"))
g = search.simulated_annealing(p)
#g = search.simulated_annealing(p, search.exp_schedule(limit=10000))
#g = search.hill_climbing(p)
print("p",p)
print("g",g)
print(g.state)
print(p.cost(g.state))