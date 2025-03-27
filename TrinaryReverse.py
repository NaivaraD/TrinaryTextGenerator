from turtle import *

# create a dictionary for the letters, each being 0-26 in trinary with three places
library = {
    ' ': [0,0,0], 'A': [0,0,1], 'B': [0,0,2],
    'C': [0,1,0], 'D': [0,1,1], 'E': [0,1,2], 
    'F': [0,2,0], 'G': [0,2,1], 'H': [0,2,2],
    'I': [1,0,0], 'J': [1,0,1], 'K': [1,0,2],
    'L': [1,1,0], 'M': [1,1,1], 'N': [1,1,2],
    'O': [1,2,0], 'P': [1,2,1], 'Q': [1,2,2],
    'R': [2,0,0], 'S': [2,0,1], 'T': [2,0,2],
    'U': [2,1,0], 'V': [2,1,1], 'W': [2,1,2],
    'X': [2,2,0], 'Y': [2,2,1], 'Z': [2,2,2]
    }

# python directional numbers as compass variables
north = 0
east = 90
south = 180
west = 270

# dictionaries to make moving forward, left, and right easier
move = {north: (0, 1), east: (1, 0), south: (0, -1), west: (-1, 0)}
leftTurn = {north: west, east: north, south: east, west: south}
rightTurn = {north: east, east: south, south: west, west: north}

# dictionary to store what will be function calls as numbers
coOrdStamp = {0: 'start', 1: 'square', 2: 'nodeNext', 3: 'letterNext'}

# distances as variables
mindist = 30
dist = 1

# setup variables
startDir = north
startX = 0
startY = 0
startStamp = 0
coOrdsList = [{'x': startX, 'y': startY, 'dir': startDir, 'stamp': startStamp}]

#----------

# func to add coOrds to the list
def addCoOrd(distance, direction, dx, dy):
    coOrdsList.append({
        'x': coOrdsList[-1]['x'] + dx * distance * mindist,
        'y': coOrdsList[-1]['y'] + dy * distance * mindist,
        'dir': direction
    })

# func to move forward
def zero(distance, direction):
    dx, dy = move[direction]
    addCoOrd(distance, direction, dx, dy)

# func to move and turn left
def one(distance, direction):
    direction = leftTurn[direction]
    dx, dy = move[direction]
    addCoOrd(distance, direction, dx, dy)

# func to move and turn right
def two(distance, direction):
    direction = rightTurn[direction]
    dx, dy = move[direction]
    addCoOrd(distance, direction, dx, dy)

# preset turtle so it looks nice
def setup():
    mode('logo')
    hideturtle()
    width(2)

# make a starting arrow with a stamps
def start():
    bk(5)
    shape('arrow')
    stamp()
    fd(5)

# square stamp
def square():
    shape('square')
    stamp()

# make a shorthand for the arrows in between letters, to show which direction the node is facing
def letterNext():
    square()
    fd(10)
    shape('arrow')
    stamp()
    bk(10)

# make an arrow embedded in the squares so it looks smaller, with intent to increase legibility
def nodeNext():
    square()
    fd(5)
    shape('arrow')
    stamp()
    bk(5)

#----------

# create a dictionary for the directional functions
directionLib = {0: zero, 1: one, 2: two}

# ask what the user wants and put it in a variable
print('Please enter what you would like Ciphered:')
translate = list(input('>>> ').upper())

# main loop 1 that goes through each letter comparing the input to the library
for i in range(len(translate)):

    # puts that letter in a variable
    currentLetter = library[translate[i]]

    # makes a list out of the letters trinary
    for currentNode in range(len(currentLetter)):
        
        # draws the node direction of the letters trinary
        directionLib[currentLetter[currentNode]](dist, coOrdsList[-1]['dir'])

        # checks if current node is in the middle of a letter and adds var for tiny arrow
        if currentNode != len(currentLetter) - 1:
            coOrdsList[-1]['stamp'] = 2

        # var initialized
        overLapTest = 0

        # loop to check if any nodes are over lapping
        for overLap in range(len(coOrdsList)-1):
            # checks if x and y of current node is the same as any previous and changes var appropriately
            if coOrdsList[-1]['x'] == coOrdsList[overLap]['x'] and coOrdsList[-1]['y'] == coOrdsList[overLap]['y']:
                overLapTest = 1

            # adds overlap var to node index
            coOrdsList[-1]['over'] = overLapTest

        # print the last added item in coOrdsList
        print(coOrdsList[len(coOrdsList) - 1])
    
    # checks if current node is at the end of a letter and adds var for large arrow
    if i != len(translate) - 1:
        coOrdsList[-1]['stamp'] = 3

    # checks if current node is at the end and adds var for a square
    if i == len(translate) - 1:
        coOrdsList[-1]['stamp'] = 1

# print full coOrdsList
print(coOrdsList)

#----------

# dictionary to actually call stamp funcs
funcStamp = {'start': start, 'square': square, 'nodeNext': nodeNext, 'letterNext': letterNext}

setup()

# main loop 2 that walks through the coOrdsList and puts the turtle in the correct location, in the correct direction, and puts a stamp down
for i in range(len(coOrdsList)):
    goto(x = coOrdsList[i]['x'], y = coOrdsList[i]['y'])
    setheading(coOrdsList[i]['dir'])
    funcStamp[coOrdStamp[coOrdsList[i]['stamp']]]()

# Goodbye!
exitonclick()