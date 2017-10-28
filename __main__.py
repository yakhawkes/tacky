"""
    The Carbon coop challenge for hackmanchester 2017
"""

from ButtonPush import ButtonPush
#Green
button1 = ButtonPush(21)
#Red
button2 = ButtonPush(13)
#Blue
button3 = ButtonPush(5)
#Yellow
button4 = ButtonPush(4)

motor = Motor(1,1)
motor.start(1,1)
while True:
    if button1.read() == True:
        #go faster
        motor.goFaster()
    else if button2.read() == True:
        #slow down
        motor.slowDown()
    else if button3.read() == True:
        motor.reverse()
