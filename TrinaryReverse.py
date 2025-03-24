
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

north = 0
east = 90
south = 180
west = 270

startDir = north
startX = 0
startY = 0
mindist = 30
dist = 1
coOrdsList = [{'x': startX, 'y': startY, 'dir': startDir}]

#----------

def zero(distance, direction):
    if direction == north:
        coOrdsList.append({'x': coOrdsList[-1]['x'], 'y': coOrdsList[-1]['y']+distance*mindist, 'dir': north})

    if direction == west:
        coOrdsList.append({'x': coOrdsList[-1]['x']-distance*mindist, 'y': coOrdsList[-1]['y'], 'dir': west})

    if direction == south:
        coOrdsList.append({'x': coOrdsList[-1]['x'], 'y': coOrdsList[-1]['y']-distance*mindist, 'dir': south})

    if direction == east:
        coOrdsList.append({'x': coOrdsList[-1]['x']+distance*mindist, 'y': coOrdsList[-1]['y'], 'dir': east})

def one(distance, direction):
    if direction == north:
        coOrdsList.append({'x': coOrdsList[-1]['x']-distance*mindist, 'y': coOrdsList[-1]['y'], 'dir': west})

    if direction == west:
        coOrdsList.append({'x': coOrdsList[-1]['x'], 'y': coOrdsList[-1]['y']-distance*mindist, 'dir': south})

    if direction == south:
        coOrdsList.append({'x': coOrdsList[-1]['x']+distance*mindist, 'y': coOrdsList[-1]['y'], 'dir': east})

    if direction == east:
        coOrdsList.append({'x': coOrdsList[-1]['x'], 'y': coOrdsList[-1]['y']+distance*mindist, 'dir': north})

def two(distance, direction):
    if direction == north:
        coOrdsList.append({'x': coOrdsList[-1]['x']+distance*mindist, 'y': coOrdsList[-1]['y'], 'dir': east})

    if direction == west:
        coOrdsList.append({'x': coOrdsList[-1]['x'], 'y': coOrdsList[-1]['y']+distance*mindist, 'dir': north})

    if direction == south:
        coOrdsList.append({'x': coOrdsList[-1]['x']-distance*mindist, 'y': coOrdsList[-1]['y'], 'dir': west})

    if direction == east:
        coOrdsList.append({'x': coOrdsList[-1]['x'], 'y': coOrdsList[-1]['y']-distance*mindist, 'dir': south})

#----------

# create a dictionary for the directional functions
directionLib = {0: zero, 1: one, 2: two}

print('Please enter what you would like Ciphered:')
translate = list(input('>>> ').upper())

# main loop that goes through each letter comparing the input to the library
for i in range(len(translate)):

    # puts that letter in a variable
    currentLetter = library[translate[i]]

    # makes a list out of the letters trinary
    for currentNode in range(len(currentLetter)):
        
        # draws the node direction of the letters trinary
        directionLib[currentLetter[currentNode]](dist, coOrdsList[-1]['dir'])

        overLapTest = 0

        for overLap in range(len(coOrdsList)-1):

            if coOrdsList[-1]['x'] == coOrdsList[overLap]['x'] and coOrdsList[-1]['y'] == coOrdsList[overLap]['y']:
                overLapTest = 1

            coOrdsList[-1]['over'] = overLapTest

        # print the last added item in coOrdsList
        print(coOrdsList[len(coOrdsList) - 1])

print(coOrdsList)