puzzleFile = open("input/day6part1.txt", "r")
#puzzleFile = open("input/day6test.txt", "r")
groupSet = set()
questionCount = 0

for line in puzzleFile:
	if line != "\n":
		for char in line:
			groupSet.add(char)
	else:
		groupSet.remove("\n")
		questionCount += len(groupSet)
		groupSet = set()

print questionCount