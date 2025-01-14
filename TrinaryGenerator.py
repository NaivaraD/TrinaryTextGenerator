# import graphic depictor
from turtle import *

#----------

# preset turtle so it looks nice
def Setup():
    mode("logo")
    hideturtle()
    width(2)

# create a shorthand for a Pixel
def Pixel():
    down()
    forward(1)
    backward(1)
    up()

# make a nice starting arrow with pixels rather than stamps
def Start():
    Pixel()
    bk(4)
    rt(90)
    bk(5)
    Pixel()
    fd(3)
    lt(90)
    fd(2)
    Pixel()
    home()
    bk(4)
    lt(90)
    bk(4)
    Pixel()
    fd(2)
    rt(90)
    fd(2)
    Pixel()
    home()
    down()

# make a starting arrow with a stamps
def Start2():
    pensize(5)
    shape("arrow")
    left(90)
    stamp()

# make a shorthand for the arrows in between letters, to show which direction the node is facing
def Next():
    forward(10)
    shape("arrow")
    stamp()
    backward(10)

#----------

# create the default (0) movement of forward with a node
def Zero():
    forward(50)
    shape("square")
    stamp()

# create the first (1) movement of left with a node
def One():
    left(90)
    forward(50)
    shape("square")
    stamp()

# create the second (2) movement of right with a node
def Two():
    right(90)
    forward(50)
    shape("square")
    stamp()

#----------

# create a library for the letters, each being 0-26 in trinary with three places

library = {' ': '000', 'A': '001', 'B': '002', 'C': '010', 'D': '011', 'E': '012', 'F': '020', 'G': '021', 'H': '022',
            'I': '100', 'J': '101', 'K': '102', 'L': '110', 'M': '111', 'N': '112', 'O': '120', 'P': '121', 'Q': '122',
            'R': '200', 'S': '201', 'T': '202', 'U': '210', 'V': '211', 'W': '212', 'X': '220', 'Y': '221', 'Z': '222'}

#----------

# ask for and recieve input on what is to be translated, and make it upper case for convenience
print("Please enter what you would like Ciphered: ")
Translate = input(">>> ").upper()

# turn input string into a list to be able to walk through it and output text
Translate = list(Translate)

# set up turtle visually
Setup()
Start()

# main loop that goes through each letter comparing the input to the library
for i in range(len(Translate)):

    # pulls out the first item of the list to compare, then discards
    x = Translate.pop(0)

    # checking if the current letter is in the library
    if x in library:

        # puts that letter in a variable
        currentLetter = list(library[x])

        # makes a list out of the letters trinary
        for y in range(len(currentLetter)):
            # pulls out the first item of the list to compare, then discards
            currentNumber = currentLetter.pop(0)

            # draws the node direction of the letters trinary

            if currentNumber == '0':
                Zero()

            if currentNumber == '1':
                One()

            if currentNumber == '2':
                Two()

    # checks for the last letter and then stamps the connecting arrow as appropriate
    if len(Translate) != 0:
        Next()

# All Done!
print("All done! Please click on glyph to close.")

# Goodbye!
exitonclick()