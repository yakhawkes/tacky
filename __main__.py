"""
    The Carbon coop challenge for hackmanchester 2017
"""
from threading import Thread
import time
from gpiozero import Button
from Motor import Motor
from Useage import Useage
import pygame

def changeSpeed(method):
    value = method()
    global sound
    global maxSpeed
    global minSpeed
    sound = "click"
    if(speed + value)< maxSpeed and (speed + value) > minSpeed:
        global speed
        speed += value

def playSound(speed):
    pygame.mixer.music.play()
    time.sleep(speed)

def storeSpeed(speed):
    global storedSpeed
    storeSpeed = speed

def checkSpeed(speed):
    if speed * 0.9 < storedSpeed or speed * 1.1 > storedSpeed:
        speed = maxSpeed()
        global sound
        global direction
        sound = "siren"
        direction = 1

sound = "click"
storedSpeed = 0
direction = 1
maxSpeed = 0.005
minSpeed = 0.5
speed = minSpeed / 2
motor = Motor()
useage = Useage()
pygame.mixer.init()
pygame.mixer.music.load("click.mp3")
#Green
button1 = Button(21)
button1.when_pressed = changeSpeed(useage.current)
#Red
button2 = Button(13)
button2.when_pressed = storeSpeed(speed)
#Blue
button3 = Button(5)
button3.when_pressed = checkSpeed(speed)
#Yellow
button4 = Button(4)

while TRUE:
    t1 = Thread(target=playSound,args={speed})
    t2 = Thread(target=motor.makeStep,args={direction,speed})
    t1.start()
    t2.start()
