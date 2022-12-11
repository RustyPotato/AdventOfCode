

inputFile = open("input1.txt")
register = 1
registerHistory = [1]
screen = [""]

def cycle():
  registerHistory.append(register)
  cycle = len(registerHistory)-1
  position = cycle-1
  inRange = abs(register - (position%40)) <= 1
  print(f"During cycle {str(cycle).rjust(3)}: CRT draws pizel at position {position}")
  if (inRange):
    screen[-1] = screen[-1] + '#'
  else:
    screen[-1] = screen[-1] + '.'
  if (cycle % 40 == 0):
    screen.append("")

  print(f"Current CRT Row: {screen[-1]}")


for line in inputFile:
  print()
  print(f"Start cycle{str(len(registerHistory)).rjust(4)}: begin executing {line.strip()}")
  line = line.strip()
  lineComp = line.split(" ")
  if (lineComp[0] == "noop"):
    cycle()

  elif (lineComp[0] == "addx"):
    cycle()
    cycle()
    register += int(lineComp[1])
    print(f"End of cycle{str(len(registerHistory)-1).rjust(3)}: finish executing {line} (Register X is now {register}")
    print(f"Sprite position: {'.' * (register-2)}###{'.' * (40-register+2)}")
  else:
    print(f"Command '{lineComp[0]}' not recognized.")
    exit()

print("\n\n\n")
indexing = 20
total = 0
while (indexing <= len(registerHistory)):
  total += indexing * registerHistory[indexing]
  indexing += 40
print(f"Part 1 total: {total}")
print("Part 2:")
for line in screen:
  print(line)

