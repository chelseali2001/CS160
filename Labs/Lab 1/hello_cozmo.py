import CozmOSU as cozmo

robot = cozmo.Robot()

def main(cozmo : cozmo.Robot):
    cozmo.say("Hello Chelsea Li")
    
robot.start(main)
