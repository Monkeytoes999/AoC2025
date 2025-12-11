import math
import numpy as np
from scipy.optimize import milp, LinearConstraint
from collections import deque

mp = []

totalPresses = 0
minSum = 0

#Part 1: 1:25:34.37 | I wrote the stupidest version of a BFS you could imagine instead of being smart, and thus got a dumb off by whatever error.
#Part 2: 50:01.11 | 26:45.44 [Took a break between sessions because I started at midnight and needed to sleep, but was given the hint of linalg between sessions which decreased working time significantly. Was getting there, but it still would have taken me a while.]

def toggleState(state, buttons):
    newState = state[:]
    for but in buttons:
        if newState[int(but)] == ".":
            newState[int(but)] = "#"
        else:
            newState[int(but)] = "."
    return newState

# with open('inputs/testcase.txt', 'r') as file:
with open('inputs/10input.txt', 'r') as file:
    for line in file:
        ln = line.strip()
        segments = ln.split(" ")
        diagram = segments[0].removeprefix("[").removesuffix("]")
        buttons = []
        i = 1
        while (segments[i][0] == "("):
            buttons.append(list(map(int, segments[i][1:len(segments[i]) - 1].split(","))))
            i += 1
        joltage = segments[i].removeprefix("{").removesuffix("}").split(",")

        minPresses = len(buttons) + 1
        goal = list(diagram)
        
        start = ["."]*len(diagram)
                
        q = deque([(start, 0)])
        visited = set()
        visited.add(tuple([0]*len(diagram)))
        
        while q:
            next = q.popleft()
            state = next[0]
            numPresses = next[1]
                        
            if all(state[i] == goal[i] for i in range(len(state))):
                totalPresses += numPresses
                break
                        
            for but in buttons:
                newState = toggleState(state, but)
                tupleState = tuple(newState)
                
                if tupleState not in visited:
                    visited.add(tupleState)
                    q.append((newState, numPresses + 1))
            
        buttonArray = []
        for i in range(len(joltage)):
            butVals = [0]*len(buttons)
            for j in range(len(buttons)):
                if i in buttons[j]:
                    butVals[j] = 1
            buttonArray.append(butVals[:])
        
        goal = [int(x) for x in joltage]
        
        a = np.array(buttonArray)
        b = np.array(goal)
        c = np.ones(a.shape[1])
        integrality = np.ones(a.shape[1])
        
        constraint = LinearConstraint(a, b, b)
        
        res = milp(c=c, constraints=constraint, integrality=integrality)
        
        for v in res.x:
            minSum += int(round(v))
            

print(f"Min Button Presses for Initialization: {totalPresses}") #Part 1
print(f"Min Button Presses for Configuration: {minSum}") #Part 2