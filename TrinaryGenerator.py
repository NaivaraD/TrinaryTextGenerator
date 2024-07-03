from turtle import *

#----------

def Setup():
    mode("logo")
    hideturtle()
    width(2)

def Pixel():
    down()
    forward(1)
    backward(1)
    up()

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

def Start2():
    pensize(5)
    shape("arrow")
    left(90)
    stamp()

def Next():
    forward(10)
    shape("arrow")
    stamp()

#----------

def Zero():
    forward(50)
    shape("square")
    stamp()

def One():
    left(90)
    forward(50)
    shape("square")
    stamp()

def Two():
    right(90)
    forward(50)
    shape("square")
    stamp()

#----------

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

#print("Please enter what you would like Ciphered with each letter separated with a space:")
#Translate = input(">>> ").upper().split()
Translate = input("Please enter what you would like Ciphered with each letter separated with a space: ").upper().split()
print(Translate)
TransLen = len(Translate)
print(TransLen)
Setup()
Start2()
for i in range(TransLen):
    x = Translate.pop(0)
    if x == "-":
        CharSp()

    elif x == "A":
        CharaA()

    elif x == "B":
        CharaB()

    elif x == "C":
        CharaC()

    elif x == "D":
        CharaD()

    elif x == "E":
        CharaE()

    elif x == "F":
        CharaF()

    elif x == "G":
        CharaG()

    elif x == "H":
        CharaH()

    elif x == "I":
        CharaI()

    elif x == "J":
        CharaJ()

    elif x == "K":
        CharaK()

    elif x == "L":
        CharaL()

    elif x == "M":
        CharaM()

    elif x == "N":
        CharaN()

    elif x == "O":
        CharaO()

    elif x == "P":
        CharaP()

    elif x == "Q":
        CharaQ()

    elif x == "R":
        CharaR()

    elif x == "S":
        CharaS()

    elif x == "T":
        CharaT()

    elif x == "U":
        CharaU()

    elif x == "V":
        CharaV()

    elif x == "W":
        CharaW()

    elif x == "Y":
        CharaY()

    elif x == "X":
        CharaX()

    elif x == "Z":
        CharaZ()

    if i != TransLen - 1:
        Next()
print("All done!")

exitonclick()