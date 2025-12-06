import math
mp = []

sum = 0

#Part 1: 11:29.87
#Part 2: 16:16.70

# with open('inputs/testcase.txt', 'r') as file:
with open('inputs/6input.txt', 'r') as file:
    for line in file:
        # ln = line.strip()
        mp.append(list(line))
    
    #Part 2
    for i in range(len(mp)):
        mp[i] = mp[i][::-1][1:]
    
    ops = mp[len(mp) - 1]
    ops = [val for val in ops if val.strip()]
    
    vals = [1] * len(ops)
    for j in range(len(ops)):
        if ops[j] == "+":
            vals[j] = 0
    
    #Part 1
    # for i in range(len(mp) - 1):
    #     nums = mp[i].split(" ")
    #     nums = [val for val in nums if val.strip()]
    #     for j in range(len(nums)):
    #         if ops[j] == "+":
    #             vals[j] += int(nums[j])
    #         else:
    #             vals[j] *= int(nums[j])
            
    #Part 2
    k = 0
    for i in range(len(mp[0])):
        num = 0
        for j in range(len(mp) - 1):
            if (mp[j][i] != " "):
                num *= 10
                num += int(mp[j][i])
        if num != 0:
            if ops[k] == "+":
                vals[k] += num
            else:
                vals[k] *= num
        else:
            num = 0
            k += 1
                    
    for val in vals:
        sum += val
        
    # Logging

print(f"Grand Total: {sum}")
