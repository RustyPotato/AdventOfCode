global fullFilesystem
Object = lambda **kwargs: type("Object", (), kwargs)

def getFolderSize(directory, fullFileSystem):
  if (directory.size != -1):
    return directory.size

  directorySize = sum(i[1] for i in directory.files)
  for subDirName in directory.subDirectories:
    # Try to find it in the file system, and call this function on it.
    subDirName = directory.name + ('' if directory.name.endswith('/') else '/') + subDirName
    filteredSubDirs = [x for x in fullFileSystem if x.name == subDirName]

    if (len(filteredSubDirs) != 1):
      print(f"Found {len(filteredSubDirs)} results for directories of name '{subDirName}'")

    subDir = filteredSubDirs[0]
    directorySize += getFolderSize(subDir, fullFileSystem)
  directory.size = directorySize
  return directorySize

def changeDirectory(command, currentPath):
  if (command == "$ cd /"):
    currentPath = []
  elif (command == "$ cd .."):
    currentPath.pop()
  else:
    newFolder = command[5:]
    currentPath.append(newFolder)

def list(command, currentPath, inFile):
  newDirectory = Object(name = '/' + '/'.join(currentPath), subDirectories = [], files = [], size = -1)
  while (len(inFile) > 0 and inFile[-1][0] != "$"):
    outLine = inFile.pop().split(" ")
    if (outLine[0] == "dir"):
      newDirectory.subDirectories.append(outLine[1])
    else:
      newDirectory.files.append((outLine[1], int(outLine[0])))
  fullFileSystem.append(newDirectory)

def processCommand(command, currentPath, inFile):
  splitCommand = command.split(" ")
  if (splitCommand[0] != "$"):
    print("Error! Trying to read an output line as input.")

  if (splitCommand[1] == "cd"):
    changeDirectory(command, currentPath)
  elif (splitCommand[1] == "ls"):
    list(command, currentPath, inFile)
  else:
    print("Error! Command not recognized.")

inputFile = open("input1.txt").read().strip().split('\n')[::-1]
currentPath = []
fullFileSystem = []

# Create filesystem representation
while len(inputFile) != 0:
  line = inputFile.pop().strip()
  processCommand(line, currentPath, inputFile)

# Calculate Totals
getFolderSize(fullFileSystem[0], fullFileSystem)

# Find solution to part 1
part1Solution = 0
for direct in fullFileSystem:
  if (direct.size < 100000):
    part1Solution += direct.size
print("Part 1 solution: " + str(part1Solution))

# Part 2 solution
totalSpace = 70000000
requiredSpace = 30000000
remainingSpace = totalSpace - fullFileSystem[0].size
requiredSpace = requiredSpace - remainingSpace

print(f"The file system is {totalSpace}, of that, {remainingSpace} is left. We need an additional {requiredSpace}.")

optionalFolders = [x for x in fullFileSystem if x.size > requiredSpace]
optionalFolders.sort(key=lambda x: x.size)
print(f"Delete folder {optionalFolders[0].name} of size {optionalFolders[0].size}.")


