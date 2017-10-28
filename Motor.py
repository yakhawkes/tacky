class Motor(object):
    """Motor controller for a setper motor"""
    def __init__(self):
        import time
        import RPi.GPIO as GPIO
        self.time = time
        self.GPIO = GPIO
        self.GPIO.setmode(GPIO.BCM)
        self.stepperPins = [7, 8, 9, 10]
        self.speed = 1
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
        self.stepCount = len(self.sequence)

    def start(self, speed=1, direction=1):  # Start main loop
        self.speed = speed
        stepCounter = 0
        sleep_time =0.1 / float(speed)
        while True:
            for pin in range(0, 4):
                pinNumber = self.stepperPins[pin]
                if self.sequence[stepCounter][pin] != 0:
                    self.GPIO.output(pinNumber, True)
                else:
                    self.GPIO.output(pinNumber, False)


            stepCounter += direction

            # If we reach the end of the sequenceuence
            # start again
            if (stepCounter >= self.stepCount):
                stepCounter = 0
            if (stepCounter < 0):
                stepCounter = self.stepCount + direction

            self.time.sleep(sleep_time)

    def goFaster():
        self.speed += 1

    def slowDown():
        if speed>0:
            self.speed -= 1

    def reverse():
        self.speed = self.direction * -1
