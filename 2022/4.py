#Import Input 
import os;
os.chdir(os.path.dirname(__file__))
with open('4.txt','r') as f:
    input = [lines.strip() for lines in f.readlines()]

#Housekeeping and prep
def splitLine(input):
    line = input.split(',')
    line[0] = line[0].split('-')
    line[1] = line[1].split('-')
    for x in (0,1):
        for y in (0,1):
            line[x][y] = int(line[x][y])
    return line

#Part 1
def checkFullOverlap(input):
    if (int(input[0][0]) <= int(input[1][0]) and int(input[0][1]) >= int(input[1][1])) \
        or (int(input[0][0]) >= int(input[1][0]) and int(input [0][1]) <= int(input[1][1])):
        return 1
    else:
        return 0

#Part 2
def checkOverlap(input):
    print(input)
    for x in range(line[0][0],line[0][1]+1):
        for y in range(line[1][0],line[1][1]+1):
            if x == y:
                print(f'{x},{y}')
                return 1
    return 0
#Part 1
count = 0
for line in input:
    line = splitLine(line)
    count = count + checkFullOverlap(line)
print(count)

#Part 2
count = 0
for line in input:
    line = splitLine(line)
    count = count + checkOverlap(line)
print(count)



