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
    global maxSpeed
    global minSpeed
    global speed
    pygame.mixer.music.load("click.mp3")
    if(speed + value)< maxSpeed and (speed + value) > minSpeed:
        speed += value

def playSound(speed):
    pygame.mixer.music.play()
    time.sleep(speed)

def storeSpeed():
    global storedSpeed
    global speed
    storeSpeed = speed

def checkSpeed():
    global speed
    global storedSpeed
    if speed * 0.9 > storedSpeed or speed * 1.1 < storedSpeed:
        speed = maxSpeed
        global direction
        pygame.mixer.music.load("siren.mp3")
        direction = 1

storedSpeed = 0
direction = 1
maxSpeed = 0.005
minSpeed = 0.5
speed = minSpeed / 4
motor = Motor()
useage = Useage()
pygame.mixer.init()
pygame.mixer.music.load("click.mp3")
#Green
button1 = Button(21)
button1.when_pressed = changeSpeed(useage.current)
#Red
button2 = Button(13)
button2.when_pressed = storeSpeed
#Blue
button3 = Button(5)
button3.when_pressed = checkSpeed
#Yellow
button4 = Button(4)

while True:
    t1 = Thread(target=playSound,args={speed})
    t2 = Thread(target=motor.makeStep,args={direction,speed})
    t1.start()
    t2.start()
