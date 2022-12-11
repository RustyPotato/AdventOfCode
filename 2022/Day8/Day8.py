import math

def isVisible(grid, x, y):
  visibleDirections = 4
  treeHeight = grid[x][y]

  # Visible from above
  for i in range (0, x):
    if (grid[i][y] >= treeHeight):
      visibleDirections -= 1
      break

  # Visible from below
  for i in range(x, len(grid)-1):
    if (grid[i+1][y] >= treeHeight):
      visibleDirections -= 1
      break

  # Visible from left
  for i in range(0, y):
    if (grid[x][i] >= treeHeight):
      visibleDirections -= 1
      break

  # Visible from right
  for i in range(y, len(grid[0])-1):
    if (grid[x][i+1] >= treeHeight):
      visibleDirections -= 1
      break
  
  return visibleDirections != 0

def scenicScore(grid, x, y):
  viewDistances = []
  treeHeight = grid[x][y]
  
  # Visible from above
  sightDistance = 0
  for i in reversed(range(0, x)):
    sightDistance += 1
    if (grid[i][y] >= treeHeight):
      break
  viewDistances.append(sightDistance)

  # Visible from left
  sightDistance = 0
  for i in reversed(range(0, y)):
    sightDistance += 1
    if (grid[x][i] >= treeHeight):
      break
  viewDistances.append(sightDistance)

  # Visible from below
  sightDistance = 0
  for i in range(x, len(grid)-1):
    sightDistance += 1
    if (grid[i+1][y] >= treeHeight):
      break
  viewDistances.append(sightDistance)

  # Visible from right
  sightDistance = 0
  for i in range(y, len(grid[0])-1):
    sightDistance += 1
    if (grid[x][i+1] >= treeHeight):
      break
  viewDistances.append(sightDistance)

  return math.prod(viewDistances)

inputFile = open("input1.txt")

grid = []
for line in inputFile:
  line = list(map(lambda x: int(x), list(line.strip())))
  grid.append(line)

visibleSpots = 0
for i in range(0, len(grid)):
  for j in range(0, len(grid[i])):
    if (isVisible(grid, i, j) == True):
      visibleSpots += 1
print(f"There are {visibleSpots} visible spots on the map.")

bestScenicScore = 0
for i in range(0, len(grid)):
  for j in range(0, len(grid[i])):
    tempScenicScore = scenicScore(grid, i, j)
    if (tempScenicScore > bestScenicScore):
      bestScenicScore = tempScenicScore
print(f"The best scenic score in the forest is {bestScenicScore}.")

