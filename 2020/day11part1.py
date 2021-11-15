import re
from colorama import Fore, Back, Style

def loadSeats(testMode):
    seatList = []
    if not testMode:
        puzzleFile = open("input/day11part1.txt", "r")
    else:
        puzzleFile = open("input/day11test.txt", "r")
    for line in puzzleFile:
        if line[-1] == "\n":
            seatList.append([line[0:-1]])
        else:
            seatList.append([line])
    puzzleFile.close()
    seatList.insert(0, ['             '])
    seatList.insert(1, ['   '])
    return seatList


def niceGrid(seatList):
    for colNo in range(0, len(seatList[2][0])):
        seatList[1][0] = seatList[1][0] + str(colNo)[-1]
        if colNo >= 10:
            seatList[0][0] = seatList[0][0] + str(colNo)[-2]
    for rowNo in range(0, len(seatList)-2):
        seatList[rowNo+2][0] = (str(rowNo).ljust(2)) + " " + seatList[rowNo+2][0]
    return seatList

def printSeats(seats):
    for row in seats:
        for seat in row:
            print(seat)

def playWithCords(seatList):
    printSeats(niceGrid(seatList))
    coOrd = input("Co-ord? ")
    xGrid = list(re.findall("(\d+), ?(\d+)", coOrd))[0][0]
    yGrid = list(re.findall("(\d+), ?(\d+)", coOrd))[0][1]
    print("x is", xGrid, "y is", yGrid)
    print("this seat is", seatList[int(yGrid)+2][0][int(xGrid)+3])
    highlightSeat(loadSeats(gloTest), int(xGrid), int(yGrid))

def highlightSeat(seatList, xCord, yCord):
    for rowNo in range(0, len(seatList)-2):
        if rowNo == yCord:
            print(Fore.RED + seatList[rowNo + 2][0][0:xCord-1] + Fore.LIGHTYELLOW_EX + seatList[rowNo + 2][0][xCord-1] + Fore.GREEN + seatList[rowNo + 2][0][xCord] + Fore.LIGHTYELLOW_EX + seatList[rowNo + 2][0][xCord+1] + Fore.RED + seatList[rowNo + 2][0][xCord:-1])
        elif xCord -1 <= rowNo <= xCord+1:
            print(Fore.RESET + seatList[rowNo+2][0][0:xCord-1] + Fore.LIGHTYELLOW_EX + seatList[rowNo+2][0][xCord-1:xCord+2] + Fore.RESET + seatList[rowNo+2][0][xCord+2:])
        else:
            print(Fore.RESET + seatList[rowNo+2][0][0:xCord] + Fore.RED + seatList[rowNo+2][0][xCord] + Fore.RESET + seatList[rowNo+2][0][xCord:-1])

def findAdjacentSeats(seatList, xCord, yCord):
    adjacentSeats = []
    if xCord >len(seatList[0]):
        pass


gloTest = True

highlightSeat(loadSeats(gloTest),3,3)