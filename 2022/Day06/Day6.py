
def processSignal(signal, distinctCount):
  signal = signal.strip()
  for i in range(0, len(signal)-distinctCount):
    if (len(set(signal[i: i+distinctCount])) == len(signal[i: i+distinctCount])):
      return i + distinctCount
  return 0

inputFile = open("input1.txt")

for line in inputFile:
  print("Part 1 Sol: " + str(processSignal(line, 4)))
  print("Part 2 Sol: " + str(processSignal(line, 14)))


