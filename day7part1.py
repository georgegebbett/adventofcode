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

def checkContainsGold(bag):
	global bagsContainGold
	if "shiny gold" in ruleDict[bag] and ultimateBag not in bagsContainGold:
		bagsContainGold.append(ultimateBag)
	else:
		for containedBag in ruleDict[bag]:
			checkContainsGold(containedBag)

ruleDict = createRuleDict()
bagsContainGold = []

for item in ruleDict:
	ultimateBag = item
	checkContainsGold(item)

print len(bagsContainGold)