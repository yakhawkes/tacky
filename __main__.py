"""
    The Carbon coop challenge for hackmanchester 2017
"""
from threading import Thread
import time
from gpiozero import Button
from Motor import Motor
from Useage import Useage
import pygame

def changeSpeed():
    global useage
    value = useage.current()
    global maxSpeed
    global minSpeed
    global speed
    pygame.mixer.music.load("click.mp3")
    if(speed + value)>= maxSpeed and (speed + value) <= minSpeed:
        speed += value

def playSound(speed):
    pygame.mixer.music.play()
    time.sleep(speed)

def storeSpeed():
    """(none)->none Store the speed value"""
    global storedSpeed
    global speed
    storedSpeed = speed

def checkSpeed():
    global speed
    global storedSpeed
    global direction
    if storedSpeed * 0.9 > speed or storedSpeed * 1.1 < speed:
        speed = maxSpeed
        pygame.mixer.music.load("siren.mp3")
        direction = 1

def reverse():
    global direction
    direction = direction *-1

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
button1.when_pressed = changeSpeed
#Red
button2 = Button(13)
button2.when_pressed = storeSpeed
#Blue
button3 = Button(5)
button3.when_pressed = checkSpeed
#Yellow
button4 = Button(4)
button4.when_pressed = reverse

while True:
    t1 = Thread(target=playSound,args={speed})
    t2 = Thread(target=motor.makeStep,kwargs={'directon': direction,'speed': speed})
    t1.start()
    t2.start()
