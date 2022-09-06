# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

# Node system used as the AI's internal interpretation of the maze
import math, sys, getopt


class node:
    parent = None
    heuristic: float = -1.0
    distanceFromStart: int = -1
    totalNodeCost: float = -1.0
    upNode = None
    rightNode = None
    downNode = None
    leftNode = None
    x: int = 0
    y: int = 0


# This is a debug Feature for printing out the maze
def printMaze(maze):
    for r in maze:
        for c in r:
            print(str(c), end='')
        print('\n')

# Debug Feature to print out the coords of every node in a 1D list
def printNodeList(list):
    for n in list:
        print(" (" + str(n.x) + ", " + str(n.y) + ") H:" + str(n.heuristic), end='  ')


# This function takes a maze text file and turns it into a 2D Array
def importMaze(fileName):
    # Obtain maze & split
    referenceFile = open(fileName, "r")  # Open Maze Text File
    maze1D = referenceFile.read()

    # Obtain Size of maze
    width: int = 0  # Width of Maze
    for char in maze1D:
        if char != '\n':
            width = width + 1
        else:
            break

    height: int = maze1D.count('\n')
    print("Size of Maze: " + str(width) + " x " + str(height))
    referenceFile.close()  # Close Maze Reference File

    # Convert 1D array of maze and turn into 2D array
    mazeArr = [[0 for x in range(width)] for y in range(height)]
    row: int = 0
    col: int = 0

    for i in maze1D:
        if (col < width) & (i != '\n'):
            mazeArr[row][col] = i
            col = col + 1
        elif col > width & (i != '\n'):
            row = row + 1
            col = 0
    return mazeArr  # Return 2D Maze


# Checks to see if a node exists on this coordinate on the maze. If so, it returns its pointer, otherwise returns None
def doesNodeExistHere(x, y, visitedNodeList, availableNodes):
    # print("Ran a search for " + str(x) + " " + str(y))
    returnNode = None

    for n in visitedNodeList:
        if n.x == x and n.y == y:
            returnNode = n
            # print("Node has been Found here.")
            break

    for n in availableNodes:
        if n.x == x and n.y == y:
            returnNode = n
            # print("Node has been Found here.")
            break
    return returnNode


# This function builds the neighbors of a node based on the maze to create a tree
def connectNeighbors(currentNode, x, y, maze, visitedNodes, availableNodes):
    # If to right direction of node is not a wall
    if maze[y][x + 1] != '%':

        # If no connection and Node does not exists
        if currentNode.rightNode is None and doesNodeExistHere(x + 1, y, visitedNodes, availableNodes) is None:
            currentNode.rightNode = node()  # Create node
            currentNode.rightNode.x = x + 1  # Set X Cord
            currentNode.rightNode.y = y  # Set Y Cord
            currentNode.rightNode.parent = currentNode
            currentNode.rightNode.leftNode = currentNode  # Connect current node and target node
        # If no connection and Node DOES exist
        if currentNode.rightNode is None and not doesNodeExistHere(x + 1, y, visitedNodes, availableNodes) is None:
            targetNode = doesNodeExistHere(x + 1, y, visitedNodes, availableNodes)
            targetNode.leftNode = currentNode  # Connect current node and target node



    # If to down direction of node is not a wall and that node has not been created, create it.
    if maze[y + 1][x] != '%':
        # If no connection and Node does not exists
        if currentNode.downNode is None and doesNodeExistHere(x, y + 1, visitedNodes, availableNodes) is None:
            currentNode.downNode = node()  # Create node
            currentNode.downNode.x = x  # Set X Cord
            currentNode.downNode.y = y + 1  # Set Y Cord
            currentNode.downNode.parent = currentNode
            currentNode.downNode.upNode = currentNode  # Connect current node and target node
        # If no connection and Node DOES exist
        if currentNode.downNode is None and not doesNodeExistHere(x, y + 1, visitedNodes, availableNodes) is None:
            targetNode = doesNodeExistHere(x, y + 1, visitedNodes, availableNodes)
            targetNode.upNode = currentNode  # Connect current node and target node



    # If to left direction of node is not a wall and that node has not been created, create it.
    if maze[y][x - 1] != '%':
        # If no connection and Node does not exists
        if currentNode.leftNode is None and doesNodeExistHere(x - 1, y, visitedNodes, availableNodes) is None:
            currentNode.leftNode = node()  # Create node
            currentNode.leftNode.x = x - 1  # Set X Cord
            currentNode.leftNode.y = y  # Set Y Cord
            currentNode.leftNode.parent = currentNode
            currentNode.leftNode.rightNode = currentNode  # Connect current node and target node
        # If no connection and Node DOES exist
        if currentNode.leftNode is None and not doesNodeExistHere(x - 1, y, visitedNodes, availableNodes) is None:
            targetNode = doesNodeExistHere(x - 1, y, visitedNodes, availableNodes)
            targetNode.rightNode = currentNode  # Connect current node and target node



    # If to up direction of node is not a wall and that node has not been created, create it.
    if maze[y - 1][x] != '%':
        # If no connection and Node does not exists
        if currentNode.upNode is None and doesNodeExistHere(x, y - 1, visitedNodes, availableNodes) is None:
            currentNode.upNode = node()  # Create node
            currentNode.upNode.x = x  # Set X Cord
            currentNode.upNode.y = y - 1  # Set Y Cord
            currentNode.upNode.parent = currentNode
            currentNode.upNode.downNode = currentNode  # Connect current node and target node
        # If no connection and Node DOES exist
        if currentNode.upNode is None and not doesNodeExistHere(x, y - 1, visitedNodes, availableNodes) is None:
            targetNode = doesNodeExistHere(x, y - 1, visitedNodes, availableNodes)
            targetNode.downNode = currentNode  # Connect current node and target node



