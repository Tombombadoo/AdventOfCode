import os;
os.chdir(os.path.dirname(__file__))
with open('8.txt', 'r') as f:
    treeMap = [line.strip() for line in f.readlines()]

def checkTree(x,y,map,aocPart):
    height = len(map)
    width = len(map[0])
    blockedCount = 0
    scenicScore = 0
    scorePerDir = {}
    for direction in ('up','left','down','right'):
        #Set the range for the loop
        if direction == 'up':
            checkedYRange = reversed(range(0,y))
            checkedXRange = range(x,x+1)
        elif direction == 'down':
            checkedYRange = range(y+1,height)
            checkedXRange = range(x,x+1)
        elif direction == 'left':
            checkedYRange = range(y,y+1)
            checkedXRange = reversed(range(0,x))
        elif direction == 'right':
            checkedYRange = range(y,y+1)
            checkedXRange = range(x+1,width)

        #AoC Part 1
        if aocPart == 1:
            #Check edge trees
            if (x == 0 and y in range(0,height)) or (x == width and y in range(0,height)) \
            or (y == 0 and x in range(0,width)) or (y == height and x in range(0,width)):
                #The tree is at the edge
                break
            #Check each tree height in the range against the current tree height
            #If there's a blocking tree, add 1 to the counter and break the loop
            for checkedY in checkedYRange:
                for checkedX in checkedXRange:
                    blocked = 0
                    if map[checkedY][checkedX] >= map[y][x]:
                        blockedCount = blockedCount + 1
                        blocked = 1
                    if blocked == 1:
                        break
                if blocked == 1:
                    break
        #AoC Part 2
        elif aocPart == 2:
            #Default the score for this direction
            count = 0
            blocked = 0
            #Check each tree in the range against the current tree height
            #For each checked tree, add it to a counter if its lower than the current tree
            #Break at the first one
            for checkedY in checkedYRange:
                for checkedX in checkedXRange:
                    blocked = 0
                    if map[checkedY][checkedX] < map[y][x]:
                        count = count + 1
                    else:
                        count = count + 1
                        blocked = 1
                    if blocked == 1:
                        break
                if blocked == 1:
                    break
            scorePerDir[direction] = count 
            if direction == 'up':
                scenicScore = scorePerDir[direction]
            else:
                scenicScore = scenicScore * scorePerDir[direction]

    #Returns
    if aocPart == 1:
        # If the tree has been blocked 4 times, it's all directions, and so can't be seen from outside
        if blockedCount == 4:
            return 1
        else:
            return 0
    elif aocPart == 2:
        return scenicScore


seenCount = 0
for ypos in range(0,len(treeMap)):
    for xpos in range(0,len(treeMap[0])):
        result = checkTree(xpos,ypos,treeMap,1)
        if result == 0:
            seenCount = seenCount + 1
print(f'Trees seen from the outside: {seenCount}')

scenicScores = []
for ypos in range(0,len(treeMap)):
    for xpos in range(0,len(treeMap[0])):
        result = checkTree(xpos,ypos,treeMap,2)
        scenicScores.append(result)
print(f'Maximum Scenic Score = {max(scenicScores)}')
