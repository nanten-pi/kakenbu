import RPi.GPIO as GPIO

STATE_STOP = 0
STATE_ON = 1

class Motor:

    def __init__(self, pina, pinb, pwmpin):
        self.state = STATE_STOP
        self.pina = pina
        self.pinb = pinb
        self.pwmpin = pwmpin
        self.duty = 0

        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)

        GPIO.setup(self.pina, GPIO.OUT)
        GPIO.output(self.pina, GPIO.LOW)

        GPIO.setup(self.pinb, GPIO.OUT)
        GPIO.output(self.pinb, GPIO.LOW)

        GPIO.setup(self.pwmpin, GPIO.OUT)
        GPIO.output(self.pwmpin, GPIO.LOW)

        self.pwm = GPIO.PWM(self.pwmpin, 80)
        return

    def setspeed(self,duty):
        self.duty = duty
        if self.state == STATE_ON:
            self.pwm.ChangeDutyCycle(self.duty)
        return self.state

    def accelon(self,back = False):
        if back == False:
            GPIO.output(self.pina, GPIO.HIGH)
            GPIO.output(self.pinb, GPIO.LOW)
        else:
            GPIO.output(self.pina, GPIO.LOW)
            GPIO.output(self.pinb, GPIO.HIGH)

        if self.state == STATE_STOP:
            self.pwm.start(self.duty)

        self.state = STATE_ON
        return self.state

    def acceloff(self):
        GPIO.output(self.pina, GPIO.LOW)
        GPIO.output(self.pinb, GPIO.LOW)
        self.pwm.stop()
        self.state = STATE_STOP
        return self.state

    def brakeon(self):
        GPIO.output(self.pina, GPIO.HIGH)
        GPIO.output(self.pinb, GPIO.HIGH)
        self.pwm.stop()
        GPIO.output(self.pina, GPIO.LOW)
        GPIO.output(self.pinb, GPIO.LOW)
        self.state = STATE_STOP
        return self.state
