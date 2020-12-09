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


def findWeakness(cypher, oddVal):
    for firstValPos in range(len(cypher) - 1):
        valuesList = []
        valuesList.append(cypher[firstValPos])
        for nextValPos in range(firstValPos, len(cypher) - 1):
            if cypher[nextValPos] not in valuesList:
                valuesList.append(cypher[nextValPos])
            if sum(valuesList) == oddVal:
                valuesList.sort()
                return valuesList[0] + valuesList[-1]


print(findWeakness(loadInstructions(False), decodeCypher(loadInstructions(False), 25)))
