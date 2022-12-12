
calorieCounter = open("input2.txt", "r")

fileMaximum = 0
entryTotal = 0

for line in calorieCounter:
  if (line == "\n"):
    if (entryTotal > fileMaximum):
      fileMaximum = entryTotal
    entryTotal = 0
  else:
    entryTotal += int(line)
print("Final Answer is " + str(fileMaximum))

