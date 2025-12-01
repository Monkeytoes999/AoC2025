import math
mp = []

currentPosition = 50
zeroCount = 0

#Part 1: 7:46
#Part 2: 11:54

with open('inputs/testcase.txt', 'r') as file:
# with open('inputs/1input.txt', 'r') as file:
    for line in file:
        ln = line.strip()
        mp.append(ln)
        
for ins in mp:
    dir = 1
    if (ins[0:1] == "L"):
        dir = -1
    dist = int(ins[1:])
    
    #Part 2
    if (dist // 100 > 0):
        zeroCount += dist // 100
    distToZero = (100 - currentPosition) if dir == 1 else (currentPosition if currentPosition != 0 else 100)
    if (dist % 100 >= distToZero):
        zeroCount += 1
    
    currentPosition = currentPosition + dir*dist
    
    #Part 1
    # if (currentPosition == 0):
    #     zeroCount += 1
    
    currentPosition = currentPosition % 100

    # Logging
    # print(ins)
    # print(currentPosition)
    # print(zeroCount)

print(zeroCount)