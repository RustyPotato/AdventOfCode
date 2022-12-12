def canMove(grid, curr, target):
  # If it's out of bounds
  if (target[0] < 0 or target[0] >= len(grid)):
    return False
  if (target[1] < 0 or target[1] >= len(grid[0])):
    return False
  currentCell = grid[curr[0]][curr[1]]
  targetCell = grid[target[0]][target[1]]
  # If there's already a more efficient path there.
  if (currentCell[1] + 1 >= targetCell[1]):
    return False
  # If the height difference is too steep.
  if (currentCell[0] > targetCell[0] + 1):
    return False
  return True

def tryPath(grid, current, depth):
  grid[current[0]][current[1]] = (grid[current[0]][current[1]][0], depth)
  # End condition!
  if (grid[current[0]][current[1]][0] == 1):
    return
  if canMove(grid, current, (current[0]-1, current[1])):
    globalQueue.append(((current[0]-1, current[1]), depth + 1))
  if canMove(grid, current, (current[0]+1, current[1])):
    globalQueue.append(((current[0]+1, current[1]), depth + 1))
  if canMove(grid, current, (current[0], current[1]-1)):
    globalQueue.append(((current[0], current[1]-1), depth + 1))
  if canMove(grid, current, (current[0], current[1]+1)):
    globalQueue.append(((current[0], current[1]+1), depth + 1))

def printMap(grid):
  spacing = 5
  heights = list(map(lambda x: ''.join(map(lambda y: str(chr(y[0]+96)).rjust((spacing//2) + 1).ljust(spacing) + "|", x)), grid))
  depths = list(map(lambda x: ''.join(map(lambda y: str(y[1]).rjust(spacing) + "|", x)), grid))

  print("Height Map: ")
  for i in range(0, len(heights)):
    print("-" * len(heights[i]))
    print(heights[i])
    print(depths[i])

inputFile = open("input1.txt")

# [(current, depth)]
globalQueue = []
heightMap = []
depthMap = []
index = (0, 0)
startCoords = (0, 0)
endCoords = (0, 0)

for line in inputFile:
  heightMap.append([])
  for char in line.strip():
    if (char == "S"):
      startCoords = (index[0], index[1])
      heightMap[-1].append((ord('a')-96, 99999))
    elif (char == "E"):
      endCoords = (index[0], index[1])
      globalQueue.append((endCoords, 0))
      heightMap[-1].append((ord('z')-96, 99999))
    else:
      heightMap[-1].append((ord(char)-96, 99999))
    index = (index[0], index[1] + 1)
  index = (index[0] + 1, 0)

#printMap(heightMap)
#tryPath(heightMap, startCoords, endCoords, 0)
#printMap(heightMap)

while (len(globalQueue) != 0):
  nextTry = globalQueue.pop()
  tryPath(heightMap, nextTry[0], nextTry[1])

printMap(heightMap)
minDistance = 99999
for row in heightMap:
  for cell in row:
    if (cell[0] == 1 and cell[1] < minDistance):
      minDistance = cell[1]
print(f"Min distance found was {minDistance}.")
