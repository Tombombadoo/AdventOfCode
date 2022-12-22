import os;
os.chdir(os.path.dirname(__file__))
with open('10sample.txt', 'r') as f:
    input = [line.strip() for line in f.readlines()]

currentCycle = 0
cycle = 0
x = 1

def checkCycleOutput(cycle,x):
    if cycle in [20,60,100,140,180,220]:
        return x * cycle
    return 0

def printPixel(cycle,x,output,row):
    rowOffset = row*40
    print(cycle-rowOffset)
    if cycle-rowOffset in (x,x-1,x+1):
        output[row].append('#')
        print('Appending #')
    else:
        output[row].append(' ')
        print('Appending " "')

    

signalSum = 0
for line in input:
    if line == 'noop':
        #Starting the cycle
        currentCycle = currentCycle + 1
        #Check if we're on the right cycle
        #Finished the cycle
        signalSum = signalSum + int(checkCycleOutput(currentCycle,x))
        
    else:
        line = line.split(' ')
        #Starting the next cycle
        currentCycle = currentCycle + 1
        #End the next cycle
        signalSum = signalSum + int(checkCycleOutput(currentCycle,x))
        #Starting the second cycle
        currentCycle = currentCycle + 1
        #Finished the second cycle
        signalSum = signalSum + int(checkCycleOutput(currentCycle,x))
        x = x + int(line[1])

print(f'Part 1: {signalSum}')

x = 1
row = 0
crtOut = {}
crtOut[row] = []
print(crtOut)
for line in input:
    if line == 'noop':
        #Starting the cycle
        currentCycle = currentCycle + 1
        #Check if we're on the right cycle
        #Finished the cycle
        if(currentCycle-20)%40 == 0:
            row = row + 1
            crtOut[row] = []
        printPixel(currentCycle,x,crtOut,row)
    else:
        line = line.split(' ')
        #Starting the next cycle
        currentCycle = currentCycle + 1
        #End the next cycle
        if(currentCycle-20)%40 == 0:
            row = row + 1
            crtOut[row] = []
        printPixel(currentCycle,x,crtOut,row)
        #Starting the second cycle
        currentCycle = currentCycle + 1
        #Finished the second cycle
        if(currentCycle-20)%40 == 0:
            row = row + 1
            crtOut[row] = []
        printPixel(currentCycle,x,crtOut,row)
        x = x + int(line[1])

for line in crtOut:
    print(line)
