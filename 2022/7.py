#Import Input 
import os;
os.chdir(os.path.dirname(__file__))
with open('7sample.txt','r') as f:
    input = [lines.strip() for lines in f.readlines()]

fs = {
    "/": {
        "parent": "/",
        "children" : [],
        "files": []
    }
}
currentDir = '/'

def runCommand(line):
    cmd = line.split(' ')
    #Get rid of the $
    cmd.pop(0)
    if cmd[0] == 'cd':
        if cmd[1] == '..':
            global currentDir
            currentDir = fs[currentDir]["parent"]
            #Move up a dir
            return
        try:
            fs[currentDir]["children"].append(cmd[1])
        except:
            fs[currentDir]["children"] = []
            fs[currentDir]["children"].append(cmd[1])

        try:
            fs[cmd[1]]["parent"] = currentDir
        except:
            fs[cmd[1]] = {}
            fs[cmd[1]]["parent"] = currentDir
        currentDir = cmd[1]       
    else:
        #Its an LS
        pass


def recordDir(line):
    pass

def recordFile(line):
    cmd = line.split(' ')
    try:
        fs[currentDir]["files"].append(cmd[0])
    except:
        fs[currentDir]["files"] = []
        fs[currentDir]["files"].append(cmd[0])
    print(fs)
#Run the code

#Build the filesystem object

for line in input:
    if line[0] == '$':
        runCommand(line)
        print(fs)
    elif line.startswith('dir'):
        recordDir(line)
    else:
        recordFile(line)

