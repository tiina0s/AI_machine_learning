# -*- coding: utf-8 -*-
"""
Created on Tue Nov 20 14:33:56 2018

@author: Lenovo
"""

def loadFile():
    
    file = open("spam.txt", "r") 
    firstLine = file.readline()
    findSpam(firstLine)


def train(wordsInLetter):
    
    file = open("spam.txt", "r") 
    firstLine = file.readline()
    line1 = firstLine.split(',')
    lines = file.readlines()
    dataset = list(lines)
    word = list()
    ramps = list()
    rampsLength = 0 
    
    for line in dataset: # kogu spami hulk
        if line[24] == "1":
            rampsLength = rampsLength + 1
            
    p_ramps = rampsLength/len(dataset)  # P(ramps)
    koguP = p_ramps
    
    pole_ramps = (len(lines) - rampsLength)/len(dataset) # P(pole_ramps)
    koguP_pole_ramps = pole_ramps
    
    for i in range(0,len(line1),1): #leiame nende sonade toenaosused, mis on olemas uues kirjas
     #   print('line1',line1[i])
        if line1[i] in wordsInLetter:
            for line in dataset:
                word.append(line[i])
                ramps.append(line[24])
        
            p1 = p(word,ramps,rampsLength)  
            koguP = koguP * p1
            koguP_pole_ramps = koguP_pole_ramps * p1

    print("kiri pole ramps P()=", koguP_pole_ramps)
    print("kiri on ramps P()=", koguP)
    if (koguP > koguP_pole_ramps):
        print("kiri on ramps")
    else:
        print("kiri pole ramps")

def p(word,ramps,rampsCount):
    wordCount = 0
    for i in range(len(word)):
        if word[i] == "1" and ramps[i] == "1":
            wordCount = wordCount + 1
    p = (wordCount + 1)/(rampsCount + 2)
   
    return p
      
def findSpam(wordsList):
    line = wordsList.split(',')
    file = open("kiri1.txt", "r") 
    words = file.read().split()
    SYMBOLS = '${}()[].,:;+-*/&|<>=~1234567890?_#@\''
    results = []
    for element in words: # kaotame koik symbolid tekstist, loome listi sonadest
        temp = ""
        for ch in element:
            if ch not in SYMBOLS:
                temp += ch
    
        if temp is not '':
            results.append(temp)

    wordsInLetter = [] # leiame need sonad, mis on treeningufailis olemas
    for i in range(len(results)):
        for j in range(len(line)):
            if results[i] == line[j]:
                if results[i] not in wordsInLetter:
                    wordsInLetter.append(results[i])
            
    print("Sonad, mis on ka treeningfailis: ", wordsInLetter)
    getP = train(wordsInLetter) #sel juhul, kas on spam

    
loadFile()



