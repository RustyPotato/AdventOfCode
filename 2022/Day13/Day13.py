from functools import cmp_to_key

def packetCompare(left, right):
  if (type(left) is int and type(right) is int):
    if (left < right):
      return 1
    elif (left > right):
      return -1
    return 0


  if (type(left) is not list):
    left = [left]
  if (type(right) is not list):
    right = [right]

  for i in range(0, max(len(left), len(right))):
    # If the left or right run out of elements
    if (i == len(left)):
      return 1
    if (i == len(right)):
      return -1

    val = packetCompare(left[i], right[i])
    if (val != 0):
      return val
  return 0

packetPairs = map(lambda x: x.split("\n"), open("input1.txt").read().strip().split("\n\n"))
allPackets = []
validPackets = []

for i, pair in enumerate(packetPairs):
  firstPacket = eval(pair[0])
  secondPacket = eval(pair[1])
  allPackets.append(firstPacket)
  allPackets.append(secondPacket)
  val = packetCompare(firstPacket, secondPacket)
  if (val == True):
    validPackets.append(i+1)
print(f"Part 1 answer: {sum(validPackets)}")


allPackets.append([[2]])
allPackets.append([[6]])
allPackets.sort(key=cmp_to_key(packetCompare), reverse=True)

indices = [allPackets.index([[2]])+1, allPackets.index([[6]])+1]
print(f"Part 2 answer: {indices} => {(indices[0]) * (indices[1])}")

