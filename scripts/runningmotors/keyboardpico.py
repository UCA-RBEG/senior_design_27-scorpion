# RUN AS main.py ON PICO
from machine import Pin, PWM
import sys

# =========================
# MOTOR SETUP
# =========================

# Motor 1
pwm1 = PWM(Pin(15))
pwm1.freq(1000)

in1 = Pin(16, Pin.OUT)
in2 = Pin(17, Pin.OUT)

# Motor 2
pwm2 = PWM(Pin(20))
pwm2.freq(1000)

in3 = Pin(19, Pin.OUT)
in4 = Pin(18, Pin.OUT)

# Start stopped
pwm1.duty_u16(0)
pwm2.duty_u16(0)


# =========================
# MOTOR FUNCTIONS
# =========================

def motor1(speed):
    """
    speed: -1.0 to 1.0
    """

    speed = max(-1.0, min(1.0, speed))

    if speed > 0:
        in1.off()
        in2.on()

    elif speed < 0:
        in1.on()
        in2.off()

    else:
        in1.off()
        in2.off()

    pwm1.duty_u16(int(abs(speed) * 65535))


def motor2(speed):
    """
    speed: -1.0 to 1.0
    """

    speed = max(-1.0, min(1.0, speed))

    if speed > 0:
        in3.off()
        in4.on()

    elif speed < 0:
        in3.on()
        in4.off()

    else:
        in3.off()
        in4.off()

    pwm2.duty_u16(int(abs(speed) * 65535))


def drive(left, right):
    motor1(left)
    motor2(right)


def stop():
    drive(0, 0)


# =========================
# KEYBOARD COMMAND LOOP
# =========================

SPEED = 0.40

print("Robot motor controller ready")
print("W = Forward")
print("S = Backward")
print("A = Left")
print("D = Right")
print("X = Stop")

while True:

    command = sys.stdin.read(1)

    if command == 'w':
        drive(SPEED, SPEED)

    elif command == 's':
        drive(-SPEED, -SPEED)

    elif command == 'a':
        drive(-SPEED, SPEED)

    elif command == 'd':
        drive(SPEED, -SPEED)

    elif command == 'x':
        stop()
