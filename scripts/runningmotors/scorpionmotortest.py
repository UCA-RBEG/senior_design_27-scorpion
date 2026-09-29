from machine import Pin, PWM
from time import sleep

# LEFT MOTOR
left_pwm = PWM(Pin(15))
left_pwm.freq(1000)

left_in1 = Pin(16, Pin.OUT)
left_in2 = Pin(17, Pin.OUT)

# RIGHT MOTOR
right_pwm = PWM(Pin(20))
right_pwm.freq(1000)

right_in1 = Pin(19, Pin.OUT)
right_in2 = Pin(18, Pin.OUT)


def set_motor(in1, in2, pwm, speed):
    # speed: -1.0 to +1.0

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

    duty = int(abs(speed) * 65535)
    pwm.duty_u16(duty)


def drive(left_speed, right_speed):
    set_motor(
        left_in1,
        left_in2,
        left_pwm,
        left_speed
    )

    set_motor(
        right_in1,
        right_in2,
        right_pwm,
        right_speed
    )


def stop():
    drive(0, 0)


# TEST

drive(0.7, 0.7)
sleep(2)

stop()
sleep(1)

drive(-0.7, -0.7)
sleep(2)

stop()
