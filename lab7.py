# -*- coding: utf-8 -*-
"""
Created on Sat Oct 27 21:57:33 2018

@author: Lenovo
"""

def fc_entails(kb, q):
    # kb - teadmusbaas mingil kujul
    # q - loogikamuutuja e. sümbol, mille kohta tahame teada, kas see järeldub kb-st
    # 3 tabelit: agenda, count ja inferred

    agenda = []

    count = [None] * len(kb)
    for i in range(len(kb)):
        j = [kb[i],len(kb[i])-1]
        count[i] = j 
        if len(kb[i]) == 1:  # lisada ainult viimased elemendid, mis on teada
            agenda.append(kb[i][0])
    inferred = [None] * len(agenda)
    for i in range(len(agenda)):
        j = agenda[i],False
        inferred[i] = j
    while (len(agenda) != 0):
        p = agenda.pop()

        istrue = True
        # tahe leidmine, kas on false ikka
        for i in range(len(inferred)):
            if inferred[i][0] == p:
                if inferred[i][1] == False:
                    istrue = False
       
        if istrue == False:
            
            for j in range(len(inferred)):
                if inferred[j][0] == p:
                    inferred = list(inferred)
                    inferred[j] = [p,True]
                    inferred = tuple(inferred)
            t = -1
            # for each horn clause c in kb
            for c in kb:

                t = t + 1    
                if p in c:

                    if (len(c) > 1 and c[0] == c[1]):
                        count[t][1] = count[t][1] - 2 # kui 1. ja 2. kaik on sama, siis lahutame 2
                    else:
                        count[t][1] = count[t][1] - 1

                    isInferred = 0
                    if count[t][1] == 0: # kui koik eeldused on taidetud
                        for i in inferred:
                            if i[0] == c[0]:
                                isInferred = i[1]

                        if c[-1] == q and isInferred == True:
                            return(True)

                        inferred= list(inferred)
                        inferred = tuple(inferred)
    return(False)

def fc_entails0(kb, q):
    agenda = []
    
    count = [None] * len(kb)
    for i in range(len(kb)):
        j = [kb[i],len(kb[i])-1]
        count[i] = j 
        if len(kb[i]) == 1:
            agenda.append(kb[i][0])
    inferred = [None] * len(agenda)
    for i in range(len(agenda)):
        j = agenda[i],False
        inferred[i] = j

    while (len(agenda) != 0):
        p = agenda.pop()
        istrue = True
        for i in range(len(inferred)):
            if inferred[i][0] == p:
                if inferred[i][1] == False:
                    istrue = False
                    
        if istrue == False:
            for j in range(len(inferred)):
                if inferred[j][0] == p:
                    inferred = list(inferred)
                    inferred[j] = [p,True]
                    inferred = tuple(inferred)
            t = -1
            for c in kb:
                t = t + 1    
                if p in c:
                    
                    #if (count[t][1] != 0):
                    count[t][1] = count[t][1] - 1
                    print(count)
                    print("t1")
                    print(count[t][1])
                    print(count[t][0])
                    if count[t][1] == 0:
                        print("C")
                        print(c)
                        if c[-1] == q and c[0] != q:
                            return(True)
                        agenda.append(c[-1])
                        inferred= list(inferred)
                        k = [c[-1],False]
                        inferred.append(k)
                        inferred = tuple(inferred)
    return(False)

l1 = ["P","Q"]
l2 = ["L","M","P"]
l3 = ["B","L","M"]
l4 = ["A","P","L"]
l5 = ["A","B","L"]
l6 = ["A"]
l7 = ["B"]
list1 = [l1,l2,l3,l4,l5,l6,l7]

k1 = "Q"

print(fc_entails0(list1,k1))

t1 = ["kivi","kivi", "paber"]
t4 = ["paber","paber","kaarid"]
t7 = ["kaarid","kaarid","kivi"]

t2 = ["kivi","paber","kivi"]
t3 = ["kivi","kaarid","kaarid"]
t5 = ["paber","kivi","kivi"]
t6 = ["paber","kaarid","paber"]
t8 = ["kaarid","kivi","kaarid"]
t9 = ["kaarid","paber","paber"]

# lisada kaardi, paber. 

def kkp(a,b):
    facts = []

    j = [a,b]
    
    if a == b:
        facts = [t1,t4,t7]
    else:
        facts = [t2,t3,t5,t6,t8,t9]
    facts.append([a])
    if (a != b):
        facts.append([b])
  #  print(facts)
    print(a,",",b)
    print("paber: ", fc_entails0(facts,"paber"))
    print("kivi: ", fc_entails0(facts,"kivi"))  
    print("kaarid: ", fc_entails0(facts,"kaarid"))
    
    
    
#kkp("kivi","kivi")
print("")
#kkp("paber","paber")
print("")
#kkp("kaarid","kaarid")

print("")
kkp("kivi","paber")
print("")
#kkp("kivi","kaarid")
print("")
#kkp("paber","kivi")
print("")
#kkp("paber","kaarid")
print("")
#kkp("kaarid","kivi")
print("")
#kkp("kaarid","paber")
