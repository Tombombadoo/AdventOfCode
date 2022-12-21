#Import Input 
import os;
import sys;
os.chdir(os.path.dirname(__file__))
with open('7.txt','r') as f:
    input = [lines.strip() for lines in f.readlines()]
sys.setrecursionlimit(3000)
fs = {
    0: {
        "parentID": "",
        "childrenID" : [],
        "files": [],
        "totalSize": 0,
        "name": "root"
    }
}
currentID = 0
newID = 0

def runCommand(line):
    cmd = line.split(' ')
    #Get rid of the $
    cmd.pop(0)

    if cmd[0] == 'cd':
        if cmd[1] == '..':
            global currentID
            #Move up a dir
            currentID = fs[currentID]["parentID"]
            return

        #Moving to a new directory so generate a new ID
        global newID
        newID = newID + 1

        try:
            fs[currentID]["childrenID"].append(newID)
        except:
            fs[currentID]["childrenID"] = []
            fs[currentID]["childrenID"].append(newID)
        try:
            fs[newID]["parentID"] = currentID
        except:
            fs[newID] = {}
            fs[newID]["parentID"] = currentID
        currentID = newID
        fs[currentID]["name"] = cmd[1]
        fs[currentID]["totalSize"] = 0
    else:
        #Its an LS
        pass


def recordFile(line):
    cmd = line.split(' ')
    try:
        fs[currentID]["files"].append(cmd[0])
    except:
        fs[currentID]["files"] = []
        fs[currentID]["files"].append(cmd[0])


def calculateFolderSize(folderID,fileSystem):
    try:
        if len(fileSystem[folderID]["childrenID"]) > 0:
            for childID in fileSystem[folderID]["childrenID"]:
                calculateFolderSize(childID,fs)
    except KeyError :
        pass
    try:
        for file in fileSystem[folderID]["files"]:
            fileSystem[folderID]["totalSize"] = fileSystem[folderID]["totalSize"] + int(file)
    except:
        pass
    try:
        for childID in fileSystem[folderID]["childrenID"]:
            fileSystem[folderID]["totalSize"] = fileSystem[folderID]["totalSize"] + fileSystem[childID]["totalSize"]
    except:
        pass
    

def findFoldersPart1(folderID,fileSystem):
    output = 0
    try:
        if len(fileSystem[folderID]["childrenID"]) > 0:
            for childID in fileSystem[folderID]["childrenID"]:
                output = output + findFoldersPart1(childID,fileSystem)
    except KeyError :
        pass
    if fileSystem[folderID]["totalSize"] <= 100000:
        output = output + fileSystem[folderID]["totalSize"]
    return output


def findFolderPart2(folderID,fileSystem):
    totalFSSize = 70000000
    totalRemaining = totalFSSize - fileSystem[1]["totalSize"]
    totalRequired = 30000000 - totalRemaining
    try:
        if len(fileSystem[folderID]["childrenID"]) > 0:
            for childID in fileSystem[folderID]["childrenID"]:
                findFolderPart2(childID,fileSystem)
    except KeyError :
        pass
    if fileSystem[folderID]["totalSize"] >= totalRequired:
        global outputP2
        outputP2.append(fileSystem[folderID]["totalSize"])



#Run the code
#Build the filesystem object
for line in input:
    if line[0] == '$':
        runCommand(line)
    elif line.startswith('dir'):
        pass
    else:
        recordFile(line)

#Calculate folder sizes and put them in the FS dictionary
calculateFolderSize(1,fs)

#Find sizes for folders
outputP1 = 0
outputP1 = findFoldersPart1(0,fs)
print(f'Part 1: {outputP1}')

outputP2 = []
findFolderPart2(0,fs)
print(f'Part 2: {min(outputP2)}')