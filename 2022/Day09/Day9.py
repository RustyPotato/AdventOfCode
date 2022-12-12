
class RopeGame:
  def __init__(self, inLength):
    self.grid = ["."]
    self.nodes = [(0,0)] * inLength
    self.setCell(0, 0, '#')

  def processCommand(self, direction, amount):
    for i in range(0, amount):
      if (direction == "U"):
        self.nodes[0] = (self.nodes[0][0]-1, self.nodes[0][1])
      elif (direction == "D"):
        self.nodes[0] = (self.nodes[0][0]+1, self.nodes[0][1])
      elif (direction == "L"):
        self.nodes[0] = (self.nodes[0][0], self.nodes[0][1]-1)
      elif (direction == "R"):
        self.nodes[0] = (self.nodes[0][0], self.nodes[0][1]+1)
      else:
        print(f"Error, unrecognized direction {direction}.")
        exit()
      self.expandGrid()
      self.moveTail()

  def getTailVisitedSpots(self):
    total = 0
    for line in self.grid:
      total += line.count("#")
    return total

  # Check if the head node (nodes[0]) has moved out of bounds,
  # and expand the grid appropriately to contain it.
  def expandGrid(self):
    adjustment = (0, 0)
    if (self.nodes[0][0] == -1):
      self.grid.insert(0, "." * len(self.grid[0]))
      adjustment = (1, 0)
    if (self.nodes[0][1] == -1):
      for i in range(0, len(self.grid)):
        self.grid[i] = "." + self.grid[i]
      adjustment = (0, 1)
    if (self.nodes[0][0] >= len(self.grid)):
      self.grid.append("." * len(self.grid[0]))
    if (self.nodes[0][1] >= len(self.grid[0])):
      for i in range(0, len(self.grid)):
        self.grid[i] = self.grid[i] + "."
    
    # If we move the grid down/left, we need to shift the nodes to account for it.
    for i, node in enumerate(self.nodes):
      self.nodes[i] = (node[0] + adjustment[0], node[1] + adjustment[1])

  # Check if the tail needs to be moved, and move it if needed.
  def moveTail(self):
    for i in range(1, len(self.nodes)):
      head = self.nodes[i-1]
      tail = self.nodes[i]
      if (abs(head[0] - tail[0]) + 
          abs(head[1] - tail[1])) > 2: # Diagonally too far
        diffX = (head[0] - tail[0])
        diffX = (diffX//abs(diffX))
        diffY = (head[1] - tail[1])
        diffY = (diffY//abs(diffY))
        self.nodes[i] = (tail[0] + diffX, tail[1] + diffY)
      elif (abs(head[0] - tail[0]) >= 2): # Vertically too far
        self.nodes[i] = (tail[0] + ((head[0] - tail[0])//2), tail[1])
      elif (abs(head[1] - tail[1]) >= 2): # Horizontally too far
        self.nodes[i] = (tail[0], tail[1] + ((head[1] - tail[1])//2))

    # Record in the grid the place the tail is in now.
    self.setCell(self.nodes[-1][0], self.nodes[-1][1], "#")

  def printStatus(self):
    for line in self.grid:
      if (len(line) != len(grid[0])):
        print("Error!, the grid is not square.")
        exit()
    print(f"Head at ({self.nodes[0][0]}, {self.nodes[0][1]}). Tail at ({self.nodes[-1][0]}, {self.nodes[-1][1]}). Grid of size ({len(self.grid)}, {len(self.grid[0])})")

  def printGrid(self):
    printVal = []
    for i in range(0, len(self.grid)):
      printVal.append(''.join(self.grid[i]))
      
    for i, node in enumerate(self.nodes):
      printVal[node[0]] = printVal[node[0]][:node[1]] + str(i) + printVal[node[0]][node[1]+1:]

    if (self.nodes[0] == self.nodes[-1]):
      printVal[self.nodes[0][0]] = printVal[self.nodes[0][0]][:self.nodes[0][1]] + "O" + printVal[self.nodes[0][0]][self.nodes[0][1]+1:]
    else:
      printVal[self.nodes[0][0]] = printVal[self.nodes[0][0]][:self.nodes[0][1]] + "H" + printVal[self.nodes[0][0]][self.nodes[0][1]+1:]
      printVal[self.nodes[-1][0]] = printVal[self.nodes[-1][0]][:self.nodes[-1][1]] + "T" + printVal[self.nodes[-1][0]][self.nodes[-1][1]+1:]
    for i, line in enumerate(printVal):
      print(str(i).rjust(2) + ": " + line)

  def setCell(self, x, y, val, grid=None):
    if (grid == None):
      grid = self.grid
    grid[x] = grid[x][:y] + val + grid[x][y+1:]

part1 = RopeGame(2)
part2 = RopeGame(10)
inputFile = open("input1.txt")
for line in inputFile:
  line = line.strip().split()
  part1.processCommand(line[0], int(line[1]))
  part2.processCommand(line[0], int(line[1]))

print(f"Part 1: The tail visited {part1.getTailVisitedSpots()} places.")
print(f"Part 2: The tail visited {part2.getTailVisitedSpots()} places.")

