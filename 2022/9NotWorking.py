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
        tailPositions.add(f'{ropePos[1][0]},{ropePos[1][1]}')   
        global moveCount
    return ropePos

def moveRopeTail(headX,headY,ropePos,tailPositions):
    headPos = [ropePos[0][0],ropePos[0][1]]
    tailPos = [ropePos[1][0],ropePos[1][1]]
    xDiff = abs(headPos[0] - tailPos[0])
    yDiff = abs(headPos[1] - tailPos[1])    
    #Flag that we're going to move as default
    move = 1
    #Is the head touching? Don't move
    if headPos[0] in (tailPos[0]-1,tailPos[0]+1,tailPos[0]) and headPos[1] in (tailPos[1]-1,tailPos[1]+1,tailPos[1]):
        move = 0
    if move == 1:
        #Is the head off axis and more than 1 away? Move to the axis thats furthest away
        #Calculate the difference
        xDiff = abs(headPos[0] - tailPos[0])
        yDiff = abs(headPos[1] - tailPos[1])
        print(f'Starting Difference X: {xDiff}, Y:{yDiff}')

        #If an axis is off by 1 and the difference is greater than 1 for 1 axis
        if (headPos[0] in (tailPos[0]-1,tailPos[0]+1) or headPos[1] in (tailPos[1]-1,tailPos[1]+1)) \
            and (xDiff > 1 or yDiff > 1):
            #If x is greater
            if xDiff > yDiff:
                print('Moving Y Axis')
                tailPos[1] = headPos[1]
            else:
                tailPos[0] = headPos[0]
                print('Moving X Axis')           
        
        #Is the head more than 1 away on the same axis? Move next to the head
        xDiff = abs(headPos[0] - tailPos[0])
        yDiff = abs(headPos[1] - tailPos[1])
        print(f'After Diagonal Difference X: {xDiff}, Y:{yDiff}')
        if xDiff > yDiff:
            if headPos[0] < tailPos[0]:
                tailPos[0] = tailPos[0] - 1
            elif headPos[0] > tailPos[0]:
                tailPos[0] = tailPos[0] + 1
        else:
            if headPos[1] < tailPos[1]:
                tailPos[1] = tailPos[1] - 1
            elif headPos[1] > tailPos[1]:
                tailPos[1] = tailPos[1] + 1
        xDiff = abs(headPos[0] - tailPos[0])
        yDiff = abs(headPos[1] - tailPos[1])
        print(f'After Movement Difference X: {xDiff}, Y:{yDiff}')
    ropePos[1] = tailPos
    return ropePos

#Run the script
#Define starting positions for the head and tail
# Using X and Y as Axis
moveCount = 0
ropePos=[[0,0],[0,0]]
uniqueTailPosList = set()
#uniqueTailPosList.add('0,0')
for movement in input:
    ropePos = moveRopeHead(movement[0],movement[2],ropePos,uniqueTailPosList)
uniqueTailPosList = list(uniqueTailPosList)
uniqueTailPosList.sort()
print(uniqueTailPosList)
print(f'Unique positions: {len(uniqueTailPosList)}')
print(moveCount)