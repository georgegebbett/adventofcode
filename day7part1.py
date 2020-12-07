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

def checkContainsColour(bag, reqdColour, ultimateBag):
	if reqdColour in ruleDict[bag] and ultimateBag not in bagsContainColour:
		bagsContainColour.append(ultimateBag)
	else:
		for containedBag in ruleDict[bag]:
			checkContainsColour(containedBag, reqdColour, ultimateBag)

def numBagsContainColour(reqdColour):
	global ruleDict
	global bagsContainColour
	ruleDict = createRuleDict()
	bagsContainColour = []
	for item in ruleDict:
		ultimateBag = item
		checkContainsColour(item, "shiny gold", ultimateBag)
	return len(bagsContainColour)


print numBagsContainColour("shiny gold")