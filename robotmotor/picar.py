from ta7291p import Motor
import time

FRONT_LEFT_WHEEL_PIN_A = 17
FRONT_LEFT_WHEEL_PIN_B = 4
FRONT_LEFT_WHEEL_PWMPIN = 27

FRONT_RIGHT_WHEEL_PIN_A = 18
FRONT_RIGHT_WHEEL_PIN_B = 23
FRONT_RIGHT_WHEEL_PWMPIN = 24

REAR_LEFT_WHEEL_PIN_A = 6
REAR_LEFT_WHEEL_PIN_B = 13
REAR_LEFT_WHEEL_PWMPIN = 19

REAR_RIGHT_WHEEL_PIN_A = 20
REAR_RIGHT_WHEEL_PIN_B = 12
REAR_RIGHT_WHEEL_PWMPIN = 21

class PiCar():

    def __init__(self):
        self._motors = {}
        self._motors["front_left"] = Motor(FRONT_LEFT_WHEEL_PIN_A, FRONT_LEFT_WHEEL_PIN_B, FRONT_LEFT_WHEEL_PWMPIN)
        self._motors["front_right"] = Motor(FRONT_RIGHT_WHEEL_PIN_A, FRONT_RIGHT_WHEEL_PIN_B, FRONT_RIGHT_WHEEL_PWMPIN)
        self._motors["rear_left"] = Motor(REAR_LEFT_WHEEL_PIN_A, REAR_LEFT_WHEEL_PIN_B, REAR_LEFT_WHEEL_PWMPIN)
        self._motors["rear_right"] = Motor(REAR_RIGHT_WHEEL_PIN_A, REAR_RIGHT_WHEEL_PIN_B, REAR_RIGHT_WHEEL_PWMPIN)

        self._speed = 0
        self.state = 0
        self.set_speed(100)
        return


    def set_speed(self, speed):
        self._speed = speed
        for key in self._motors:
            self._motors[key].setspeed(speed)
        return


    def turn_left(self):
        print("turn_left : run")
        for key in self._motors:
            if "rear" in key:
                self._motors[key].setspeed(int(self._speed * 0.7))
            else:
                self._motors[key].setspeed(self._speed)

            if "left" in key:
                self._motors[key].accelon(back=True)
            if "right" in key:
                self._motors[key].accelon()
        print("turn_left : over")
        return


    def turn_right(self):
        print("turn_right : run")
        for key in self._motors:
            if "rear" in key:
                self._motors[key].setspeed(int(self._speed * 0.7))
            else:
                self._motors[key].setspeed(self._speed)

            if "left" in key:
                self._motors[key].accelon()
            if "right" in key:
                self._motors[key].accelon(back=True)
        print("turn_right : over")
        return


    def forward(self):
        print("forward : run")
        for key in self._motors:
            self._motors[key].setspeed(self._speed)
            self._motors[key].accelon()
        print("forward : over")
        return


    def back(self):
        print("back : run")
        for key in self._motors:
            self._motors[key].setspeed(self._speed)
            self._motors[key].accelon(back=True)
        print("back : over")
        return


    def brake(self):
        print("brake : run")
        for key in self._motors:
            self._motors[key].brakeon()
        print("brake : over")
        return


    def acceloff(self):
        print("acceloff : run")
        for key in self._motors:
            self._motors[key].acceloff()
        print("acceloff : over")
        return


    def debug_proc(self):
        time.sleep(5)
        # Check for each tire
        # for key in self._motors:
        #     print(key)
        #     time.sleep(1)
        #     self._motors[key].setspeed(100)
        #     self._motors[key].accelon()
        #     time.sleep(1)
        #     self._motors[key].accelon(back=True)
        #     time.sleep(1)
        #     self._motors[key].acceloff()

        # Check : operation function
        self.forward()
        time.sleep(1)
        self.brake()
        time.sleep(1)
        self.turn_left()
        time.sleep(1)
        self.turn_right()
        time.sleep(1)
        self.acceloff()
        time.sleep(1)
        self.back()
        time.sleep(1)
        self.acceloff()



if __name__ == '__main__':
    pi_car = PiCar()
    pi_car.debug_proc()
