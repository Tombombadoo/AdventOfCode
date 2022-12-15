#Import Input 
import os;
os.chdir(os.path.dirname(__file__))
with open('5.txt','r') as f:
    input = [lines.strip('\n') for lines in f.readlines()]
instructionStart = input.index('')
instructions = []
stacks = []

#Populate initial stacks
for line in input[:instructionStart]:
    stacks.append(line)

#Populate Instructions
for line in input[instructionStart+1:]:
    instructions.append(line)