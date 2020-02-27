import random
import CozmOSU as cozmo
from cozmo.util import degrees, distance_mm, speed_mmps

robot = cozmo.Robot()

def roll_a_die(data, card, cozmo):
    dice = random.randint(1, 6)

    if card == "Addition":
        print("You gained " + str(dice) + " point(s)")
        data[2] += dice 
    elif card == "Deduction":
        print("You lost " + str(dice) + " point(s)")
        data[2] -= dice
    elif card == "Move":
        data = move(data, dice, cozmo)
    
    return data


def draw_a_card(data, cozmo):
    card = random.randint(1, 4)

    if card == 1:
        return roll_a_die(data, "Addition", cozmo)
    elif card == 2:
        return roll_a_die(data, "Deduction", cozmo)
    else:
        return roll_a_die(data, "Move", cozmo)

def move(data, dice, cozmo):
    for x in range(dice):
        if data[3] == 6 or data[3] == 8:
            cozmo.turn(-90)
        elif data[3] == 13 or data[3] == 15:
            cozmo.turn(90)

        cozmo.driveForward(150, 200)
        data[3] += 1
    
    print("You moved " + str(dice) + " square(s)")

    return data

def play(data, cozmo):
    while data[0] == False:
        data[1] += 1
        data = draw_a_card(data, cozmo)

        print("Points: " + str(data[2]))
        
        if data[3] >= 19:
            print("You made it to the end!\n")
            data[0] = True
        else:
            print("You're on square " + str(data[3]) + "\n")

    return data

def main(cozmo : cozmo.Robot):
    data = [False, 0, 0, 0]
    data = play(data, cozmo)
    score = (data[1] * 4) + data[2]
    cozmo.say("The final score is: " + str(score) + "\n")

robot.start(main)
