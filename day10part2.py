import itertools
import time
import math

def loadAdaptors(testMode):
    print("loading adaptor list from file")
    adaptorList = []
    if not testMode:
        puzzleFile = open("input/day10part1.txt", "r")
    else:
        puzzleFile = open("input/day10test.txt", "r")
    for line in puzzleFile:
        adaptorList.append(int(line))
    puzzleFile.close()
    print("adaptor list loaded")
    return adaptorList


def getDeviceRating(adaptors):
    adaptors.sort()
    deviceRating = adaptors[len(adaptors) - 1] + 3
    return deviceRating


def putAdaptorsInOrder(adaptors, deviceRating):
    print("putting adaptors in most basic acceptable order")
    adaptors.append(deviceRating)
    adaptors.sort()
    orderedAdaptors = [[0]]
    possibleNexts = []
    adaptorTry = 0
    prevEle = 0
    while adaptorTry < len(adaptors):
        if adaptors[adaptorTry] - 1 in orderedAdaptors[prevEle] or adaptors[adaptorTry] - 2 in orderedAdaptors[prevEle] or adaptors[adaptorTry] - 3 in orderedAdaptors[prevEle]:
            possibleNexts.append(adaptors[adaptorTry])
            adaptorTry += 1
        else:
            orderedAdaptors.append(possibleNexts)
            possibleNexts = []
            prevEle += 1
    orderedAdaptors.append([deviceRating])
    print('adaptors put in most basic order')
    return orderedAdaptors


def getBaseList(orderedAdaptors):
    print('finding base list from which to generate every possible order')
    baseList = []
    for element in orderedAdaptors:
        iterations = []
        if len(element) == 1:
            baseList.append(element)
        else:
            iterationTry2 = []
            for length in range(1, len(element) + 1):
                iterationTry = (list(itertools.combinations(element, length)))
                for item in iterationTry:
                    item = list(item)
                    if len(item) == 1:
                        iterationTry2.append(int(item[0]))
                    else:
                        iterationTry2.append(list(item))

            baseList.append(list(iterationTry2))
    print('base list found:')
    print(baseList)
    print(orderedAdaptors)
    return baseList




def itemGood(lastinArray, itemToBeAdded):
    if itemToBeAdded <= lastinArray + 3:
        return True
    else:
        return False

def generateAllLists(baseList):
    print('generating all possible sequences')
    allLists = []
    goodLists = 0
    badLists = []
    newList = []
    testsRun = 0

    newList = itertools.product(*baseList)

    print("Sequence testing started")
    for nlistItem in newList:
        testsRun += 1
        nListList = []

        nListList = list(nlistItem)
        newListFinal = []

        for nListListItem in range(0,len(nListList)):
            if type(nListList[nListListItem]) is list:
                for aaaaaaa in (itertools.chain(nListList[nListListItem])):
                    if aaaaaaa <= newListFinal[len(newListFinal)-1] + 3:
                        newListFinal.append(aaaaaaa)
                    else:
                        newListFinal.append(aaaaaaa)
                        badLists.append(newListFinal)
                        break
            else:
                if len(newListFinal) == 0:
                    newListFinal.append(nListList[nListListItem])
                elif nListList[nListListItem] <= newListFinal[len(newListFinal)-1] + 3:
                    newListFinal.append(nListList[nListListItem])
                else:
                    newListFinal.append(nListList[nListListItem])
                    badLists.append(newListFinal)
                    break
            if newListFinal[len(newListFinal)-1] == baseList[len(baseList)-1][0]:
                goodLists += 1
                allLists.append(newListFinal)




    print('all possible sequences found')
    print(testsRun, "tests run")

    print()


    return goodLists

def countGoodLists(allLists):
    print('eliminating bad sequences')
    goodLists = 0
    for subList in allLists:
        for elIndex in range(1, len(subList)):
            if subList[elIndex] == subList[elIndex-1]+1 or subList[elIndex] == subList[elIndex-1]+2 or subList[elIndex] == subList[elIndex-1]+3:
                if subList[elIndex] == subList[len(subList)-1]:
                    goodLists += 1
            else:
                break
    print('bad sequences eliminated')
    return goodLists

def itemGoodReverse(nextInArray, itemToBeAdded):
    if itemToBeAdded >= nextInArray - 3:
        return True
    else:
        return False


def newApproach(baseList):
    currentList = []
    for baseListIndex in range(0, len(baseList)-1):
        baseListItem = baseList[baseListIndex]
        nextBaseItem = baseList[baseListIndex+1]
        if nextBaseItem == baseList[-1]:
            endReached = True
        else:
            if len(baseListItem) == 1:
                if itemGoodReverse(nextBaseItem[0], baseListItem[0]):
                    currentList.append(baseListItem[0])
                    break
            else:
                for level2ListIndex in range(0, len(baseListItem)):
                    if type(baseListItem[level2ListIndex]) is int:
                        if itemGoodReverse(nextBaseItem[0], baseListItem[level2ListIndex]):
                            currentList.append(baseListItem[level2ListIndex])
                    else:
                        if itemGoodReverse(nextBaseItem[0], baseListItem[level2ListIndex][-1]):
                            currentList.append(baseListItem[level2ListIndex])

def again(adaptorsInOrder):
    factSum = []
    indexTry = 0
    goodPerms = []
    normalNumbers = []
    while indexTry < len(adaptorsInOrder):
        adaptorList = adaptorsInOrder[indexTry]
        if len(adaptorList) > 1:

            factSum.append(math.factorial(len(adaptorList)))
            for permSet in range(0,len(adaptorList)+1):
                for perm in itertools.combinations(adaptorList, permSet):
                    print(perm)
                    if len(perm) != 0:
                        if perm[-1] < adaptorsInOrder[indexTry+1][-1] + 3:
                            print("goodPerm", perm)
                            goodPerms.append(list(perm))
                        else:
                            print("badPerm", perm)
        else:
            normalNumbers.append(adaptorList)
        indexTry+=1
    print(len(goodPerms))
    print(len(normalNumbers))
    print(goodPerms)
    print(normalNumbers)
    for hmm in itertools.product(*goodPerms, *normalNumbers):
        print(hmm)
        listHmm = list(hmm)
        for hmmEl in listHmm:
            if type(hmmEl) is list:
                for ele in hmmEl:
                    listHmm.append(ele)
                listHmm.remove(hmmEl)
                listHmm.sort()
        print(listHmm)




start_time = time.time()

gloTest = False

print(generateAllLists(getBaseList(putAdaptorsInOrder(loadAdaptors(gloTest), getDeviceRating(loadAdaptors(gloTest))))))

#again(putAdaptorsInOrder(loadAdaptors(gloTest),getDeviceRating(loadAdaptors(gloTest))))

print(time.time() - start_time, "seconds")