from shapely.geometry import Polygon, Point, MultiPoint, LineString

mp = []

maxArea = 0
maxInternalArea = 0

#Part 1: 0:5:38
#Part 2: 3:58:00

# with open('inputs/testcase.txt', 'r') as file:
with open('inputs/9input.txt', 'r') as file:
    for line in file:
        ln = line.strip()
        mp.append(ln.split(","))
    
maxArea = 0
maxInternalArea = 0
poly1 = Polygon(mp)
for i in range(len(mp)):
    x1, y1 = int(mp[i][0]), int(mp[i][1])
    for j in range(len(mp)):
        x2, y2 = int(mp[j][0]), int(mp[j][1])
        area = (abs(x2 - x1) + 1) * (abs(y2 - y1) + 1)
        maxArea = max(maxArea, area)
        
        internal = True
        if area > maxInternalArea:
            poly2 = Polygon([(x1, y1), (x1, y2), (x2, y2), (x2, y1)])
            if poly1.contains(poly2):
                maxInternalArea = max(maxInternalArea, area) 
    
    # Logging
print(f"{maxArea}")
print(f"{maxInternalArea}")