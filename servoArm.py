import RPi.GPIO as GPIO
import time

# Variables here
servoPINBase = 17        # This is to control the base movement
servoPINClaw = 4         # This is to control the claw
servoPINUD = 27          # This is to control the up and down movement
servoPINFB = 19            # This is to control the forward and back movement

# Funtions here
def getch():
    inp = raw_input()
    return inp

def baseRight():
    base.ChangeDutyCycle(2.5)
    time.sleep(0.5)
        
def baseLeft():
    base.ChangeDutyCycle(12.5)
    time.sleep(0.5)
    
def pinchClaw():
    claw.ChangeDutyCycle(2.5)
    time.sleep(0.5)
    
def openClaw():
    claw.ChangeDutyCycle(12.5)
    time.sleep(0.5)
    
def armUp():
    upDown.ChangeDutyCycle(12.5)    # This goes back
    time.sleep(0.5)
    
def armDown():
    upDown.ChangeDutyCycle(2.5)
    time.sleep(0.5)
    
def armForward():
    forBack.ChangeDutyCycle(2.5)    # This goes back
    time.sleep(0.5)

def armBack():
    forBack.ChangeDutyCycle(12.5)    # This goes back
    time.sleep(0.5)

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
    
    # Left base movement
    if(charInput == "l"):
        baseLeft()
        
    # Right base movement
    if(charInput == "r"):
        baseRight()
        
    # Pinch claw
    if(charInput == "p"):
        pinchClaw()
        
    # Open claw
    if(charInput == "o"):
        openClaw()
        
    # Move arm up
    if(charInput == "u"):
        armUp()
    
    # Move arm down
    if(charInput == "d"):
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