def getReturnPath(endNode):
    currentNode = endNode
    list = []
    while currentNode.parent is not None:
        list.append(currentNode)
        currentNode = currentNode.parent

    return list

#Prints the Return Path
def printReturnPath(maze, path):
    #print(path)
    scanX: int = 0
    scanY: int = 0
    found = 0
    for r in maze:
        scanX = 0
        for c in r:
            found = 0
            for n in path:

                if scanX == n.x and scanY == n.y and not c == 'G':
                    print('+', end='')
                    found = 1
            if found == 0:
                print(str(c), end='')
            scanX = scanX + 1
        scanY = scanY + 1
        print('\n')


def depthFirstSearch(startX, startY, maze):
    startNode = node()  # Creating Starting Position Node
    startNode.x = startX  # Establish X Coordinate
    startNode.y = startY  # Establish Y Coordinate
    visitedNodes = []  # Visited Nodes
    visitedNodesCount: int = 0
    availableNodes = []  # Available nodes to navigate
    availableNodes.append(startNode)  # Add Starting Node to Available Nodes
    isGoalState = 0  # Used to end simulation once G is found
    x: int = startX  # X Coordinate of current position
    y: int = startY  # Y Coordinate of current position

    while availableNodes and not isGoalState:
        # Get current node and position
        currentNode = availableNodes.pop()
        x = currentNode.x
        y = currentNode.y
        visitedNodesCount = visitedNodesCount + 1

        # Establish Neighbors
        connectNeighbors(currentNode, x, y, maze, visitedNodes, availableNodes)

        # If node has been visited, do not add it to visited list
        if currentNode in visitedNodes:
            continue
        visitedNodes.append(currentNode)
        # Get Current Node's Neighbors.
        if not currentNode.upNode is None and not currentNode.upNode in visitedNodes and not currentNode.upNode in availableNodes:
            availableNodes.append(currentNode.upNode)
        if not currentNode.leftNode is None and not currentNode.leftNode in visitedNodes and not currentNode.leftNode in availableNodes:
            availableNodes.append(currentNode.leftNode)
        if not currentNode.downNode is None and not currentNode.downNode in visitedNodes and not currentNode.downNode in availableNodes:
            availableNodes.append(currentNode.downNode)
        if not currentNode.rightNode is None and not currentNode.rightNode in visitedNodes and not currentNode.rightNode in availableNodes:
            availableNodes.append(currentNode.rightNode)

        # Goal State
        if maze[y][x] == 'G':
            print("Depth First Search has found G at (" + str(x) + ", " + str(y) + ")")
            print("Number of expanded nodes: " + str(visitedNodesCount))
            isGoalState = 1  # We have met the goal state
    return getReturnPath(currentNode)

