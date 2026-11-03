"""Dual servo control with gpiozero and lgpio on Raspberry Pi 3B.

GPIO17: servo 1 signal; GPIO18: servo 2 signal.
Servo power must come from a separately verified supply with common GND.
Do not run if any supply/module has overheated or wiring is unverified.
"""
from time import sleep
from gpiozero import Servo
from gpiozero.pins.lgpio import LGPIOFactory

SERVO1_PIN = 17
SERVO2_PIN = 18
MIN_PULSE = 0.001
MAX_PULSE = 0.002
FRAME_WIDTH = 0.020


def duty_to_value(duty):
    """Convert a 5–10% duty cycle at 50 Hz to gpiozero's [-1, 1]."""
    return (duty - 7.5) / 2.5


def main():
    factory = LGPIOFactory(chip=0)
    servo1 = None
    servo2 = None
    try:
        servo1 = Servo(SERVO1_PIN, initial_value=None,
                       min_pulse_width=MIN_PULSE,
                       max_pulse_width=MAX_PULSE,
                       frame_width=FRAME_WIDTH,
                       pin_factory=factory)
        servo2 = Servo(SERVO2_PIN, initial_value=None,
                       min_pulse_width=MIN_PULSE,
                       max_pulse_width=MAX_PULSE,
                       frame_width=FRAME_WIDTH,
                       pin_factory=factory)

        print("Dual Servo Control — GPIO17 and GPIO18")
        print("Enter two duty cycles from 5.0 to 10.0 (e.g. 6.0 9.0); q to quit")
        while True:
            command = input("Servo1 Servo2 > ").strip()
            if command.lower() == "q":
                break
            try:
                parts = command.split()
                if len(parts) != 2:
                    print("Enter exactly two values, e.g. 6.0 9.0")
                    continue
                duty1, duty2 = (float(x) for x in parts)
                if not (5.0 <= duty1 <= 10.0 and 5.0 <= duty2 <= 10.0):
                    print("Both values must be between 5.0 and 10.0")
                    continue

                servo1.value = duty_to_value(duty1)
                servo2.value = duty_to_value(duty2)
                print(f"GPIO17: {duty1:.1f}%, GPIO18: {duty2:.1f}%")
                sleep(0.7)
                servo1.detach()
                servo2.detach()
            except ValueError:
                print("Please enter two numbers, e.g. 6.0 9.0")
    except (KeyboardInterrupt, EOFError):
        print("\nStopped")
    finally:
        if servo1 is not None:
            servo1.close()
        if servo2 is not None:
            servo2.close()
        factory.close()
        print("GPIO cleanup completed")


if __name__ == "__main__":
    main()
