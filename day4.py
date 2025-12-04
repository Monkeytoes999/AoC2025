import math
mp = []

count = 0
firstCount = 0

#Part 1: 17:28.51
#Part 2: 5:48.37

# with open('inputs/testcase.txt', 'r') as file:
with open('inputs/4input.txt', 'r') as file:
    for line in file:
        ln = line.strip()
        mp.append(list(ln))
        
    lastRolls = -1
    while lastRolls != count:
        lastRolls = count
        
        for y in range(len(mp)):
            for x in range(len(mp[y])):
                rolls = 0
                if (mp[y][x] == "@"):
                    
                    for i in range(y - 1, y + 2):
                        for j in range(x - 1, x + 2):
                            try:
                                if (i >= 0 and i < len(mp) and j >= 0 and j < len(mp[i]) and (i != y or j != x)):
                                    if mp[i][j] != ".": 
                                        rolls += 1
                            except:
                                continue
                            
                    if(rolls < 4):
                        count += 1
                        if firstCount == 0:
                            mp[y][x] = "X"
                        else:
                            mp[y][x] = "."
                            
        if firstCount == 0:
            firstCount = count
            
            for y in range(len(mp)):
                for x in range(len(mp[y])):
                    if mp[y][x] == "X":
                        mp[y][x] = "."
                    
    
    # Logging

print(f"Initial # of rolls removed: {firstCount}")
print(f"Total # of rolls removed: {count}")
