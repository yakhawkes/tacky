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
motor.start(10,1)
print("here")
while True:
    print('-')
    if button1.read() == True:
        #go faster
        motor.goFaster()
        sys.sdout.write(motor.speed)
    if button2.read() == True:
        #slow down
        motor.slowDown()
        print(motor.speed)
    if button3.read() == True:
        motor.reverse()
    if button4.read() == True:
        break

