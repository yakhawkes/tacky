"""
    The Carbon coop challenge for hackmanchester 2017
"""
import time
from gpiozero import Button
from Motor import Motor
from Useage import Useage
#Green
button1 = Button(21)
#Red
button2 = Button(13)
#Blue
button3 = Button(5)
#Yellow
button4 = Button(4)

direction = 1
maxSpeed = 0.005
minSpeed = 0.5
speed = minSpeed / 2

motor = Motor()
useage = Useage()

inputType = 1
def changeSpeed(method):
    value = method()
    global maxSpeed
    global minSpeed
    global speed
    if(speed + value)< maxSpeed and (speed + value) > minSpeed:
        speed += value
    button1.when_pressed = changeSpeed(useage.current)
while True:
    motor.makeStep(direction)
    time.sleep(speed)
