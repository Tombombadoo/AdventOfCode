#Import Input 
import os;
os.chdir(os.path.dirname(__file__))
with open('6.txt','r') as f:
    input = f.readlines()
input = input[0]

#Part 1
counter = 0
buffer = []
for letter in input:
    if len(buffer)<4:
        buffer.append(letter)
        counter = counter + 1
    else:
        counter = counter + 1
        buffer.pop(0)
        buffer.append(letter)
        if len(set(buffer)) == 4:
            print(counter)
            break

#Part 2
counter = 0
buffer = []
for letter in input:
    if len(buffer)<14:
        buffer.append(letter)
        counter = counter + 1
    else:
        counter = counter + 1
        buffer.pop(0)
        buffer.append(letter)
        if len(set(buffer)) == 14:
            print(counter)
            break
