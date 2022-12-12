
def ExecuteCommand(columnArray, count, origin, dest):
  movedBoxes = columnArray[origin-1][-count:]
  # Part 1 solution, where crates are reversed.
  #columnArray[dest-1].extend(movedBoxes[::-1])
  # Part 2 solution, where crates are not reversed.
  columnArray[dest-1].extend(movedBoxes)
  columnArray[origin-1] = columnArray[origin-1][:-count]
  return columnArray

inputFile = open("input1.txt")
inputFile = inputFile.read().split("\n\n")
board = inputFile[0].split("\n")
instructions = inputFile[1].strip().split("\n")

columnCount = len(board[-1].strip().split("   "))

# Create the columns
columnArray = []
for i in range(0, columnCount):
  columnArray.append([])

for line in board[-2::-1]:
  for i in range(0, columnCount):
    letter = line[1+(i*4)]
    if (letter != ' '):
      columnArray[i].append(letter)

for line in instructions:
  components = line.split(" ")
  count = int(components[1])
  orig = int(components[3])
  dest = int(components[5])
  columnArray = ExecuteCommand(columnArray, count, orig, dest)
solution = ""
for column in columnArray:
  solution += column[-1]
print(solution)


