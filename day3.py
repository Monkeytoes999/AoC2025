import math
mp = []

sum = 0

#Part 1: 9:01.56
#Part 2: 7:09.56

# with open('inputs/testcase.txt', 'r') as file:
with open('inputs/3input.txt', 'r') as file:
    for line in file:
        ln = line.strip()
        mp.append(ln[::-1])
        
    
    for ln in mp:
        numDigits = 12 #2 for Part 1, 12 for Part 2
        maxDigit = len(ln)
        currentVal = 0
        for i in range(numDigits):
            currentDigit = numDigits - i - 1
            for j in range(currentDigit, maxDigit):
                if int(ln[j]) >= int(ln[currentDigit]):
                    currentDigit = j
            maxDigit = currentDigit
            currentVal = currentVal*10 + int(ln[currentDigit])
        sum += currentVal
    
    # Logging

print(f"Total output Joltage: {sum}")