#Import Input 
import os;
os.chdir(os.path.dirname(__file__))
with open('5.txt','r') as f:
    input = [lines.split('\n\n') for lines in f.readlines()]
print(input)
instructionStart = input.index(['\n'])
instructions = []

stacks = {}

def moveCrates(instruction,stacks,part):
    '''This is the logic to move a crate'''
    crane = []
    if part == 1:
        for i in range(0,instruction[0]):
            crane.append(stacks[instruction[1]].pop())
            stacks[instruction[2]].append(crane[0])
            crane = []
    else:
        for i in range(0,instruction[0]):
            crane.append(stacks[instruction[1]].pop())
        crane.reverse()
        for crate in crane:
            stacks[instruction[2]].append(crate)

def getStacks(input,stacks):
    '''Populate initial stack dictionary'''
    stacksInst = []
    for line in input[:instructionStart]:
        stacksInst.append(line[0])
    stacksInst.reverse()
    for x in stacksInst[0]:
        currStack = 0
        try:
            x = int(x)
        except:
            x = x
        if x in range(0,10):
            currStack = x
            for y in stacksInst[1:]:
                try:
                    crate = y[(x*4)-3]
                except IndexError:
                    pass
                if crate != ' ':
                    try:
                        stacks[x].append(crate)
                    except KeyError:
                        stacks[x] = []
                        stacks[x].append(crate)

getStacks(input,stacks)
#Populate Instructions
for line in input[instructionStart+1:]:
    instruction = []
    instruction = line[0].split(' ')
    instruction = [int(instruction[1]),int(instruction[3]),int(instruction[5])]
    print(instruction)
    moveCrates(instruction,stacks,1)
for x in stacks:
    print(stacks[x][-1])

stacks={}
getStacks(input,stacks)
for line in input[instructionStart+1:]:
    instruction = []
    instruction = line[0].split(' ')
    instruction = [int(instruction[1]),int(instruction[3]),int(instruction[5])]
    print(instruction)
    moveCrates(instruction,stacks,2)
for x in stacks:
    print(stacks[x][-1],end='')

    