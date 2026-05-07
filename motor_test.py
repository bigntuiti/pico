from machine import Pin, PWM
import time

# Initialize motor pins
motor1 = Pin(18, Pin.OUT)
pwm = PWM(Pin(18))
pwm.freq(100)
# Function to set motor speed and direction
def set_motor(speed):
    if speed > 0:
        motor1.on()
        pwm.duty_u16(int(speed * 65535))
    elif speed < 0:
        motor1.off()
        pwm.duty_u16(int(-speed * 65535))
    else:
        motor1.off()
        pwm.duty_u16(0)
# Test the motor
try:
    while True:
        set_motor(0.5)  # Move forward at half speed
        time.sleep(2)
        set_motor(-0.5)  # Move backward at half speed
        time.sleep(2)
        set_motor(0)  # Stop the motor
        time.sleep(2)
except KeyboardInterrupt:
    set_motor(0)  # Ensure motor is stopped on exit 
