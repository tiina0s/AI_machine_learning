# -*- coding: utf-8 -*-
"""
Created on Tue Sep 18 13:58:01 2018

@author: Lenovo
"""

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

from queue import Queue, PriorityQueue

def greedy_search(kaart):
    print("Greedy search")
    start = (0,0) #(2,2)
    goal = (0,0)  #(295,257)
    length = len(kaart)
    width = len(kaart[0])

    for i in range(length):
        for j in range(width):
            if kaart[i][j] == "s":
                start = (i,j)
    print("Start: ", start)
    
    for i in range(length-1,0,-1):
        for j in range(width-1,0,-1):
            if kaart[i][j] == "D":
                goal = (i,j)
    print("Goal: ", goal)
    
    frontier = PriorityQueue()
    frontier.put((0, start))
    came_from = {}
    graph = {}
    breaking = False
    came_from[start] = None
    while not frontier.empty():
        _, current = frontier.get()
       # print("curr:",current)
        if current == goal:
            break
        neighbors = [(current[0]+1,current[1]),(current[0],current[1]-1),
                   (current[0],current[1]+1),(current[0]-1,current[1])]
      #  print(neighbors)
        set1 = {()}
        for next in neighbors:
            if next not in came_from and next[0] < length and next[1] < width and next[0] > 0 and next[1] > 0 and kaart[next[0]][next[1]] != "*": #and kaart[next[0]][next[1]] == " ":
                if kaart[next[0]][next[1]] is "D":
                     set1.add(next)
                     priority = heuristic(goal, next)
                     frontier.put((priority,next))
                     came_from[next] = current
                     teemant = next
                     graph.update({current:set(set1)})
                     breaking = True
               # elif kaart[next[0]][next[1]] == "*" and breaking == False:
               #     print("laava: ", next)
                elif kaart[next[0]][next[1]] == " " and breaking == False:
                    set1.add(next)
                    priority = heuristic(goal, next)
                    frontier.put((priority,next))
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

def astar_search(kaart):
    print("Greedy search")
    start = (0,0) #(2,2)
    goal = (0,0)  #(295,257)
    length = len(kaart)
    width = len(kaart[0])
    
    for i in range(length):
        for j in range(width):
            if kaart[i][j] == "s":
                start = (i,j)
    print("Start: ", start)
    
    for i in range(length-1,0,-1):
        for j in range(width-1,0,-1):
            if kaart[i][j] == "D":
                goal = (i,j)
    print("Goal: ", goal)
    
    frontier = PriorityQueue()
    frontier.put((0, start))
    came_from = {}
    graph = {}
    breaking = False
    came_from[start] = None
    cost_so_far = {}
    cost_so_far[start] = 0
    while not frontier.empty():
        _, current = frontier.get()
       # print("curr:",current)
        if current == goal:
            break
        neighbors = [(current[0]+1,current[1]),(current[0],current[1]-1),
                   (current[0],current[1]+1),(current[0]-1,current[1])]
      #  print(neighbors)
        set1 = {()}
        for next in neighbors:
            if next not in came_from and next[0] < length and next[1] < width and next[0] > 0 and next[1] > 0 and kaart[next[0]][next[1]] != "*": #and kaart[next[0]][next[1]] == " ":
                if kaart[next[0]][next[1]] is "D":
                     set1.add(next)
                     priority = heuristic(goal, next)
                     new_cost = cost_so_far[current] + 1
                     if next not in cost_so_far or new_cost < cost_so_far[next]:
                        cost_so_far[next] = new_cost
                        priority = new_cost + heuristic(next, goal)    # g(n) + h(n)
                        frontier.put((priority, next))
                        came_from[next] = current
                     teemant = next
                     graph.update({current:set(set1)})
                     breaking = True

                elif kaart[next[0]][next[1]] == " " and breaking == False:
                    set1.add(next)
                    priority = heuristic(goal, next)
                    new_cost = cost_so_far[current] + 1
                    if next not in cost_so_far or new_cost < cost_so_far[next]:
                        cost_so_far[next] = new_cost
                        priority = new_cost + heuristic(next, goal)    # g(n) + h(n)
                        frontier.put((priority, next))
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
                
def heuristic(node, goal):
    # Manhattan distance on a square grid
    return abs(node[0] - goal[0]) + abs(node[1] - goal[1])

with open("cave300x300") as f:
    map_data = [l.strip() for l in f.readlines() if len(l)>1]

#path = greedy_search(map_data)
path = astar_search(map_data)

print("Lahendus algusest:")
print(path[::-1])
print(len(path))