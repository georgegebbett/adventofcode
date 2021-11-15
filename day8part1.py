import re

testMode = False



pointer = 0
accumulator = 0
instructionsRun = []

def loadInstructions():
	if testMode == False:
		puzzleFile = open("input/day8part1.txt", "r")
	else:
		puzzleFile = open("input/day8test.txt", "r")
	instructionsInVar = []
	for line in puzzleFile:
		instructionsInVar.append(line)
	puzzleFile.close()
	return instructionsInVar

def runComputer(instructions):
	while True:
		instruction = re.findall("^(\w+) ([\+\-]\d+)$", instructions[pointer])[0][0]
		modifier = re.findall("^(\w+) ([\+\-]\d+)$", instructions[pointer])[0][1]
		if pointer in instructionsRun:
			print accumulator
			break
		else:
			instructionsRun.append(pointer)
		if instruction == "acc":
			doAcc(modifier)
		elif instruction == "jmp":
			doJmp(modifier)
		elif instruction == "nop":
			doNop()

def doAcc(accVal):
	global accumulator
	global pointer
	accumulator += int(accVal)
	pointer += 1

def doJmp(jmpVal):
	global pointer
	pointer += int(jmpVal)

def doNop():
	global pointer
	pointer += 1


runComputer(loadInstructions())