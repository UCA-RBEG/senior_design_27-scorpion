from machine import Pin, PWM
from time import sleep

# SETUP
pwm1 = PWM(Pin(15))
pwm1.freq(1000)
pwm2 = PWM(Pin(20))
pwm2.freq(1000)

in1 = Pin(16, Pin.OUT)
in2 = Pin(17, Pin.OUT)
in3 = Pin(19, Pin.OUT)
in4 = Pin(18, Pin.OUT)

#stby = Pin(12, Pin.OUT)
#stby.off()

# LOOP
print("motor driver enabled")
in1.off()
in2.on()
in3.off()
in4.on()
pwm1.duty_u16(50_000)
pwm2.duty_u16(50_000)
print("forward")

sleep(2)
pwm1.duty_u16(0)
pwm2.duty_u16(0)
print("stop")

sleep(1)
in1.on()
in2.off()
in3.on()
in4.off()
pwm1.duty_u16(50_000)
pwm2.duty_u16(50_000)
print("backward")

sleep(2)
pwm1.duty_u16(0)
pwm2.duty_u16(0)
print("stop")

sleep(1)	
print("motor driver disabled")
