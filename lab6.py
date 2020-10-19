# -*- coding: utf-8 -*-
"""
Created on Tue Oct  9 14:38:59 2018

@author: Lenovo
"""

import games

class BearGame(games.Game):    
    
    initial = {"To move:":"bear","Bear position:":"B2","Hunters position:":"A1 B1 C1"} 
    bear_moves = 0
    hunters_moves = 0
    def __init__(self):
        # algseis jne initsialiseerimine
     #   initial = {"A1":"E","B1":"H1","C1":"H2","D1":"H3","E1":"E",
      #           "B2":"E","C2":"E","D2":"E","A3":"E","B3":"E","C3":"B",
       #          "D3":"E","E3":"E","B4":"E","C4":"E","D4":"E","A5":"E",
        #         "B5":"E","C5":"E","D5":"E","E5":"E"}
   #     initial = {"A1":"H1","B1":"H2","C1":"H3","A2":"E","B2":"B","C2":"E",
    #               "A3":"E","B3":"E","C3":"E"}
        #state = ("A1","B1","C1","A2","B2","C2","A3","B3","C3")
        bear_moves = 0
        hunters_moves = 0
        state = {"A1":["B1","A2"],
         "B1":["A1","B2","C1"],
         "C1":["B1","C2"],
         "A2":["A1","B2","A3"],
         "B2":["A2","B1","C2","B3"],
         "C2":["B2","C1","C3"],
         "A3":["A2","B3"],
         "B3":["A3","B2","C3"],
         "C3":["B3","C2"]}
        print(state)
        print("init")
       # self.bear_moves = bear_moves
       # self.hunters_moves = hunters_moves
        self.state = state
        #self.initial = initial
    def to_move(self, state):
      #  return("bear")
        return(state["To move:"])
        # otsusta, kuidas karu ja jahimeeste 
        #poolt tähistada ja tagasta, kumb pool käigul on
        
     #   for i in state:
      #      print(i)
       #     if i == "H1":
        #        print("H1 on siin")
        #print("to move")        
    def generate_edges(self,graph):
        edges = []
        for node in graph:
            for neighbour in graph[node]:
                edges.append((node, neighbour))
    
        return edges

                                                                      
    def actions(self, state):
        #available moves: [('C3', 'B3'), ('C3', 'D3'), ('C3', 'C2'), ('C3', 'C4')]
       # print("STATE")
       # print(self.state)
       # if self.terminal_test(state):
        #    print("M2ng l2bi")
         #   return(False)
        actions = []
        hunters_pos = state.get("Hunters position:")
        bear_pos = state.get("Bear position:")

        if state["To move:"] == "bear":
            all_edges = self.generate_edges(self.state) 
            for edge in all_edges:
                if (edge[0] == bear_pos):
                    if edge[1] not in hunters_pos:
                        actions.append(edge)
        else:
         #   print("kyti kord")
            hunters_pos = state.get("Hunters position:")
          #  print(hunters_pos)
            all_edges = self.generate_edges(self.state) 
            for edge in all_edges:
                if (edge[0] in hunters_pos):

                    if (edge[1] not in hunters_pos and edge[1] != bear_pos):
                        actions.append(edge)
        return actions

    def result(self, state, action):
        if self.terminal_test(state):
            print("M2ng l2bi")
            return(False)
        all_keys = state.keys()
        
        whose_turn = state.get("To move:")
        bear_pos = state.get("Bear position:")
        hunters_pos = state.get("Hunters position:")
        print("whose")
        print(whose_turn)
        print(action)
        if whose_turn == "bear":
            self.bear_moves += 1
            state["To move:"] = "hunter"  
            state["Bear position:"] = action[1]
        
        else:
            self.hunters_moves += 1
            state["To move:"] = "bear"
            state["Hunters position:"] = state["Hunters position:"].replace(action[0],action[1])
            print(state["Hunters position:"])
        return state
                

        print("result")
    def utility(self, state, side):
        print("side")
        print(side)
        if side == "bear":
            print("bear moves")
            print(self.bear_moves)
            return self.bear_moves
        else:
            return self.hunters_moves
        # mis on seisu väärtus antud poole jaoks (ei võrdu alati
        #   sellega, kelle käik antud seisus on)
        # täidab ka eval() funktsiooni rolli

    def terminal_test(self, state):
        # siin peaks ära tundma, kas karu on lõksu aetud
        if self.actions(state) == []:
            return(True)
        
bg = BearGame()
#state = {"A1":"E","B1":"H1","C1":"H2","D1":"H3","E1":"E",
#                 "B2":"E","C2":"E","D2":"E","A3":"E","B3":"E","C3":"B",
#                 "D3":"E","E3":"E","B4":"E","C4":"E","D4":"E","A5":"E",
#                 "B5":"E","C5":"E","D5":"E","E5":"E"}

#state = {"A1":["B1","A2"],
 #        "B1":["A1","B2","C1"],
  #       "C1":["B1","C2"],
   #      "A2":["A1","B2","A3"],
    #     "B2":["A2","B1","C2","B3"],
     #    "C2":["B2","C1","C3"],
       #  "A3":["A2","B3"],
      #   "B3":["A3","B2","C3"],
        # "C3":["B3","C2"]}
state = {"To move:":"bear","Bear position:":"B2","Hunters position:":"A1 B1 C1"}     
#print(state)
bg.play_game(games.query_player,
             games.random_player)



def alphabeta_depth8(game, state):
    return games.alphabeta_cutoff_search(state, game, d=8)

bg.play_game(games.query_player,
              alphabeta_depth8)