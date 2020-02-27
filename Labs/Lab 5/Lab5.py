import CozmOSU as cozmo
from cozmo.util import degrees, distance_mm, speed_mmps

robot = cozmo.Robot()

def draw_polygon(n, cozmo):
  for x in range(n):
    cozmo.driveForward(200)
    cozmo.turn(-(180 - (180*(n-2) / n)))

def draw_star(n, cozmo):
  for x in range(n):
    cozmo.driveForward(200)
    cozmo.turn(-(180 - (180/n)))

def draw_arrow(cozmo):
  cozmo.driveForward(50)
  cozmo.turn(-60)
  cozmo.driveForward(100)
  cozmo.turn(-60)
  cozmo.driveForward(100)
  cozmo.turn(-60)
  cozmo.driveForward(50)
  cozmo.turn(-120)
  cozmo.driveForward(100)
  cozmo.turn(60)
  cozmo.driveForward(100)

def draw_thing(cozmo):
  cozmo.driveForward(75)
  cozmo.turn(-145)
  cozmo.driveForward(35)
  cozmo.turn(-35)
  cozmo.driveForward(25)
  cozmo.turn(90)
  cozmo.driveForward(25)
  cozmo.turn(-35)
  cozmo.driveForward(35)
  cozmo.turn(-145)
  cozmo.driveForward(75)

def draw_plus(cozmo):
  for x in range(4):
    cozmo.driveForward(50)
    cozmo.turn(-90)
    cozmo.driveForward(25)
    cozmo.turn(90)
    cozmo.driveForward(25)
    cozmo.turn(-90)

def main(cozmo : cozmo.Robot):
    choice = int(input("Enter 1 to make a n-gon, enter 2 to make a n point star, enter 3 to make an arrow, enter 4 to make a weird arrow thingy, or enter 5 to make a plus sign: : "))

    if choice == 1:
        n = int(input("Enter the number of sides you want: "))
        draw_polygon(n, cozmo)
    elif choice == 2:
        n = int(input("Enter the number of points you want: "))
        draw_star(n, cozmo)
    elif choice == 3:
        draw_arrow(cozmo)
    elif choice == 4:
        draw_thing(cozmo)
    elif choice == 5:
        draw_plus(cozmo)
    
robot.start(main)