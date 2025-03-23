# import graphic depictor
from turtle import *

minDist = 30

#----------

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

# make a shorthand for the arrows in between letters, to show which direction the node is facing
def letterNext():
    fd(10)
    shape('arrow')
    stamp()
    bk(10)

# make an arrow embedded in the squares so it looks smaller, with intent to increase legibility
def nodeNext():
    fd(5)
    shape('arrow')
    stamp()
    bk(5)

#----------

# create the default (0) movement of forward with a node
def zero(distance):
    fd(distance*minDist)
    shape('square')
    stamp()

# create the first (1) movement of left with a node
def one(distance):
    lt(90)
    fd(distance*minDist)
    shape('square')
    stamp()

# create the second (2) movement of right with a node
def two(distance):
    rt(90)
    fd(distance*minDist)
    shape('square')
    stamp()

#----------

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

# create a dictionary for the directional functions
directionLib = {0: zero, 1: one, 2: two}

#----------

# ask for and recieve input as a list on what is to be ciphered, and make it upper case for convenience
print('Please enter what you would like Ciphered:')
translate = list(input('>>> ').upper())

# set up turtle visually
setup()
start()

dist = 1
coOrdsList = [{'x': round(xcor()), 'y': round(ycor()), 'dir': round(heading())}]

# main loop that goes through each letter comparing the input to the library
for i in range(len(translate)):

    # puts that letter in a variable
    currentLetter = library[translate[i]]

    # makes a list out of the letters trinary
    for currentNode in range(len(currentLetter)):
        
        # draws the node direction of the letters trinary
        directionLib[currentLetter[currentNode]](dist)

        if currentNode != len(currentLetter) - 1:
            nodeNext()

        # make a list of all the coordinates and directions of the nodes as a dict
        coOrdsList.append({'x': round(xcor()), 'y': round(ycor()), 'dir': round(heading())})

        overLapTest = 0

        for overLap in range(len(coOrdsList)-1):

            if coOrdsList[-1]['x'] == coOrdsList[overLap]['x'] and coOrdsList[-1]['y'] == coOrdsList[overLap]['y']:
                overLapTest = 1

            coOrdsList[-1]['over'] = overLapTest

        # print the last added item in coOrdsList
        print(coOrdsList[len(coOrdsList) - 1])

    # checks for the last letter and then stamps the connecting arrow as appropriate
    if i != len(translate) - 1:
        letterNext()

print(coOrdsList)

# All Done!
print('All done! Please click on glyph to close.')

# Goodbye!
exitonclick()