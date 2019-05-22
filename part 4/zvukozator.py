# 1. open a file
# 2. read all data as binary
# 3. generate sound somehow while reading
import sys
import winsound
from time import sleep

# First argument can be used as file name, otherwise play this file
file_name = sys.argv[1] if len(sys.argv) > 1 else __file__

step = 11600/256  # HZ per byte value
beep_offset = 400  # beep frequency offset must be > 37
beep_duration = 200  # milliseconds


def main():
    """ Currently works only on windows """
    with open(file_name, "rb") as file:
        # Skip some of the starting bytes
        byte = file.read(500)
        while byte != b"":
            # Keep reading every byte
            byte = file.read(1)
            # Calculate the frequency we will be playing
            hz = byte[0] * step
            # Show every value on one continuous line
            print(hz, end=' ', flush=True)
            if hz == 0:  # Keep silent when value is zero
                sleep(beep_duration/1000)
            else:  # Play the current byte
                winsound.Beep(int(hz) + beep_offset, beep_duration)


if __name__ == "__main__":  # Only if our file is executed directly
    print(f"Playing '{file_name}'")

    # Play two beeps to acknowledge start
    winsound.Beep(440, 300)
    sleep(0.1)
    winsound.Beep(440, 800)

    try:
        main()
    except KeyboardInterrupt:  # Intercept Ctrl+C
        pass
    finally:
        # Aknowledge end with a long beep
        winsound.Beep(440, 1000)

