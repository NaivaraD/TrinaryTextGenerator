# import graphic depictor
from turtle import *

#----------

# preset turtle so it looks nice
def setup():
    mode("logo")
    hideturtle()
    width(2)

# make a starting arrow with a stamps
def start():
    bk(5)
    shape("arrow")
    stamp()
    fd(5)

# make a shorthand for the arrows in between letters, to show which direction the node is facing
def next():
    fd(10)
    shape("arrow")
    stamp()
    bk(10)

# make an arrow embedded in the squares so it looks smaller, with intent to increase legibility
def nodeDir():
    fd(5)
    shape("arrow")
    stamp()
    bk(5)

#----------

# create the default (0) movement of forward with a node
def zero(distance):
    fd(4)
    down()
    fd(distance*30)
    shape("square")
    stamp()
    nodeDir()

# create the first (1) movement of left with a node
def one(distance):
    lt(90)
    fd(3)
    down()
    fd(distance*30)
    shape("square")
    stamp()
    nodeDir()

# create the second (2) movement of right with a node
def two(distance):
    rt(90)
    fd(3)
    down()
    fd(distance*30)
    shape("square")
    stamp()
    nodeDir()

#----------

# create a library for the letters, each being 0-26 in trinary with three places

library = { ' ': '000', 'A': '001', 'B': '002', 'C': '010', 'D': '011', 'E': '012', 'F': '020', 'G': '021', 'H': '022',
            'I': '100', 'J': '101', 'K': '102', 'L': '110', 'M': '111', 'N': '112', 'O': '120', 'P': '121', 'Q': '122',
            'R': '200', 'S': '201', 'T': '202', 'U': '210', 'V': '211', 'W': '212', 'X': '220', 'Y': '221', 'Z': '222'}

#----------

# ask for and recieve input on what is to be translated, and make it upper case for convenience
print("Please enter what you would like Ciphered:")
translate = input(">>> ").upper()

# turn input string into a list to be able to walk through it and output text
translate = list(translate)

# set up turtle visually
setup()
start()

dist = 1

# main loop that goes through each letter comparing the input to the library
for i in range(len(translate)):

    # grabs the each item in the list in turn to compare
    x = translate[i]

    # checking if the current letter is in the library
    if x in library:

        # puts that letter in a variable
        currentLetter = list(library[x])

        # makes a list out of the letters trinary
        for y in range(len(currentLetter)):
            
            # grabs the each item in the list in turn to compare
            currentNumber = currentLetter[y]

            # draws the node direction of the letters trinary

            if currentNumber == '0':
                zero(dist)

            elif currentNumber == '1':
                one(dist)

            elif currentNumber == '2':
                two(dist)

    # checks for the last letter and then stamps the connecting arrow as appropriate
    if i != len(translate) - 1:
        next()

# All Done!
print("All done! Please click on glyph to close.")

# Goodbye!
exitonclick()