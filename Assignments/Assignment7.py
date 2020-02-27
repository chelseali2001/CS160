import turtle
from random import randint
import random

def drawA():
  myTurtle.lt(90)
  myTurtle.fd(100)
  myTurtle.rt(90)
  myTurtle.fd(50)
  myTurtle.rt(90)
  myTurtle.fd(100)
  myTurtle.rt(90)
  myTurtle.pu()
  myTurtle.fd(50)
  myTurtle.pd()
  myTurtle.rt(90)
  myTurtle.fd(50)
  myTurtle.rt(90)
  myTurtle.fd(50)
  myTurtle.rt(90)
  myTurtle.fd(50)
  myTurtle.lt(90)

def drawB():
  myTurtle.lt(90)
  myTurtle.fd(100)
  myTurtle.rt(90)
  myTurtle.fd(50)
  myTurtle.rt(90)
  myTurtle.fd(100)
  myTurtle.rt(90)
  myTurtle.fd(50)
  myTurtle.rt(90)
  myTurtle.fd(50)
  myTurtle.rt(90)
  myTurtle.fd(50)
  myTurtle.rt(90)
  myTurtle.fd(50)
  myTurtle.lt(90)

def drawC():
  myTurtle.lt(90)
  myTurtle.fd(100)
  myTurtle.rt(90)
  myTurtle.fd(50)
  myTurtle.rt(90)
  myTurtle.pu()
  myTurtle.fd(100)
  myTurtle.rt(90)
  myTurtle.pd()
  myTurtle.fd(50)
  myTurtle.rt(180)
  myTurtle.fd(50)

def drawE():
  myTurtle.lt(90)
  myTurtle.fd(100)
  myTurtle.rt(90)
  myTurtle.fd(50)
  myTurtle.rt(90)
  myTurtle.pu()
  myTurtle.fd(50)
  myTurtle.rt(90)
  myTurtle.pd()
  myTurtle.fd(50)
  myTurtle.lt(90)
  myTurtle.fd(50)
  myTurtle.lt(90)
  myTurtle.fd(50)

def drawH():
  myTurtle.lt(90)
  myTurtle.fd(100)
  myTurtle.rt(180)
  myTurtle.fd(50)
  myTurtle.lt(90)
  myTurtle.fd(50)
  myTurtle.lt(90)
  myTurtle.fd(50)
  myTurtle.rt(180)
  myTurtle.fd(100)
  myTurtle.lt(90)

def drawI():
  myTurtle.lt(90)
  myTurtle.pu()
  myTurtle.fd(100)
  myTurtle.rt(90)
  myTurtle.pd()
  myTurtle.fd(50)
  myTurtle.rt(180)
  myTurtle.fd(25)
  myTurtle.lt(90)
  myTurtle.fd(100)
  myTurtle.rt(90)
  myTurtle.fd(25)
  myTurtle.rt(180)
  myTurtle.fd(50)

def drawL():
  myTurtle.lt(90)
  myTurtle.fd(100)
  myTurtle.rt(180)
  myTurtle.fd(100)
  myTurtle.lt(90)
  myTurtle.fd(50)

def drawS():
  myTurtle.fd(50)
  myTurtle.lt(90)
  myTurtle.fd(50)
  myTurtle.lt(90)
  myTurtle.fd(50)
  myTurtle.rt(90)
  myTurtle.fd(50)
  myTurtle.rt(90)
  myTurtle.fd(50)

  myTurtle.pu()
  myTurtle.rt(90)
  myTurtle.fd(100)
  myTurtle.lt(90)

def drawSmile():
  myTurtle.pu()
  myTurtle.fd(25)
  myTurtle.rt(90)
  myTurtle.pd()
  myTurtle.fd(25)
  myTurtle.lt(90)
  myTurtle.pu()
  myTurtle.fd(25)
  myTurtle.lt(90)
  myTurtle.pd()
  myTurtle.fd(25)
  myTurtle.rt(90)
  myTurtle.pu()
  myTurtle.fd(25)
  myTurtle.rt(90)
  myTurtle.fd(35)
  myTurtle.pd()
  myTurtle.fd(15)
  myTurtle.rt(90)
  myTurtle.fd(75)
  myTurtle.rt(90)
  myTurtle.fd(15)

myTurtle = turtle.Turtle()
word = ["CHELSEA LI", "BEE", "CALL", "HI", "other"]
choice = int(input("How many words do you want to print?: "))

for x in range(choice):
  val = random.choice(word)

  if val == "other":
    drawSmile()
  else:
    for i in val:
      if i == "A":
        drawA()
      elif i == "B":
        drawB()
      elif i == "C":
        drawC()
      elif i == "E":
        drawE()
      elif i == "H":
        drawH()
      elif i == "I":
        drawI()
      elif i == "L":
        drawL()
      elif i == "S":
        drawS()
      else:
        myTurtle.pu()
        myTurtle.fd(25)

      myTurtle.pu()
      myTurtle.fd(15)
      myTurtle.pd()
  
  myTurtle.pu()

  if val == "CHELSEA LI":
    myTurtle.rt(90)
    myTurtle.fd(25)
    myTurtle.rt(90)
    myTurtle.fd(625)
    myTurtle.lt(90)
    myTurtle.fd(100)
    myTurtle.lt(90)
  elif val == "BEE":
    myTurtle.rt(90)
    myTurtle.fd(25)
    myTurtle.rt(90)
    myTurtle.fd(195)
    myTurtle.lt(90)
    myTurtle.fd(100)
    myTurtle.lt(90)
  elif val == "CALL":
    myTurtle.rt(90)
    myTurtle.fd(25)
    myTurtle.rt(90)
    myTurtle.fd(260)
    myTurtle.lt(90)
    myTurtle.fd(100)
    myTurtle.lt(90) 
  elif val == "HI":
    myTurtle.rt(90)
    myTurtle.fd(25)
    myTurtle.rt(90)
    myTurtle.fd(130)
    myTurtle.lt(90)
    myTurtle.fd(100)
    myTurtle.lt(90)
  elif val == "other":
    myTurtle.rt(180)
    myTurtle.fd(150)
    myTurtle.lt(90)

  myTurtle.pd()