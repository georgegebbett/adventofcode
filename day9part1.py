def loadInstructions(testMode):
    cypherInVar = []
    if not testMode:
        puzzleFile = open("input/day9part1.txt", "r")
    else:
        puzzleFile = open("input/day9test.txt", "r")
    for line in puzzleFile:
        cypherInVar.append(int(line))
    puzzleFile.close()
    return cypherInVar


def decodeCypher(cypher, preambleLength):
    for position in range(preambleLength, len(cypher) - 1):
        success = False
        currentVal = cypher[position]
        for precVal1Pos in range(position - preambleLength, position):
            precVal1 = cypher[precVal1Pos]
            for precVal2Pos in range(position - preambleLength, position):
                precVal2 = cypher[precVal2Pos]
                if precVal1 + precVal2 == currentVal and precVal1 != precVal2:
                    success = True
                    break
                elif precVal1Pos == position - 1 and precVal2Pos == position - 1:
                    return currentVal
            if success:
                break


print(decodeCypher(loadInstructions(False), 25))
