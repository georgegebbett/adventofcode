import re

testMode = False

pointer = 0
accumulator = 0


def loadInstructions():
    if not testMode:
        puzzleFile = open("input/day8part1.txt", "r")
    else:
        puzzleFile = open("input/day8test.txt", "r")
    instructionsInVar = []
    for line in puzzleFile:
        instructionsInVar.append(line)
    puzzleFile.close()
    return instructionsInVar


def runComputer(instructions):
    global pointer
    global accumulator
    repeating = False
    if not repeating:
        print("running input program")
        instructionsRun = []
        while True:
            if pointer in instructionsRun:
                repeating = True
                print("no luck with the input program (loop found), going to substitutions")
                break
            elif pointer > len(instructions):
                print("input program gave good output, which is", accumulator)
                break
            else:
                instructionsRun.append(pointer)
                instruction = re.findall("^(\w+) ([\+\-]\d+)$", instructions[pointer])[0][0]
                modifier = re.findall("^(\w+) ([\+\-]\d+)$", instructions[pointer])[0][1]
                doOps(instruction, modifier)

    if repeating:
        instructions = generateInstructions(getJmpList(instructions), instructions)
        subTry = 0
        for ins in instructions:
            subTry += 1
            pointer = 0
            accumulator = 0
            instructionsRun = []
            success = False
            while True:
                if pointer in instructionsRun:
                    break
                elif pointer >= len(ins):
                    success = True
                    break
                else:
                    instructionsRun.append(pointer)
                    instruction = re.findall("^(\w+) ([\+\-]\d+)$", ins[pointer])[0][0]
                    modifier = re.findall("^(\w+) ([\+\-]\d+)$", ins[pointer])[0][1]
                    doOps(instruction, modifier)

            if success == True:
                print("substitution successful on attempt", str(subTry) + ", output is", accumulator)
                break


def doOps(instruction, modifier):
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


def getJmpList(instructions):
    checkIndex = 0
    nopJmpIndexes = []
    for ins in instructions:
        instruction = re.findall("^(\w+) ([\+\-]\d+)$", ins)[0][0]
        modifier = re.findall("^(\w+) ([\+\-]\d+)$", ins)[0][1]

        if re.findall("^(\w+) ([\+\-]\d+)$", ins)[0][0] == "nop":
            nopJmpIndexes.append(checkIndex)
        elif re.findall("^(\w+) ([\+\-]\d+)$", ins)[0][0] == "jmp":
            nopJmpIndexes.append(checkIndex)

        checkIndex += 1
    return nopJmpIndexes


def generateInstructions(nopJmpIndex, instructions):
    instructionsList = []
    for occ in nopJmpIndex:
        instruction = re.findall("^(\w+) ([\+\-]\d+)$", instructions[occ])[0][0]
        modifier = re.findall("^(\w+) ([\+\-]\d+)$", instructions[occ])[0][1]

        if instruction == "nop":
            instructions[occ] = "jmp " + modifier
        elif instruction == "jmp":
            instructions[occ] = "nop " + modifier
        instructionsList.append(instructions)
        instructions = loadInstructions()
    return instructionsList


runComputer(loadInstructions())
