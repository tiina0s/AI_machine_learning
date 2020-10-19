# -*- coding: utf-8 -*-
"""
Created on Tue Oct 30 14:28:27 2018

@author: Lenovo
"""
# kõikide numbriga ruutude peal kutsun välja cnf_sweeper()
# enne peab olema teada kinniste naabrite list

class EmptyClause:
    def __eq__(self, other):
        return isinstance(other, EmptyClause)

  
def cnf_sweeper(m, neighbors):
    """CNF komponent ühe ruudu kohta 
    parametrid: m - miinide arv
            neighbors - naabrite list"""
    n = len(neighbors)
    cnf = []
    for i in range(2**n):
        binform = "{:0{n}b}".format(i,n=n)
        ones = 0
        clause = []
        for j in range(n):
            if binform[j] == "1":
                ones += 1
                clause.append(-neighbors[j])
            else:
                clause.append(neighbors[j])    
        if ones != m:
            cnf.append(tuple(clause))
            print(binform, ones, clause)
        
            
    return(cnf)
def removeFrom(c):
 
    listC = []
    c1 = list(set(c))
    for i in range(len(c)):
        if -c[i] not in c1:
            listC.append(c[i])

    return list(set(listC))        
    
def resolve(ci,cj):

    resolvent = []
  
    cii = removeFrom(ci)
    cjj = removeFrom(cj)
    #print("ci",ci)
   #print("cii",cii)
    #print("cj",cj)
    #print("cjj",cjj)
    for i in range(len(cii)):

        if cii[i] not in resolvent and -cii[i] not in cjj :
            resolvent.append(cii[i])

    for i in range(len(cjj)):

        if cjj[i] not in resolvent and -cjj[i] not in cii :
            resolvent.append(cjj[i])
    print(ci,cj)
    print("res")
    print(resolvent)
    if len(resolvent) > 1 and resolvent[1] == -resolvent[0]:
        return(())
    resolvent = tuple(resolvent) 
    return(resolvent)           
                
def resolution_entails(kb, alpha):
    # kb - teadmusbaas CNF kujul
    # alpha - literaal, mida tahame kontrollida.
    clauses = []
    for i in range(len(kb)):
    #    print(kb[i])
        kt = []
        for j in range(len(kb[i])):
           
            kt.append(kb[i][j])
        kt.append(-alpha)
        kt = tuple(kt)
        clauses.append(kt)
                    # ALPHA LISADA OIGESTI
      #  clauses.append(cnf_sweeper(-alpha,[1,2,5,7,8]))
    clauses = set(clauses)
    print(clauses)
    while True:
        new = set()
    #   print(clauses)
        print("")
        for ci in clauses:
            for cj in clauses:
                if ci != cj:
                    resolvent = resolve(ci,cj)
                   # print(ci,cj)
                    if () == resolvent:
                        return True
                    new = resolvent
                    print("New")
                    print(new)
       # return False
     #   print(clauses)
      #  print("New")
      #  print(new)
        if new.issubset(clauses): ## KAS LISAB SIIA OIGESTI
           # print(new)
            return False
        clauses = list(clauses)
        clauses2 = set()
        clauses2.add(tuple(new))
        clauses = clauses2
        #clauses = set(clauses)
    #print(clauses)
    
test = cnf_sweeper(1,[2,4,5])
test2 = cnf_sweeper(1,[1,3,4,5,6])
test3 = cnf_sweeper(0,[2,5,6])
test4 = cnf_sweeper(1,[1,2,3,4,6,7,8,9])
test5 = cnf_sweeper(1,[4,5,8])
test6 = cnf_sweeper(1,[4,5,6,7,9])
test7 = cnf_sweeper(0,[5,6,7])

cnf = test + test2 + test3 + test4 + test5 + test6 + test7

print(resolution_entails(cnf,-2))

