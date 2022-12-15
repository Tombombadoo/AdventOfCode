#Import Input 
import os;
os.chdir(os.path.dirname(__file__))
with open('4.txt','r') as f:
    input = [lines.strip() for lines in f.readlines()]

