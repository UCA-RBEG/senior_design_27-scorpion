# RUN ON LAPTOP / SSH TO PI (NOT ON PICO)
import serial
import sys
import termios
import tty
import select
import time

PORT = "/dev/ttyACM0"
BAUD = 115200

# If no repeated movement key arrives within this time,
# automatically stop the robot.
DEADMAN_TIMEOUT = 0.25

ser = serial.Serial(PORT, BAUD, timeout=0.1)

time.sleep(2)

print()
print("ROBOT TELEOP")
print("----------------")
print("W = Forward")
print("S = Backward")
print("A = Left")
print("D = Right")
print("SPACE = Stop")
print("Q = Quit")
print()
print("Hold a movement key to drive.")
print("Releasing it automatically stops the robot.")
print()


old_settings = termios.tcgetattr(sys.stdin)

last_command_time = 0
moving = False

try:

    tty.setcbreak(sys.stdin.fileno())

    while True:

        # Check whether a keyboard character is available
        readable, _, _ = select.select(
            [sys.stdin],
            [],
            [],
            0.02
        )

        if readable:

            key = sys.stdin.read(1).lower()

            if key == "w":
                ser.write(b"w")
                last_command_time = time.monotonic()
                moving = True

            elif key == "s":
                ser.write(b"s")
                last_command_time = time.monotonic()
                moving = True

            elif key == "a":
                ser.write(b"a")
                last_command_time = time.monotonic()
                moving = True

            elif key == "d":
                ser.write(b"d")
                last_command_time = time.monotonic()
                moving = True

            elif key == " ":
                ser.write(b"x")
                moving = False
                print("\rSTOP        ", end="", flush=True)

            elif key == "q":
                ser.write(b"x")
                print("\nRobot stopped.")
                break

        # DEADMAN SWITCH
        #
        # If movement commands stop arriving,
        # stop the motors automatically.
        if moving:

            if time.monotonic() - last_command_time > DEADMAN_TIMEOUT:

                ser.write(b"x")
                moving = False

finally:

    # Always attempt to stop robot when program exits
    ser.write(b"x")

    termios.tcsetattr(
        sys.stdin,
        termios.TCSADRAIN,
        old_settings
    )

    ser.close()

    print("Serial connection closed.")
) as listener:

    listener.join()
