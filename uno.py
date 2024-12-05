import serial
import time

arduino = serial.Serial('/dev/tty.usbmodem21201', 9600, timeout=1)
time.sleep(2)

def detect_number():
    return 4
number = 0
while number <= 9:
    # number = detect_number()
    if 0 <= number <= 9:
        arduino.write(str(number).encode())
        print(f"Sent number {number} to Arduino")
        time.sleep(1)
    else:
        print("Invalid number. Please enter a number between 0 and 9.")
    number += 1
