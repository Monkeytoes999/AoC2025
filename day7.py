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
# I also recognize now that this is a BAD recursive approach. I have implemented a much better recursive solution below.
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

# And this recursion WORKS. You just don't be an idiot and you can make a good recursive function. I have a tendancy to overcomplicate my solutions.
# visited = {}
# def calculatePath(x, y):
#     if (y == len(dupMap) - 1):
#         return 1
#     elif ((x, y) in visited):
#         return visited[(x, y)]
#     elif (dupMap[y][x] == "^"):
#         out = 0
#         out += calculatePath(x - 1, y + 1)
#         out += calculatePath(x + 1, y + 1)
#         visited[(x, y)] = out
#         return out
#     else:
#         out = calculatePath(x, y + 1)
#         visited[(x, y)] = out
#         return out

# for y in range(len(dupMap)):
#     for x in range(len(dupMap[0])):
#         if dupMap[y][x] == "S":
#             worlds = calculatePath(x, y)
#             print(f"Worlds: {worlds}")
#             break
    
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

