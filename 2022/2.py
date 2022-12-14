#Import Input 
import os;
os.chdir(os.path.dirname(__file__))
with open('2.txt','r') as f:
    input = [lines.strip() for lines in f.readlines()]

rps = {
    "A":{
        'score': 1,
        'wins': 'C',
        'loses': 'B'
    },
    "B":{
        'score': 2,
        'wins': 'A',
        'loses': 'C'
    },
    "C":{
        'score': 3,
        'wins': 'B',
        'loses': 'A'
    },
    'winScore': 6,
    'drawScore': 3
}

def playRPSPart1(opponent,me):
    if me == 'X':
        me = 'A'
    elif me == 'Y':
        me = 'B'
    else:
        me = 'C'
    score = rps[me]['score']
    if opponent == rps[me]['wins']:
        score = score + rps['winScore']
    elif me == opponent:
        score = score + rps['drawScore']
    return score

def playRPSPart2(opponent,me):
    if me == 'X':
        me = rps[opponent]['wins']
    elif me == 'Y':
        me = opponent
    else:
        me = rps[opponent]['loses']
    score = rps[me]['score']
    if opponent == rps[me]['wins']:
        score = score + rps['winScore']
    elif me == opponent:
        score = score + rps['drawScore']
    return score


totalScore = 0
for line in input:
    score = playRPSPart1(line[0],line[2])
    totalScore = totalScore + score
print(f'Part 1 total score: {totalScore}') 


totalScore = 0
for line in input:
    score = playRPSPart2(line[0],line[2])
    totalScore = totalScore + score
print(f'Part 2 total score: {totalScore}') 