def breadthFirstSearch(startX, startY, maze):
    startNode = node()  # Creating Starting Position Node
    startNode.x = startX  # Establish X Coordinate
    startNode.y = startY  # Establish Y Coordinate
    visitedNodes = []  # Visited Nodes
    visitedNodesCount: int = 0
    availableNodes = []  # Available nodes to navigate
    availableNodes.append(startNode)  # Add Starting Node to Available Nodes
    isGoalState = 0  # Used to end simulation once G is found
    x: int = startX  # X Coordinate of current position
    y: int = startY  # Y Coordinate of current position

    while availableNodes and not isGoalState:
        # Get current node and position
        currentNode = availableNodes.pop(0)
        x = currentNode.x
        y = currentNode.y
        visitedNodesCount = visitedNodesCount + 1

        # Establish Neighbors
        connectNeighbors(currentNode, x, y, maze, visitedNodes, availableNodes)

        # If node has been visited, do not add it to visited list
        if currentNode in visitedNodes:
            continue
        visitedNodes.append(currentNode)
        # Get Current Node's Neighbors.
        if not currentNode.upNode is None and not currentNode.upNode in visitedNodes and not currentNode.upNode in availableNodes:
            availableNodes.append(currentNode.upNode)
            # print("Appended up node")
        if not currentNode.leftNode is None and not currentNode.leftNode in visitedNodes and not currentNode.leftNode in availableNodes:
            availableNodes.append(currentNode.leftNode)
            # print("Appended left node")
        if not currentNode.downNode is None and not currentNode.downNode in visitedNodes and not currentNode.downNode in availableNodes:
            availableNodes.append(currentNode.downNode)
            # print("Appended down node")
        if not currentNode.rightNode is None and not currentNode.rightNode in visitedNodes and not currentNode.rightNode in availableNodes:
            availableNodes.append(currentNode.rightNode)
            # print("Appended right node")

        # Goal State
        if maze[y][x] == 'G':
            print("Breadth First Search has found G at (" + str(x) + ", " + str(y) + ")")
            print("Number of expanded nodes: " + str(visitedNodesCount))
            isGoalState = 1  # We have met the goal state
    return getReturnPath(currentNode)

# Calculates Euclidean Distance
def calculateHeuristic(x, y, xGoal, yGoal):
    return math.sqrt(pow(yGoal - y, 2) + pow(xGoal - x, 2))


# Calculates the heuristic of every node around the current node
def calculateNeighborHeuristics(currentNode, xGoal, yGoal):
    rightNode = currentNode.rightNode
    downNode = currentNode.downNode
    leftNode = currentNode.leftNode
    upNode = currentNode.upNode

    if not rightNode is None:  # If heuristic for neighbor hasn't been calculated, calculate it.
        if rightNode.heuristic == -1.0:
            rightNode.heuristic = calculateHeuristic(rightNode.x, rightNode.y, xGoal, yGoal)
        if rightNode.distanceFromStart == -1 or rightNode.distanceFromStart > currentNode.distanceFromStart + 1:
            rightNode.distanceFromStart = currentNode.distanceFromStart + 1
        if rightNode.totalNodeCost == -1.0 or rightNode.totalNodeCost > rightNode.distanceFromStart + rightNode.heuristic:
            rightNode.totalNodeCost = rightNode.distanceFromStart + rightNode.heuristic

    if not downNode is None:  # If heuristic for neighbor hasn't been calculated, calculate it.
        if downNode.heuristic == -1.0:
            downNode.heuristic = calculateHeuristic(downNode.x, downNode.y, xGoal, yGoal)
        if downNode.distanceFromStart == -1 or downNode.distanceFromStart > currentNode.distanceFromStart + 1:
            downNode.distanceFromStart = currentNode.distanceFromStart + 1
        if downNode.totalNodeCost == -1.0 or downNode.totalNodeCost > downNode.distanceFromStart + downNode.heuristic:
            downNode.totalNodeCost = downNode.distanceFromStart + downNode.heuristic

    if not leftNode is None:  # If heuristic for neighbor hasn't been calculated, calculate it.
        if leftNode.heuristic == -1.0:
            leftNode.heuristic = calculateHeuristic(leftNode.x, leftNode.y, xGoal, yGoal)
        if leftNode.distanceFromStart == -1 or leftNode.distanceFromStart > currentNode.distanceFromStart + 1:
            leftNode.distanceFromStart = currentNode.distanceFromStart + 1
        if leftNode.totalNodeCost == -1.0 or leftNode.totalNodeCost > leftNode.distanceFromStart + leftNode.heuristic:
            leftNode.totalNodeCost = leftNode.distanceFromStart + leftNode.heuristic

    if not upNode is None:  # If heuristic for neighbor hasn't been calculated, calculate it.
        if upNode.heuristic == -1.0:
            upNode.heuristic = calculateHeuristic(upNode.x, upNode.y, xGoal, yGoal)
        if upNode.distanceFromStart == -1 or upNode.distanceFromStart > upNode.distanceFromStart + 1:
            upNode.distanceFromStart = upNode.distanceFromStart + 1
        if upNode.totalNodeCost == -1.0 or upNode.totalNodeCost > upNode.distanceFromStart + upNode.heuristic:
            upNode.totalNodeCost = upNode.distanceFromStart + upNode.heuristic


# Returns heuristic of a given node
def getTotalNodeCost(targetNode):
    return targetNode.totalNodeCost


# Sorts List of Available Nodes by their distance from goal
def sortAvailableList(available):
    available.sort(key=getTotalNodeCost)


