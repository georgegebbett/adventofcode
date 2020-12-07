import re

testMode = False

def createRuleDict():
	if testMode == False:
		puzzleFile = open("input/day7part1.txt", "r")
	else:
		puzzleFile = open("input/day7test.txt", "r")
	ruleDict = {}
	for line in puzzleFile:
		bagColour = re.findall("^([\w\s]+) bags contain", line)
		bagContents = re.findall("(\d) ([\w\s]+) bags?", line)
		contentDict = {}
		for item in bagContents:
			contentDict.update({item[1]:item[0]})
		ruleDict.update({bagColour[0]:contentDict})
	return ruleDict
	puzzleFile.close()

def countBags(bag):
	global bagCount
	for containedBag in ruleDict[bag]:
		for bagContained in range(1, int(ruleDict[bag].get(containedBag))+1):
			bagCount += 1
			countBags(containedBag)
		

ruleDict = createRuleDict()
bagCount = 0

countBags("shiny gold")

print bagCount