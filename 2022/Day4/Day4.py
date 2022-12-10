
inputFile = open("input1.txt")
completeSubsets = 0
intersections = 0

for line in inputFile:
  assignments = line.split(',')
  firstRange = assignments[0].split('-')
  firstRange = set(range(int(firstRange[0]), int(firstRange[1])+1))
  
  secondRange = assignments[1].split('-')
  secondRange = set(range(int(secondRange[0]), int(secondRange[1])+1))

  if (firstRange.issubset(secondRange) or secondRange.issubset(firstRange)):
    completeSubsets += 1

  if (len(firstRange.intersection(secondRange)) != 0):
    intersections += 1
    
print(f"Complete Subsets: {completeSubsets}")
print(f"Any Intersections: {intersections}")




