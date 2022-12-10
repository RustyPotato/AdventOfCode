def characterToPriority(newChar):
  mismatchPriority = ord(newChar)
  if (newChar.isupper()):
    mismatchPriority -= 38
  else:
    mismatchPriority -= 96
  return mismatchPriority

inputFile = open("input1.txt")
totalMismatches = 0

for line in inputFile:
  line = line.strip()
  firstHalf = line[0:len(line)//2]
  secondHalf = line[len(line)//2:]
  
  matchingItems = list(set(firstHalf).intersection(set(secondHalf)))
  assert(len(matchingItems) == 1)

  totalMismatches += characterToPriority(matchingItems[0])
print("Total Mismatches: " + str(totalMismatches))

inputFile = open("input1.txt")
totalMismatches = 0
while True:
  firstBag = set(inputFile.readline().strip())
  secondBag = set(inputFile.readline().strip())
  thirdBag = set(inputFile.readline().strip())

  if (len(firstBag) == 0 or len(secondBag) == 0 or len(thirdBag) == 0):
    break;

  matchingItems = list(firstBag.intersection(secondBag).intersection(thirdBag))
  #assert(len(matchingItems) == 0)
  totalMismatches += characterToPriority(matchingItems[0])

print("Total Badge Mismatches: " + str(totalMismatches))
