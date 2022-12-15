#Import Input 
import os;
os.chdir(os.path.dirname(__file__))
with open('3.txt','r') as f:
    input = [lines.strip() for lines in f.readlines()]

#Generate variables
pri = {}
score = 0
count = 0

#Generate item priorities
for x in range(ord('a'), ord('z')+1):
    count = count + 1
    pri[chr(x)] = count
for x in range(ord('A'), ord('Z')+1):
    count = count + 1
    pri[chr(x)] = count

#Get Rucksack Items and cumulative score
for line in input:
    rucksack = []
    rucksack.append(line[:int(len(line)/2)])
    rucksack.append(line[int(len(line)/2):])
    for item in rucksack[0]:
        if item in rucksack[1]:
            score = score + pri[item]
            break
print(f'Total Score for part 1: {score}')

#Get elf groups
group = []
score = 0
for line in input:
    group.append(line)
    if len(group) == 3:
        for item in set(group[0]):
            if item in set(group[1]) and item in set(group[2]):
                score = score + pri[item]
        group = []
print(f'Total Score for part 2: {score} ')