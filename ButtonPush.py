class ButtonPush(object):
    """ButtonPush"""
    def __init__(self, pinNumber):
        self.pinNumber = pinNumber
        #set up the GPIO
        import RPi.GPIO as GPIO
        self.GPIO = GPIO
        self.GPIO.setmode(GPIO.BCM)
        #try to set the pin to listen
        self.pin = False == self.GPIO.setup(pinNumber, self.GPIO.IN, pull_up_down=self.GPIO.PUD_UP)

    def read(self):
        return False == self.GPIO.input(self.pinNumber)
