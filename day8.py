import math
import numpy as np
from scipy.spatial.distance import cdist
mp = []

#Part 1: 48:17.43
#Part 2: 2:37.29

# with open('inputs/testcase.txt', 'r') as file:
with open('inputs/8input.txt', 'r') as file:
    for line in file:
        ln = line.strip()
        coords = ln.split(',')
        mp.append([int(coords[0]), int(coords[1]), int(coords[2])])
        
numConnections = 1000 #1000 for input, 10 for test cases
distances = cdist(mp, mp)

distObj = {}
minDistances = []

for i in range(len(distances)):
    v = distances[i]
    v.sort()
    distObj[i] = list(v[2:])
    minDistances.append(v[1])
    
indices = list(range(len(minDistances)))

groupings = []
for i in range(len(minDistances)):
    groupings.append([i])

p1 = 0
p2 = 0
j = 0
while(len(groupings) > 1):
    combined = zip(minDistances, indices)
    sortedCombined = sorted(combined)
    sortedDistances, sortedIndices = zip(*sortedCombined)
    sortedDistances = list(sortedDistances)
    sortedIndices = list(sortedIndices)
    
    p1, p2 = sortedIndices[0], sortedIndices[1]
    minDistances[p1] = distObj[p1].pop(0)
    minDistances[p2] = distObj[p2].pop(0)
    
    g1 = []
    g2 = []
    for g in groupings:
        if p1 in g:
            g1 = g
        if p2 in g:
            g2 = g
            
    if (g1 != g2):
        groupings.remove(g1)
        groupings.remove(g2)
        groupings.append(g1 + g2)
    j += 1
    
    #Part 1
    if j == numConnections:
        sizes = []
        for i in range(len(groupings)):
            sizes.append(len(groupings[i]))

        sizes = sorted(sizes, reverse=True)
        print(f"Three Largest Circuits after {numConnections} connections: {sizes[0] * sizes[1] * sizes[2]}")
    
print(f"Product of X Coords of last connection: {mp[p1][0] * mp[p2][0]}")