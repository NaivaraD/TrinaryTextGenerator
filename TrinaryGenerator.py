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

def CharSp():
    Zero()
    Zero()
    Zero()

def CharaA():
    Zero()
    Zero()
    One()

def CharaB():
    Zero()
    Zero()
    Two()

def CharaC():
    Zero()
    One()
    Zero()

def CharaD():
    Zero()
    One()
    One()

def CharaE():
    Zero()
    One()
    Two()

def CharaF():
    Zero()
    Two()
    Zero()

def CharaG():
    Zero()
    Two()
    One()

def CharaH():
    Zero()
    Two()
    Two()

def CharaI():
    One()
    Zero()
    Zero()

def CharaJ():
    One()
    Zero()
    One()

def CharaK():
    One()
    Zero()
    Two()

def CharaL():
    One()
    One()
    Zero()

def CharaM():
    One()
    One()
    One()

def CharaN():
    One()
    One()
    Two()

def CharaO():
    One()
    Two()
    Zero()

def CharaP():
    One()
    Two()
    One()

def CharaQ():
    One()
    Two()
    Two()

def CharaR():
    Two()
    Zero()
    Zero()

def CharaS():
    Two()
    Zero()
    One()

def CharaT():
    Two()
    Zero()
    Two()

def CharaU():
    Two()
    One()
    Zero()

def CharaV():
    Two()
    One()
    One()

def CharaW():
    Two()
    One()
    Two()

def CharaX():
    Two()
    Two()
    Zero()

def CharaY():
    Two()
    Two()
    One()

def CharaZ():
    Two()
    Two()
    Two()

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

    # library again basically

    if x == " ":
        CharSp()

    if x == "A":
        CharaA()

    if x == "B":
        CharaB()

    if x == "C":
        CharaC()

    if x == "D":
        CharaD()

    if x == "E":
        CharaE()

    if x == "F":
        CharaF()

    if x == "G":
        CharaG()

    if x == "H":
        CharaH()

    if x == "I":
        CharaI()

    if x == "J":
        CharaJ()

    if x == "K":
        CharaK()

    if x == "L":
        CharaL()

    if x == "M":
        CharaM()

    if x == "N":
        CharaN()

    if x == "O":
        CharaO()

    if x == "P":
        CharaP()

    if x == "Q":
        CharaQ()

    if x == "R":
        CharaR()

    if x == "S":
        CharaS()

    if x == "T":
        CharaT()

    if x == "U":
        CharaU()

    if x == "V":
        CharaV()

    if x == "W":
        CharaW()

    if x == "Y":
        CharaY()

    if x == "X":
        CharaX()

    if x == "Z":
        CharaZ()

    # checks for the last letter and then stamps the connecting arrow as appropriate
    if len(Translate) != 0:
        Next()

# All Done!
print("All done! Please click on glyph to close.")

# Goodbye!
exitonclick()