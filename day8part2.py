import re

testMode = False

pointer = 0
accumulator = 0
ops = 1

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
	global ops
	global pointer
	instructionsRun = []
	swap = False
	while True:
		if pointer in instructionsRun:
			runWhileReplacing(instructions)
			break
		elif pointer > len(instructions):
			print accumulator
			break
		else:
			instructionsRun.append(pointer)
		
		instruction = re.findall("^(\w+) ([\+\-]\d+)$", instructions[pointer])[0][0]
		modifier = re.findall("^(\w+) ([\+\-]\d+)$", instructions[pointer])[0][1]		
		doOps(instruction, modifier)


def doOps(instruction, modifier):
	if instruction == "acc":
		doAcc(modifier)
	elif instruction == "jmp":
		lastPointer = pointer	
		doJmp(modifier)
		lastOp = "jmp"
	elif instruction == "nop":
		lastPointer = pointer
		doNop()
		lastOp = "nop"

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


def runWhileReplacing(instructions):
	global pointer
	global accumulator
	instructionsRun = []
	pointer = 0
	checkIndex = 0
	nopJmpIndexes = []
	originalInstructions = instructions
	success = False
	for ins in instructions:
		instruction = re.findall("^(\w+) ([\+\-]\d+)$", ins)[0][0]
		modifier = re.findall("^(\w+) ([\+\-]\d+)$", ins)[0][1]	
		
		if re.findall("^(\w+) ([\+\-]\d+)$", ins)[0][0] == "nop":
			nopJmpIndexes.append(checkIndex)
		elif re.findall("^(\w+) ([\+\-]\d+)$", ins)[0][0] == "jmp":
			nopJmpIndexes.append(checkIndex)
		checkIndex += 1

	for occ in nopJmpIndexes:
		pointer = 0
		accumulator = 0
		instruction = re.findall("^(\w+) ([\+\-]\d+)$", instructions[occ])[0][0]
		modifier = re.findall("^(\w+) ([\+\-]\d+)$", instructions[occ])[0][1]
		instructionsRun = []


		if instruction == "nop":
			instructions[occ] = "jmp " + modifier
		elif instruction == "jmp":
			instructions[occ] = "nop " + modifier 

		instructionsRun = []
		while True:
			if pointer in instructionsRun:
				break
			elif pointer >= len(instructions):
				print accumulator
				success = True
				break
			else:
				instructionsRun.append(pointer)

				instruction = re.findall("^(\w+) ([\+\-]\d+)$", instructions[pointer])[0][0]
				modifier = re.findall("^(\w+) ([\+\-]\d+)$", instructions[pointer])[0][1]
				
				doOps(instruction, modifier)
		
		if success == True:
			break
			
		instructions = loadInstructions()




runComputer(loadInstructions())