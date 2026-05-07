from machine import Pin, PWM
import time

# Initialize motor pins
motor1 = Pin(18, Pin.OUT)
motor2 = Pin(20, Pin.OUT)
motor3 = Pin(6, Pin.OUT)
motor4 = Pin(8, Pin.OUT)

pwm1 = PWM(Pin(18))
pwm1.freq(1000)
pwm2 = PWM(Pin(20))
pwm2.freq(1000)
pwm3 = PWM(Pin(6))
pwm3.freq(1000)
pwm4 = PWM(Pin(8))
pwm4.freq(1000)
# Function to set motor speed and direction
def set_motor(speed):
    if speed > 0:
        motor1.on()
        pwm1.duty_u16(int(speed * 65535))
        pwm2.duty_u16(int(speed * 65535))
        pwm3.duty_u16(int(speed * 65535))
        pwm4.duty_u16(int(speed * 65535))   
    elif speed < 0:
        motor1.off()
        pwm1.duty_u16(int(-speed * 65535))
        pwm2.duty_u16(int(-speed * 65535))
        pwm3.duty_u16(int(-speed * 65535))
        pwm4.duty_u16(int(-speed * 65535))
    else:
        motor1.off()
        pwm1.duty_u16(0)
        pwm2.duty_u16(0)
        pwm3.duty_u16(0)
        pwm4.duty_u16(0)


# Test the motor
try:
    while True:
        set_motor(0.1)  # Move forward at half speed
        time.sleep(2)
        set_motor(-0.1)  # Move backward at half speed
        time.sleep(2)
        set_motor(0)  # Stop the motor
        time.sleep(2)
        print("Motor test cycle complete")
except Exception as e:
    print(f"An error occurred: {e}")
except KeyboardInterrupt:
    set_motor(0)  # Ensure motor is stopped on exit 
