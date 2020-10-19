# -*- coding: utf-8 -*-
"""
Created on Mon Sep 17 18:40:06 2018

@author: Lenovo
"""

# -*- coding: utf-8 -*-
"""
Created on Tue Sep 11 13:56:20 2018

@author: Lenovo
"""

lava_map1 = [
    "      **               **      ",
    "     ***     D        ***      ",
    "     ***                       ",
    "                      *****    ",
    "           ****      ********  ", #1,13
    "           ***          *******",
    " **                      ******",
    "*****             ****     *** ",
    "*****              **          ",
    "***                            ",
    "              **         ******",
    "**            ***       *******",
    "***                      ***** ",
    "                               ",
    "                s              ",# [14,16]
]

lava_map2 = [
    "     **********************    ",
    "   *******   D    **********   ",
    "   *******                     ",
    " ****************    **********",
    "***********          ********  ",
    "            *******************",
    " ********    ******************",
    "********                   ****",
    "*****       ************       ",
    "***               *********    ",
    "*      ******      ************",
    "*****************       *******",
    "***      ****            ***** ",
    "                               ",
    "                s              ",
]

#14,16 naabrid on 14,17  14,15  15,16   13  16

from queue import Queue
from sklearn.neighbors import NearestNeighbors

def minu_otsing(kaart):
    # leia start, näiteks tuple kujul (x, y)

    start = (0,0)
    length = len(kaart)
    width = len(kaart[0])

    for i in range(length):
        for j in range(width):
            if kaart[i][j] == "s":
                start = (i,j)
                break
    print("Start: ", start)

    frontier = Queue()
    frontier.put(start)
    came_from = {}
    came_from[start] = None
    path = Queue()
    teemant = (0,0)
    graph = {}
    breaking = False
    while not frontier.empty():
        current = frontier.get()
        neighbors = [(current[0]+1,current[1]),(current[0],current[1]-1),
                    (current[0],current[1]+1),(current[0]-1,current[1])]

        set1 = {()}
        for next in neighbors:
            if next not in came_from and next[0] < length and next[1] < width and next[0] > 0 and next[1] > 0:

                if kaart[next[0]][next[1]] is "D":
                     set1.add(next)
                     frontier.put(next)
                     came_from[next] = current
                     teemant = next
                     graph.update({current:set(set1)})
                     breaking = True
                elif kaart[next[0]][next[1]] == " " and breaking == False:
                    set1.add(next)
                    frontier.put(next)
                    came_from[next] = current
                    graph.update({current:set(set1)})

    curr =  teemant
    path = []
    
    path.append(curr)
    while curr != start:
        last,curr1 = graph.popitem()
        graph.update({last:curr1})
        if last == start:
            curr = start
            path.append(start)
        if curr in curr1:
            path.append(last)
            curr = last
        last,curr1 = graph.popitem()

    return path

path = minu_otsing(lava_map2)
print("Lahendus: ")
print(path)
print("Lahendus algusest:")
print(path[::-1])
#for i in path:
    #print(i)