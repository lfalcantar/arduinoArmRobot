import RPi.GPIO as GPIO
import time
import readchar

# Variables here
servoPINBase = 21        # This is to control the base movement
servoPINClaw = 4        # This is to control the claw
servoPINUD = 26          # This is to control the up and down movement
servoPINFB = 16            # This is to control the forward and back movement
basePos = 2.5
stdIncrement = .5

leftarm = 6
rightarm = 6
def getch():
    inp = raw_input()
    return inp


def baseRight():
    # global basePos
    # global stdIncrement
    # basePos += stdIncrement
    # base.ChangeDutyCycle(basePos)
    base.ChangeDutyCycle(2.5)
    time.sleep(0.5)
    
def baseLeft():
    # global basePos
    # global stdIncrement
    # basePos -= stdIncrement
    # base.ChangeDutyCycle(basePos)
    base.ChangeDutyCycle(12)
    time.sleep(0.5)
    

def pinchClaw():
    claw.ChangeDutyCycle(2.5)
    ##time.sleep(0.5)
    
def openClaw():
    claw.ChangeDutyCycle(12.5)
    ##time.sleep(0.5)
    
def armUp():
    upDown.ChangeDutyCycle(10)
    fowardInitial = 12.5
    forBack.ChangeDutyCycle(fowardInitial)# This goes back
    time.sleep(0.5)
    
def armDown():
    upDown.ChangeDutyCycle(2.5)
    fowardInitial = 12.5
    forBack.ChangeDutyCycle(12.5)
    time.sleep(0.5)
    
def armForward():
    upDown.ChangeDutyCycle(12)
    forBack.ChangeDutyCycle(2.5)    # This goes back
    time.sleep(0.5)

def armBack():
    upDown.ChangeDutyCycle(12)
    forBack.ChangeDutyCycle(12)    # This goes back
    time.sleep()

GPIO.setmode(GPIO.BCM)
GPIO.setup(servoPINBase, GPIO.OUT)
GPIO.setup(servoPINClaw, GPIO.OUT)
GPIO.setup(servoPINUD, GPIO.OUT)
GPIO.setup(servoPINFB, GPIO.OUT)

# Init the servos
base = GPIO.PWM(servoPINBase, 50)      # GPIO 17 for PWM with 50Hz
base.start(2.5)                        # Init

claw = GPIO.PWM(servoPINClaw, 50)
claw.start(2.5)

upDown = GPIO.PWM(servoPINUD, 50)
upDown.start(2.5)

forBack = GPIO.PWM(servoPINFB, 50)
forBack.start(2.5)

while True:
    # This will get the input
    charInput = getch()
    #charInput = readchar.readkey()
    #print(repr(readchar.readkey()))
    
    # Left base movement
    if(charInput == "a"):
        baseLeft()
        
    # Right base movement
    if(charInput == "d"):
        baseRight()
        
    # Pinch claw
    if(charInput == "p"):
        pinchClaw()
        
    # Open claw
    if(charInput == "o"):
        openClaw()
        
    # Move arm up
    if(charInput == "w"):
        armUp()
    
    # Move arm down
    if(charInput == "s"):
        armDown()
        
    # MOve arm forward
    if(charInput == "f"):
        armForward()
        
    # Move arm backward
    if(charInput == "b"):
        armBack()
        
    # Escape character
    if(charInput == "t"):
        print "Program ended"
        break
    
base.stop()
GPIO.cleanup()