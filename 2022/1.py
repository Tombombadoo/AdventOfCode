#Import Input 
import os;
os.chdir(os.path.dirname(__file__))
with open('1.txt','r') as f:
    input = [lines.strip() for lines in f.readlines()]

#Define variables
calories = []
counter = 0
elfTotal = 0

for line in input:
    if line == '':
        elfTotal = 0
        counter = counter + 1
    else:
        elfTotal = elfTotal + int(line)
        calories.insert(counter,elfTotal)
#Part 1
calories.sort()
print(calories[-1])

#Part 2
print(calories[-1]+calories[-2]+calories[-3])