from machine import Pin, PWM
import time

motor1_1 = Pin(18, Pin.OUT)
motor1_2 = Pin(19, Pin.OUT)

motor2_1 = Pin(20, Pin.OUT)
motor2_2 = Pin(21, Pin.OUT)

motor3_1 = Pin(6, Pin.OUT)
motor3_2 = Pin(7, Pin.OUT)

motor4_1 = Pin(8, Pin.OUT)
motor4_2 = Pin(9, Pin.OUT)

# PWM objects
pwm_motor1_1 = PWM(motor1_1)
pwm_motor1_2 = PWM(motor1_2)

pwm_motor2_1 = PWM(motor2_1)
pwm_motor2_2 = PWM(motor2_2)

pwm_motor3_1 = PWM(motor3_1)
pwm_motor3_2 = PWM(motor3_2)

pwm_motor4_1 = PWM(motor4_1)
pwm_motor4_2 = PWM(motor4_2)

# Set frequency
pwm_motor1_1.freq(1000)
pwm_motor1_2.freq(1000)

pwm_motor2_1.freq(1000)
pwm_motor2_2.freq(1000)

pwm_motor3_1.freq(1000)
pwm_motor3_2.freq(1000)

pwm_motor4_1.freq(1000)
pwm_motor4_2.freq(1000)

# Function to set motor speed and direction
def set_motor(speed,motor_num):
    if speed > 0:
        motor1_1.on()
        pwm_motor1_1.duty_u16(int(speed * 65535))
    elif speed < 0:
        motor1_1.off()
        pwm_motor1_1.duty_u16(int(-speed * 65535))
    else:
        motor1_1.off()
        pwm_motor1_1.duty_u16(0)

def forward(speed):
    motor1_1.on()
    motor2_1.on()
    motor3_1.on()
    motor4_1.on()

    pwm_motor1_1.duty_u16(int(speed * 65535))
    pwm_motor2_1.duty_u16(int(speed * 65535))
    pwm_motor3_1.duty_u16(int(speed * 65535))
    pwm_motor4_1.duty_u16(int(speed * 65535))

    time.sleep(4)

    motor1_1.off()
    motor2_1.off()
    motor3_1.off()
    motor4_1.off()

# Test the motor
try:
    while True:
        forward(0.25)
except KeyboardInterrupt:
    set_motor(0)  # Ensure motor is stopped on exit 
