# -*- coding: utf-8 -*-
"""
Created on Mon Oct  1 13:45:50 2018

@author: Lenovo
"""

import search
import copy

class EightPuzzle(search.Problem):
    def actions(self, state):
        actions = []
        if self.goal_test(state) == False:
            zero = state.index(0)
            row = zero // 3
            col = zero % 3
            if row == 0:
                actions.append('down')
            elif row == 1:
                actions.append('up')
                actions.append('down')
            elif row == 2:
                actions.append('up')
            if col == 0:
                actions.append('right')
            elif col == 1:
                actions.append('right')
                actions.append('left')
            elif col == 2:
                actions.append('left')
        return actions

    def result(self, state, action):
        new_state = list(copy.deepcopy(state))
        zero = state.index(0)
        if action == 'up':
            new_state[zero] = state[zero-3]
            new_state[zero-3] = 0
        elif action == 'down':
            new_state[zero] = state[zero+3]
            new_state[zero+3] = 0
        elif action == 'right':
            new_state[zero] = state[zero+1]
            new_state[zero+1] = 0
        elif action == 'left':
            new_state[zero] = state[zero-1]
            new_state[zero-1] = 0
     
        return tuple(new_state)
        
    def goal_test(self, state):
        return self.goal == state
 
    def path_cost(self, c, state1, action, state2):
        return c + 1   
    
goal = (1, 2, 3, 4, 5, 6, 7, 8, 0)

inistate = (1, 2, 3, 7, 0, 5, 8, 4, 6)
inistate2 = (1, 8, 2, 0, 4, 3, 7, 6, 5 )
inistate3 = (5, 4, 0, 6, 1, 8, 7, 3, 2 )
inistate4 = ( 8, 6, 7, 2, 5, 4, 3, 0, 1  )

problem = EightPuzzle(inistate, goal)

print(search.compare_searchers([problem, EightPuzzle(inistate2,goal)], ["Strateegia", inistate, inistate2],
                      searchers=[search.depth_first_graph_search]))

#search.compare_searchers([problem], ["Strateegia", inistate],
 #                     searchers=[search.depth_first_graph_search])

#search.compare_searchers([problem], ["Strateegia", inistate3],
 #                     searchers=[search.iterative_deepening_search])

goalnode = search.breadth_first_graph_search(problem)

# sammud (tegevused, käigud) algolekust lõppolekuni
print(goalnode.solution())
# olekud algolekust lõppolekuni
print(goalnode.path())
