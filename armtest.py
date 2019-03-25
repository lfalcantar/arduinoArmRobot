import RPi.GPIO as GPIO
from gpiozero import Servo
from time import sleep
import readchar

myCorrection=0
maxPW=(2.0+myCorrection)/1000
minPW=(1.0-myCorrection)/1000
 
servo = Servo(26,min_pulse_width=minPW,max_pulse_width=maxPW)
servo2 = Servo(21,min_pulse_width=minPW,max_pulse_width=maxPW)              #right servo
servoPINBase = Servo(17,min_pulse_width=minPW,max_pulse_width=maxPW)        # This is to control the base movement
servoPINClaw = Servo(4,min_pulse_width=minPW,max_pulse_width=maxPW)         # This is to control the claw
basePos = 0
stdIncrement = .1

def baseRight():
    global basePos
    global stdIncrement
    if (basePos < 1):
        basePos = basePos + stdIncrement
        base.value = basePos
        sleep(0.5)
        
def baseLeft():
    global basePos
    global stdIncrement
    if (basePos > -1):
        basePos = basePos - stdIncrement
        base.value = basePos
        sleep(0.5)
    
def pinchClaw():
    servoPINClaw.value = -.9
    ##time.sleep(0.5)
    
def openClaw():
   servoPINClaw.value = .9
    ##time.sleep(0.5)
    
def armUp():
    servo.value= 1
    servo2.value= -0.3
    sleep(0.5)
    
def armDown():
    servo.value= -.85
    servo2.value= .9
    sleep(0.5)
    
while True:
    # This will get the input
    charInput = readchar.readkey()
    print(repr(readchar.readkey()))
    
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
                
    # Escape character
    if(charInput == "t"):
        print "Program ended"
        break
    
base.stop()
GPIO.cleanup()
