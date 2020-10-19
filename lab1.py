# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

def vacworld_sim(ini_state={}, steps=10):
    performance = {"puhtus":0, "energia":10}
    for step in range(steps):
        # call agent program with data about the current environment
        percepts = {"asukoht":ini_state["asukoht"], "puhtus":ini_state["ruum" + ini_state["asukoht"]]}
        #action = reflex_agent(percepts)
        if step == 0:
            agent_state = {"ruumA":"ei tea", "ruumB":"ei tea"}
        action, agent_state = state_reflex_agent(percepts, agent_state)     # mäluga agent
        #action = reflex_agent(percepts) # tavaline agent
        print(step, ", Tolmuimeja asub ruumis: ", ini_state["asukoht"], " tegevus: ", action)
        # perform agent action (update world state)
        if action == "Suck" :
            performance = {"puhtus":performance["puhtus"]+1, "energia":performance["energia"]-1}
            if ini_state["asukoht"] == "A":
                ini_state = {"asukoht":ini_state["asukoht"], "ruumA":"puhas", "ruumB":ini_state["ruumB"]}
            else:
                ini_state ={"asukoht":ini_state["asukoht"], "ruumA":ini_state["ruumA"], "ruumB":"puhas"}
        elif action == "Right":
            performance = {"puhtus":performance["puhtus"], "energia":performance["energia"]-1}
            ini_state = {"asukoht":"B", "ruumA":ini_state["ruumA"], "ruumB":ini_state["ruumB"]}
        elif action == "Left":
            performance = {"puhtus":performance["puhtus"], "energia":performance["energia"]-1}
            ini_state = {"asukoht":"A", "ruumA":ini_state["ruumA"], "ruumB":ini_state["ruumB"]}
            
    print("kokkuvõttes performance: puhtus:", performance["puhtus"], "/2, energia: ", performance["energia"], "/10")
    if performance["puhtus"] == 2:
        print("kõik on puhas")
    else:
        print("pole puhtust")
    if (performance["energia"]) <= 6:
        print("energiat kulus palju")
    else:
        print("energiat kulus vähe")
    return ini_state

def state_reflex_agent(percepts, agent_state):
    if percepts["asukoht"] == "A":
        if percepts["puhtus"] == "must":
         action = "Suck"
         agent_state["ruumA"] = "puhas"
        elif percepts["puhtus"] == "puhas" and agent_state["ruumB"] != "puhas":
            action = "Right"
        else:
            action = "NoOp"
    elif percepts["asukoht"] == "B":
        if percepts["puhtus"] == "must":
            action = "Suck"
            agent_state["ruumB"] = "puhas"
        elif percepts["puhtus"] == "puhas" and agent_state["ruumA"] != "puhas":
            action = "Left"
        else:
            action = "NoOp"
    return action, agent_state

def reflex_agent(percepts):

    print(percepts["puhtus"])
# decide action based on environment perception
    
    if percepts["asukoht"] == "A":
        if percepts["puhtus"] == "must":
         action = "Suck"
        elif percepts["puhtus"] == "puhas":
            action = "Right"
    elif percepts["asukoht"] == "B":
        if percepts["puhtus"] == "must":
            action = "Suck"
        elif percepts["puhtus"] == "puhas":
            action = "Left"
    else:
        action = "NoOp"

    
    #print(action)
    return action

test_state = {"asukoht":"A", "ruumA":"must", "ruumB":"must"}

vacworld_sim(test_state)