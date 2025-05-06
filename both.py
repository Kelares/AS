from gpiozero import Servo
from time import sleep

# Use GPIO17 (pin 11) — adjust if using another pin
servo_l = Servo(18)
servo_r = Servo(27)

try:
    while True:
#        print("Center")
 #       servo.mid()
  #      sleep(1)

        print("Right")
        servo_l.max()
        servo_r.min()
        sleep(5)

        print("Left")
        servo_l.min()
        servo_r.max()
        sleep(5)

except KeyboardInterrupt:
    print("Exiting...")
