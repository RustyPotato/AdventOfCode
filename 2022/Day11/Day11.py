import math

global worryControl
worryControl = None
global worryMax
worryMax = None

def getLambdaFunction(equation):
  parts = equation.split()
  assert(parts[0] == "new")
  assert(parts[1] == "=")
  assert(parts[2] == "old")
  if (parts[3] == "*" and parts[4] == "old"):
    return lambda x: x * x
  elif (parts[3] == "*"):
    return lambda x: x * int(parts[4])
  elif (parts[3] == "+" and parts[4] == "old"):
    return lambda x: x + x
  elif (parts[3] == "+"):
    return lambda x: x + int(parts[4])
  else:
    print(f"Unable to parse equation {equation}.")
    exit()

class Monkey:
  def __init__(self, inputBlock):
    lines = monkey.split("\n")
    self.monkeyId = int(lines[0].replace("Monkey", "").replace(":", "").strip())
    self.items = list(map(lambda x: int(x), lines[1].replace("Starting items: ", "").strip().split(", ")))
    self.worryOperation = getLambdaFunction(lines[2].replace("Operation: ", "").strip())
    self.divideTest = int(lines[3].replace("Test: divisible by", "").strip())
    self.trueTarget = int(lines[4].replace("If true: throw to monkey ", "").strip())
    self.falseTarget = int(lines[5].replace("If false: throw to monkey ", "").strip())
    self.totalInspections = 0

  def inspectItems(self, allMonkies):
    self.totalInspections += len(self.items)
    # This function assumes a monkey can't toss something
    # to themselves, which would cause an infinite loop.
    newItems = map(self.worryOperation, self.items)
    newItems = map(lambda x: x // worryControl, newItems)
    newItems = map(lambda x: x % worryMax, newItems)
    
    self.items = []
    for newItem in newItems:
      self.throwItem(newItem, allMonkies)

  def throwItem(self, value, allMonkies):
    target = self.falseTarget
    if (value % self.divideTest == 0):
      target = self.trueTarget

    # Find the target monkey, and deposit the item in it's queue.
    for otherMonkey in allMonkies:
      if otherMonkey.monkeyId == target:
        otherMonkey.recieveItem(value)
        break


  def recieveItem(self, newItem):
    self.items.append(newItem)

  def print(self):
    print(f"Monkey {self.monkeyId}")
    print(f"  Has items: {self.items}")
    print(f"  Worry Op: {self.worryOperation}")
    print(f"  Test: Divide by {self.divideTest}")
    print(f"    On True Target: {self.trueTarget}")
    print(f"    On False Target: {self.falseTarget}")

inputFile = open("input1.txt").read().strip().split("\n\n")
monkies = []

for monkey in inputFile:
  newMonk = Monkey(monkey)
  monkies.append(newMonk)

# To keep the numbers sufficiently small and manageable, we divide them
# all by their collective lowestCommonMultiple across all monkies.
allDivTests = list(map(lambda x: x.divideTest, monkies))
greatestCommonDenominator = allDivTests[0]
product = allDivTests[0]
for i in range(1, len(allDivTests)):
  greatestCommonDenominator = math.gcd(greatestCommonDenominator, allDivTests[i])
  product = product * allDivTests[i]
worryMax = abs(product) // greatestCommonDenominator

part1 = False
if (part1):
  roundsSimulated = 20
  worryControl = 3
else:
  roundsSimulated = 10000
  worryControl = 1

for roundCount in range(0, roundsSimulated):
  for monkey in monkies:
    monkey.inspectItems(monkies)

print(f"\n== After Round {roundsSimulated} ==")
inspectCounts = []
for monk in monkies:
  print(f"Monkey {monk.monkeyId} inspected items {monk.totalInspections} times.")
  inspectCounts.append(monk.totalInspections)

inspectCounts = sorted(inspectCounts, reverse=True)
print(f"Final Solution: {inspectCounts[0] * inspectCounts[1]}")





















