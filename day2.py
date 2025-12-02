import math
mp = []

sumInvalid = 0

#Part 1: 11:05.13
#Part 2: 38:00.70

# with open('inputs/testcase.txt', 'r') as file:
with open('inputs/2input.txt', 'r') as file:
    for line in file:
        ln = line.strip()
        mp = ln.split(",")
        
    for rng in mp:
        startRange = int(rng.split("-")[0])
        endRange = int(rng.split("-")[1])
        # print(startRange, endRange)
        
        id = startRange
        while id in range(startRange, endRange + 1):
            
            strID = str(id)
            # Part 1
            # if (len(strID) % 2 == 0):
            #     if (strID[0:int(len(strID)/2)] == strID[int(len(strID)/2):]):
            #         # print(id)
            #         sumInvalid += id
            
            #Part 2
            valCaught = False
            for i in range(1, int(math.floor(len(strID)/2)) + 1):
                # print (i)
                if (len(strID) % i == 0 and not valCaught):
                    val = (id / int(strID[0:i]))
                    if (int(val) == val):
                        val = int(val)
                        strVal = str(val)

                        validPattern = True
                        j = 0
                        while (j < len(strVal) and validPattern):
                            if (j % i == 0):
                                if (strVal[j] != "1"):
                                    validPattern = False
                            else:
                                if (strVal[j] != "0"):
                                    validPattern = False
                            j += 1
                        if validPattern:
                            sumInvalid += id
                            valCaught = True
            id += 1

    
    # Logging

print(f"Sum of invalid IDs: {sumInvalid}")