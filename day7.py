import math
import copy
mp = []

splitCount = 0
worlds = 0

#Part 1: 9:23.31
#Part 2: 33:41.05

# with open('inputs/testcase.txt', 'r') as file:
with open('inputs/7input.txt', 'r') as file:
    for line in file:
        ln = line.strip()
        mp.append(list(ln)) 
     
dupMap = copy.deepcopy(mp)
for i in range(len(mp)):
    for j in range(len(mp[0])):
        if mp[i][j] == "S":
            mp[i+1][j] = "|"
        elif mp[i][j] == "|" and i < (len(mp) - 1):
            if mp[i+1][j] == "^":
                splitCount += 1
                if j > 0 and mp[i+1][j-1] != "|":
                    mp[i+1][j-1] = "|"
                if j < (len(mp[i]) - 1) and mp[i+1][j+1] != "|":
                    mp[i+1][j+1] = "|"
            else:
                mp[i+1][j] = "|"
                    
# I tried recursion, and like yeah, it works, but it's NOT a good method for the # of 'worlds' the program goes through (390684413472684) and probably eats a LOT of memory.
# def recursiveSplit(map):
#     global worlds
#     for i in range(len(map)):
#         for j in range(len(map[0])):
#             if map[i][j] == "S":
#                 map[i+1][j] = "|"
#             elif map[i][j] == "|" and i < (len(map) - 1):
#                 if map[i+1][j] == "^":
#                     leftOccupied = (False if j == 0 else map[i+1][j-1] == "|")
#                     rightOccupied = (False if j == (len(map[i]) - 1) else map[i+1][j+1] == "|")
#                     if (not leftOccupied and not rightOccupied):
#                         if j > 0 and map[i+1][j-1] != "|":
#                             leftMap = copy.deepcopy(map)
#                             leftMap[i+1][j-1] = "|"
#                             recursiveSplit(leftMap)
#                         if j < (len(map[i]) - 1) and map[i+1][j+1] != "|":
#                             rightMap = copy.deepcopy(map)
#                             rightMap[i+1][j+1] = "|"
#                             recursiveSplit(rightMap)
#                 else:
#                     map[i+1][j] = "|"
#             elif (map[i][j] == "|" and i == (len(map) - 1)):
#                 worlds += 1
# recursiveSplit(dupMap)
    
for i in range(len(dupMap[0])):
    dupMap[len(dupMap) - 1][i] = 1

for i in range(len(dupMap) - 2, -1, -1):
    for j in range(len(dupMap[0])):
        if dupMap[i][j] == "^":
            if j == 0:
                lSide = 0
            else:
                k = i + 1
                while dupMap[k][j - 1] == ".":
                    k += 1
                lSide = dupMap[k][j - 1]
            if j == (len(dupMap[0]) - 1):
                rSide = 0
            else:
                k = i + 1
                while dupMap[k][j + 1] == ".":
                    k += 1
                rSide = dupMap[k][j + 1]
            dupMap[i][j] = lSide + rSide
            worlds = lSide + rSide
    
# Logging    
print(f"Splits [Non-Quantum]: {splitCount}")
print(f"Worlds: {worlds}")

