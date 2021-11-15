def loadAdaptors(testMode):
    adaptorList = []
    if not testMode:
        puzzleFile = open("input/day10part1.txt", "r")
    else:
        puzzleFile = open("input/day10test.txt", "r")
    for line in puzzleFile:
        adaptorList.append(int(line))
    puzzleFile.close()
    return adaptorList


def getDeviceRating(adaptors):
    adaptors.sort()
    deviceRating = adaptors[len(adaptors) - 1] + 3
    return deviceRating


def putAdaptorsInOrder(adaptors, deviceRating):
    adaptors.append(deviceRating)
    adaptors.sort()
    orderedAdaptors = []
    currentVoltage = 0
    numberOfOnes = 0
    numberOfThrees = 0
    for adaptor in adaptors:
        if adaptor == currentVoltage + 1:
            orderedAdaptors.append(adaptor)
            currentVoltage = adaptor
            numberOfOnes += 1
        elif adaptor == currentVoltage + 2:
            orderedAdaptors.append(adaptor)
            currentVoltage = adaptor
        elif adaptor == currentVoltage + 3:
            orderedAdaptors.append(adaptor)
            currentVoltage = adaptor
            numberOfThrees += 1
    return numberOfOnes * numberOfThrees


print(putAdaptorsInOrder(loadAdaptors(True), getDeviceRating(loadAdaptors(True))))
