puzzleFile = open("input/day6part1.txt", "r")
#puzzleFile = open("input/day6test.txt", "r")
groupQuest = []
questionCount = 0
persNo = 1
persDict = {}

for line in puzzleFile:
	if line == "\n":
		littleQues = []
		questionsAdded = []
		for qList in persDict.values():
			for question in qList:
				littleQues.append(question)
		for question in littleQues:
			if littleQues.count(question) == len(persDict) and question not in questionsAdded:
				questionCount+=1
				questionsAdded.append(question)
		persDict = {}
		persNo = 1
	else:
		for char in line:
			if char != "\n":
				try:
					persDict[persNo].append(char)
				except:
					persDict.update({persNo: [char]})
		persNo += 1

print questionCount