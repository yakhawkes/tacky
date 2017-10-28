"""
    The Carbon coop challenge for hackmanchester 2017
"""
import time
from ButtonPush import ButtonPush
from Motor import Motor
#Green
button1 = ButtonPush(21)
#Red
button2 = ButtonPush(13)
#Blue
button3 = ButtonPush(5)
#Yellow
button4 = ButtonPush(4)

motor = Motor()
speed = 1
while True:
    if speed > 1:
        motor.advance()
    if button1.read() == True:
        #go faster
        speed+=10
    print(speed)

    if button2.read() == True:
        #slow down
        speed-=10
        print(speed)

    if button3.read() == True:
        pass

    if button4.read() == True:
        break

    
