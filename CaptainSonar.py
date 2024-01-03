import math
import copy
sonarMap = [["o", "i", "o", "o", "o", "o", "o", "o", "o"],
            ["o", "o", "o", "o", "i", "o", "o", "i", "o"],
            ["o", "o", "o", "o", "o", "o", "o", "o", "o"],
            ["o", "o", "o", "o", "o", "o", "i", "o", "o"],
            ["o", "i", "o", "o", "o", "i", "o", "o", "o"],
            ["o", "o", "o", "o", "o", "o", "o", "i", "o"],
            ["o", "i", "o", "o", "i", "o", "o", "o", "o"],
            ["o", "o", "o", "o", "o", "o", "o", "o", "o"],
            ["o", "o", "i", "o", "o", "o", "o", "o", "o"]]

## silent running
## Mines
## Detonate mines retrace
## Pathing rules with mines


size = 9
quadrants = 9
quadrantSize = size / math.sqrt(quadrants) ## 3

currPath = []
possibleLocs = []

for index1, row in enumerate(sonarMap):
    for index2, val in enumerate(row):
        if(val == "o"):
            possibleLocs.append([index1, index2])

while(1):    
    tempSonarMap = copy.deepcopy(sonarMap)

    for rowIndex, row in enumerate(tempSonarMap):
        for colIndex in range(len(row)):
            if(tempSonarMap[rowIndex][colIndex] == "o"):
                tempSonarMap[rowIndex][colIndex] = "X"
    inputDir = input("Enter Action: ")
    currPath.append(inputDir)

    ## Logic for getting loc
    newLocs = []
    if(inputDir == "N"):
        for loc in possibleLocs:
            loc[0] -= 1

    elif(inputDir == "S"):
        for loc in possibleLocs:
            loc[0] += 1

    elif(inputDir == "E"):
        for loc in possibleLocs:
            loc[1] += 1

    elif(inputDir == "W"):
        for loc in possibleLocs:
            loc[1] -= 1

    elif(inputDir == "SURFACE"):
        quad = int(input("Enter Quadrant: ")) ## single number
        currPath.append(quad)
        for location in possibleLocs:
            temp = ((((location[0] // quadrantSize) * math.sqrt(quadrants)) + (location[1] // quadrantSize)) + 1)
            if (temp == quad):
                newLocs.append(location)
        possibleLocs = copy.deepcopy(newLocs)
    
    elif(inputDir == "DRONE"):
        quad = int(input("Enter Quadrant: ")) ## single number
        ans = input("Was Guess Correct: ") ## YES or NO
        currPath.append(quad)
        currPath.append(ans)
        for location in possibleLocs:
            temp = ((((location[0] // quadrantSize) * math.sqrt(quadrants)) + (location[1] // quadrantSize)) + 1)
            if(ans == "YES"):
                if (temp == quad):
                    newLocs.append(location)
            else:
                if (temp != quad):
                    newLocs.append(location)
        possibleLocs = copy.deepcopy(newLocs)

    elif(inputDir == "SONAR"):
        quad = int(input("Enter Quadrant: ")) ## single number or size + 1
        row = int(input("Enter Row: ")) ## single number or size + 1
        col = int(input("Enter Column: ")) ## single number or size + 1

        if(quad != "X"):
            for location in possibleLocs:
                temp = ((((location[0] // quadrantSize) * math.sqrt(quadrants)) + (location[1] // quadrantSize)) + 1)
                if (temp == quad):
                    newLocs.append(location)

        for location in possibleLocs:
            if((location[0] == row) or (location[1] == col)):
                newLocs.append(location)

        possibleLocs = copy.deepcopy(newLocs)
    
    elif(inputDir == "TORPEDO" or inputDir == "MINE DETONATION"):
        row = int(input("Enter Row: ")) ## single number
        col = int(input("Enter Column: ")) ## single number
        hit = input("MISS, INDIRECT HIT, or DIRECT HIT?: ")

        currPath.append([row, col])
        currPath.append(hit)

        possibleSpots = [[row - 1, col - 1], [row - 1, col], [row - 1, col + 1],
                         [row, col - 1], [row, col], [row, col + 1],
                         [row + 1, col - 1], [row + 1, col], [row + 1, col + 1]]

        if(hit == "DIRECT HIT"):
            possibleLocs = [[row, col]]

        elif(hit == "INDIRECT HIT"):
            for location in possibleLocs:
                for spots in possibleSpots:
                    if (location == spots):
                        if(location != [row, col]):
                            newLocs.append(location)
            possibleLocs = copy.deepcopy(newLocs)

        elif(hit == "MISS"):
            for location in possibleLocs:
                if ((location == possibleSpots[0]) or (location == possibleSpots[1]) or (location == possibleSpots[2]) or (location == possibleSpots[3])):
                    continue
                if ((location == possibleSpots[4]) or (location == possibleSpots[5]) or (location == possibleSpots[6]) or (location == possibleSpots[7]) or (location == possibleSpots[8])):
                    continue
                newLocs.append(location)
            possibleLocs = copy.deepcopy(newLocs)
    
    elif(inputDir == "ENEMY TORPEDO"):
        torRow = int(input("Enter Row: "))
        torCol = int(input("Enter Col: "))
        currPath.append([torRow, torCol])
        for location in possibleLocs:
            if (((abs(location[0] - torRow)) + (abs(location[1] - torCol))) <= 4):
                newLocs.append(location)
        possibleLocs = copy.deepcopy(newLocs)

    for location in possibleLocs:
        if (not(location[0] < 0 or location[0] >= size or location[1] >= size or location[1] < 0)):
            if(sonarMap[location[0]][location[1]] != "i"):
                newLocs.append(location)
    
    possibleLocs = copy.deepcopy(newLocs)
    
    for locSpot in possibleLocs:
        tempSonarMap[locSpot[0]][locSpot[1]] = "o"
    
    print("    ", end ="")
    for col in range(size):
        print(col, end=" ")
    print("\n    ", end="")
    print("--" * size)

    for index, mapRow in enumerate(tempSonarMap):
        print(f"{index} | ", end="")
        for spot in mapRow:
            print(f"{spot} ", end="")
        print("")
    print(currPath)
