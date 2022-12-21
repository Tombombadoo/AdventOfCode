import os;
os.chdir(os.path.dirname(__file__))
with open('9.txt', 'r') as f:
    input = [line.strip() for line in f.readlines()]

def moveRopeHead(direction,count,ropePos,tailPositions):
    print(f'{direction} {count}')
    count = int(count)
    for i in range(1,count+1):
        if direction == 'U':
            ropePos[0][1] = ropePos[0][1] + 1
            #print(f'Moving the head to {ropePos[0][0]},{ropePos[0][1]}')
            ropePos = moveRopeTail(ropePos[0][0],ropePos[0][1],ropePos,tailPositions)
        elif direction == 'D':
            ropePos[0][1] = ropePos[0][1] - 1
            #print(f'Moving the head to {ropePos[0][0]},{ropePos[0][1]}')
            ropePos = moveRopeTail(ropePos[0][0],ropePos[0][1],ropePos,tailPositions)
        elif direction == 'L':
            ropePos[0][0] = ropePos[0][0] - 1
            #print(f'Moving the head to {ropePos[0][0]},{ropePos[0][1]}')
            ropePos = moveRopeTail(ropePos[0][0],ropePos[0][1],ropePos,tailPositions)
        elif direction == 'R':
            ropePos[0][0] = ropePos[0][0] + 1
            #print(f'Moving the head to {ropePos[0][0]},{ropePos[0][1]}')
            ropePos = moveRopeTail(ropePos[0][0],ropePos[0][1],ropePos,tailPositions)
        
    return ropePos

def moveRopeTail(headX,headY,ropePos,tailPositions):
    headPos = [ropePos[0][0],ropePos[0][1]]
    tailPos = [ropePos[1][0],ropePos[1][1]]
    xDiff = abs(headPos[0] - tailPos[0])
    yDiff = abs(headPos[1] - tailPos[1])    
    #Flag that we're going to move as default
    move = 1
    #Are you overlapped? Don't move
    if headPos == tailPos:
        move = 0
    #Is the head diagonal? Don't move
    elif headPos[0] in (tailPos[0]-1,tailPos[0]+1) and headPos[1] in (tailPos[1]-1,tailPos[1]+1):
        move = 0
    #Is the head touching the tail? Don't move
    elif (headPos[0] == tailPos[0] or headPos[1] == tailPos[1]) and (xDiff == 1 or yDiff == 1):
        move = 0
    if move == 1:
        #Is the head off axis and more than 1 away? Move to the axis thats furthest away
        #Calculate the difference
        xDiff = abs(headPos[0] - tailPos[0])
        yDiff = abs(headPos[1] - tailPos[1])
        
        #If an axis is off by 1 and the difference is greater than 1 for 1 axis
        if (headPos[0] in (tailPos[0]-1,tailPos[0]+1) or headPos[1] in (tailPos[1]-1,tailPos[1]+1)) \
            and (xDiff > 1 or yDiff > 1):
            #If x is greater
            if xDiff > yDiff:
                #If the head position is less than tailPos
                if headPos[1] < tailPos[1]:
                    tailPos[1] = tailPos[1] - 1
                else:
                    tailPos[1] = tailPos[1] + 1
            else:
                if headPos[0] < tailPos[0]:
                    tailPos[0] = tailPos[0] - 1
                else:
                    tailPos[0] = tailPos[0] + 1            
            #tailPositions.add(f'{tailPos[0]},{tailPos[1]}')
        #Is the head more than 1 away on the same axis? Move next to the head
        xDiff = abs(headPos[0] - tailPos[0])
        yDiff = abs(headPos[1] - tailPos[1])
        if headPos[0] == tailPos [0] or headPos[1] == tailPos[1]:
            if xDiff > 1 or yDiff > 1:
                if xDiff > yDiff:
                    #If the head position is less than 
                    if headPos[0] < tailPos[0]:
                        tailPos[0] = tailPos[0] - 1
                    else:
                        tailPos[0] = tailPos[0] + 1
                else:
                    if headPos[1] < tailPos[1]:
                        tailPos[1] = tailPos[1] - 1
                    else:
                        tailPos[1] = tailPos[1] + 1 
        tailPositions.add(f'{tailPos[0]},{tailPos[1]}')
    ropePos[1] = tailPos
    print(f'{headPos} - {tailPos}')
    return ropePos


#Run the script
#Define starting positions for the head and tail
# Using X and Y as Axis
ropePos=[[0,0],[0,0]]
uniqueTailPosList = set()
uniqueTailPosList.add('0,0')
for movement in input:
    ropePos = moveRopeHead(movement[0],movement[2],ropePos,uniqueTailPosList)
print(uniqueTailPosList)
print(f'Unique positions: {len(uniqueTailPosList)}')
