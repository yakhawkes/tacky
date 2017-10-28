class Motor(object):
    """Motor controller for a setper motor"""
    def __init__(self):
        import RPi.GPIO as GPIO
        self.GPIO = GPIO
        self.GPIO.setmode(GPIO.BCM)
        self.stepperPins = [7, 8, 9, 10]
        self.step = 0
        for pinNumber in self.stepperPins:
            self.GPIO.setup(pinNumber, self.GPIO.OUT)
            self.GPIO.output(pinNumber, False)

        self.sequence = [[1, 0, 0, 1],
                    [1, 0, 0, 0],
                    [1, 1, 0, 0],
                    [0, 1, 0, 0],
                    [0, 1, 1, 0],
                    [0, 0, 1, 0],
                    [0, 0, 1, 1],
                    [0, 0, 0, 1]]

    def advance(self):  # Start main loop
        #for each step
        if self.step == len(self.sequence):
            self.step = 0

        for pin in range(0, 4):
            pinNumber = self.stepperPins[pin]
            if self.sequence[self.step][pin] != 0:
                self.GPIO.output(pinNumber, True)
            else:
                self.GPIO.output(pinNumber, False)

        self.step+=1
