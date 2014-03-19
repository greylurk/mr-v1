import RPi.GPIO as GPIO

class FanController:
    """ Controller for the Fans """
    ONE = 4
    TWO = 17
    THREE = 18
    FOUR = 22

    ON = GPIO.LOW
    OFF = GPIO.HIGH
    
    def __init__(self):
        GPIO.setmode(GPIO.BCM)

        GPIO.setup(4,GPIO.OUT,initial=GPIO.LOW)
        GPIO.setup(17,GPIO.OUT,initial=GPIO.LOW)
        GPIO.setup(18,GPIO.OUT,initial=GPIO.LOW)
        GPIO.setup(22,GPIO.OUT,initial=GPIO.LOW)

    def open(self):
        self.__enter__()

    def close(self):
        self.__exit__()

    def __enter__(self):
        return self

    def set_fan(self, fan_number, state):
	GPIO.output(fan_number, state)

    def fan_on(self, fan_number):
        GPIO.output(fan_number, self.ON)

    def fan_off(self, fan_number):
        GPIO.output(fan_number, self.OFF)

    def __exit__(self, type, value, traceback):
        GPIO.cleanup()

