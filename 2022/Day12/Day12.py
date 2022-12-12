import sys
sys.setrecursionlimit(7000)

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
  if (currentCell[0] + 1 < targetCell[0]):
    return False
  return True

def tryPath(grid, current, end, depth):
  grid[current[0]][current[1]] = (grid[current[0]][current[1]][0], depth)
  if (current[0] == end[0] and current[1] == end[1]):
    return
  if canMove(grid, current, (current[0]-1, current[1])):
    tryPath(grid, (current[0]-1, current[1]), end, depth + 1)
  if canMove(grid, current, (current[0]+1, current[1])):
    tryPath(grid, (current[0]+1, current[1]), end, depth + 1)
  if canMove(grid, current, (current[0], current[1]-1)):
    tryPath(grid, (current[0], current[1]-1), end, depth + 1)
  if canMove(grid, current, (current[0], current[1]+1)):
    tryPath(grid, (current[0], current[1]+1), end, depth + 1)

def printMap(grid):
  print("Height Map: ")
  print('\n'.join(map(lambda x: ''.join(map(lambda y: str(chr(y[0]+65)).rjust(2), x)), grid)))

  print("Priority Map: ")
  print('\n'.join(map(lambda x: ''.join(map(lambda y: str(y[1]).rjust(2), x)), grid)))


inputFile = open("input1.txt")

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
      heightMap[-1].append((ord('a')-96, 0))
    elif (char == "E"):
      endCoords = (index[0], index[1])
      heightMap[-1].append((ord('z')-96, 99999))
    else:
      heightMap[-1].append((ord(char)-96, 99999))
    index = (index[0], index[1] + 1)
  index = (index[0] + 1, 0)

#printMap(heightMap)
tryPath(heightMap, startCoords, endCoords, 0)
#printMap(heightMap)
print(f"Part 1 final answer: {heightMap[endCoords[0]][endCoords[1]][1]}.")
