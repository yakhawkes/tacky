"""
    The Carbon coop challenge for hackmanchester 2017
"""

from ButtonPush import ButtonPush
#Green
button1 = ButtonPush(3)
#Red
button2 = ButtonPush(3)
while True:
    if button1.read() == True:
        #go faster
    else if button2.read() == True:
        #slow down