def aStarSearch(startX, startY, maze, goalX, goalY):
    startNode = node()  # Creating Starting Position Node
    startNode.x = startX  # Establish X Coordinate
    startNode.y = startY  # Establish Y Coordinate
    visitedNodes = []  # Visited Nodes
    visitedNodesCount: int = 0
    availableNodes = []  # Available nodes to navigate
    availableNodes.append(startNode)  # Add Starting Node to Available Nodes
    isGoalState = 0  # Used to end simulation once G is found
    x: int = startX  # X Coordinate of current position
    y: int = startY  # Y Coordinate of current position

    while availableNodes and not isGoalState:
        # Get current node and position
        currentNode = availableNodes.pop(0)
        x = currentNode.x
        y = currentNode.y
        visitedNodesCount = visitedNodesCount + 1

        # Establish Neighbors & their Heuristics
        connectNeighbors(currentNode, x, y, maze, visitedNodes, availableNodes)
        calculateNeighborHeuristics(currentNode, goalX, goalY)

        # If node has been visited, do not add it to visited list
        if currentNode in visitedNodes:
            continue
        visitedNodes.append(currentNode)
        # Get Current Node's Neighbors.
        if not currentNode.upNode is None and not currentNode.upNode in visitedNodes and not currentNode.upNode in availableNodes:
            availableNodes.append(currentNode.upNode)
            # print("Appended up node")
        if not currentNode.leftNode is None and not currentNode.leftNode in visitedNodes and not currentNode.leftNode in availableNodes:
            availableNodes.append(currentNode.leftNode)
            # print("Appended left node")
        if not currentNode.downNode is None and not currentNode.downNode in visitedNodes and not currentNode.downNode in availableNodes:
            availableNodes.append(currentNode.downNode)
            # print("Appended down node")
        if not currentNode.rightNode is None and not currentNode.rightNode in visitedNodes and not currentNode.rightNode in availableNodes:
            availableNodes.append(currentNode.rightNode)
            # print("Appended right node")
        sortAvailableList(availableNodes)
        # Goal State
        if maze[y][x] == 'G':
            print("A* Search has found G at (" + str(x) + ", " + str(y) + ")")
            print("Number of expanded nodes: " + str(visitedNodesCount))
            isGoalState = 1  # We have met the goal state
            currentNode.totalNodeCost = previousNode.totalNodeCost + 1
        previousNode = currentNode
    return getReturnPath(currentNode)


# Import Maze, then run path finding algorithms
def main(argv):
    method = ""  # Requested Search Method
    mazeFile = ""  # Maze File Name
    args = sys.argv
    usage = "Usage: search.py –method [INSERT METHOD] [MAZE TEXT FILE NAME]"
    usage1 = "Replace [INSERT METHOD] with either 'astar', 'depth', or 'breadth'"
    usage2 = "Replace [MAZE TEXT FILE NAME] with the name of the text document"

    # Input Validation
    if len(args) != 4:  # If Number of Arguments is wrong, give error.
        print("Incorrect Usage")
        print(usage)
        exit(1)
    else:

        try:
            method = args[2]
            mazeFile = args[3]
        except:
            print(usage)
            print(usage1)
            print(usage2)

    # Check to see if they put the flag correctly
    if args[1] != "-method":
        print(usage)
        print(usage1)
        print(usage2)

    # Try to import maze, if error, then they put the wrong file name
    try:
        mazeArr = importMaze(mazeFile)
    except:
        print("Error: Invalid Text File Name or file is in use.")
        exit(1)

    # Find Starting Location
    countX: int = 0
    countY: int = 0
    startX: int = 0
    startY: int = 0
    for r in mazeArr:

        for c in r:
            if c == 'S':
                startX = countX
                startY = countY
            countX = countX + 1
        countX = 0
        countY = countY + 1

    # Find Goal Location
    for r in mazeArr:

        for c in r:
            if c == 'G':
                goalX = countX
                goalY = countY
            countX = countX + 1
        countX = 0
        countY = countY + 1

    print("Start Coordinates: (" + str(startX) + ", " + str(startY) + ")")
    print()

    returnPath = []

    if method == "depth":
        returnPath = depthFirstSearch(startX, startY, mazeArr)
    elif method == "breadth":
        returnPath = breadthFirstSearch(startX, startY, mazeArr)
    elif method == "astar":
        returnPath = aStarSearch(startX, startY, mazeArr, goalX, goalY)
    else:
        print("Error: Invalid method name.")
        exit(1)
    print("Total Cost: " + str(len(returnPath)))
    print()
    printReturnPath(mazeArr, returnPath)

if __name__ == '__main__':
    main(sys.argv[1:])
