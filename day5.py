import math
mp = []
uRs = []
lRs = []

fresh = 0
rangesDone = False
possibleFresh = 0

#Part 1: 14:19.30
#Part 2: 1:09:41.77

# with open('inputs/testcase.txt', 'r') as file:
with open('inputs/5input.txt', 'r') as file:
    for line in file:
        ln = line.strip()
        if (ln == ""):
            rangesDone = True
            continue
        if (rangesDone):
            mp.append(int(ln))
        else:
            ln = ln.split("-")
            
            lRs.append(int(ln[0]))
            uRs.append(int(ln[1]))
            
def mergeRanges(lRs, uRs):
    lowerRanges = []
    upperRanges = []
    
    for w in range(len(lRs)):
        lR = lRs[w]
        uR = uRs[w]
        if not lowerRanges:
            lowerRanges.append(lR)
            upperRanges.append(uR)
            continue

        appended = False
        
        i = 0
        while i < len(lowerRanges) and lowerRanges[i] < lR:
            if upperRanges[i] >= uR:
                appended = True
                break
            i += 1
            
        if not appended and i < len(lowerRanges):
            if lowerRanges[i] <= uR:
                lowerRanges[i] = min(lowerRanges[i], lR)
                upperRanges[i] = max(upperRanges[i], uR)
                appended = True
            if upperRanges[i] <= uR:
                appended = True
            
        i = 0
        while i < len(lowerRanges) and upperRanges[i] < lR:
            i += 1
        if not appended and i < len(lowerRanges):
            if upperRanges[i] <= uR:
                upperRanges[i] = uR
                appended = True
        
        if not appended:
            lowerRanges.append(lR)
            upperRanges.append(uR)
        
        intervals = sorted(zip(lowerRanges, upperRanges))
        lowerRanges = [l for l, u in intervals]
        upperRanges = [u for l, u in intervals]

    return lowerRanges, upperRanges
    
nLRs = []
nURs = []
clRs = lRs.copy()
cuRs = uRs.copy()
while len(nLRs) != len(lRs):
    if (len(nLRs) != 0):
        lRs = nLRs.copy()
        uRs = nURs.copy()
    nLRs, nURs = mergeRanges(lRs, uRs)
                
for i in range(len(lRs)):
    possibleFresh += uRs[i] - lRs[i] + 1

        
for val in mp:
    notFound = True
    for i in range(len(lRs)):
        if notFound and lRs[i] <= val and uRs[i] >= val:
            notFound = False
            fresh += 1
            continue
    
    # Logging

print(f"Possible Fresh: {possibleFresh}")
print(f"Fresh: {fresh}")