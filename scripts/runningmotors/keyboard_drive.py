# RUN ON LAPTOP / COMPUTER WITH KEYBOARD (NOT ON PICO)
import serial
import time
from pynput import keyboard

# CHANGE THIS TO YOUR PICO COM PORT
PORT = "COM5"

BAUD = 115200

ser = serial.Serial(PORT, BAUD, timeout=1)

time.sleep(2)

print("Connected to Pico")
print()
print("Controls:")
print("W = Forward")
print("S = Backward")
print("A = Left")
print("D = Right")
print("Release key = Stop")
print("ESC = Exit")


current_key = None


def send(command):
    ser.write(command.encode())


def on_press(key):
    global current_key

    try:
        char = key.char.lower()

        # Prevent sending the same command hundreds
        # of times from keyboard repeat
        if char == current_key:
            return

        if char == 'w':
            send('w')
            print("FORWARD")

        elif char == 's':
            send('s')
            print("BACKWARD")

        elif char == 'a':
            send('a')
            print("LEFT")

        elif char == 'd':
            send('d')
            print("RIGHT")

        else:
            return

        current_key = char

    except AttributeError:
        pass


def on_release(key):
    global current_key

    if key == keyboard.Key.esc:
        send('x')
        ser.close()
        print("Stopped")
        return False

    try:
        char = key.char.lower()

        if char == current_key:
            send('x')
            current_key = None
            print("STOP")

    except AttributeError:
        pass


with keyboard.Listener(
    on_press=on_press,
    on_release=on_release
) as listener:

    listener.join()
