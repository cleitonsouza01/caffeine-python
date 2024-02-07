import threading
import time
import keyboard
import sys


# Function to print help menu
def print_help():
    print("""
Usage: python script.py [key] [interval] [suspend_duration]

Arguments:
  key              The key to simulate pressing. Default is 'a'.
  interval         Time in seconds between each simulated key press. Default is 5 seconds.
  suspend_duration Time in seconds to suspend simulation after pressing 'Esc' or 'Space'. Default is 20 seconds.

Example:
  python script.py b 5 20    Simulate pressing 'b' every 5 seconds, suspend for 20 seconds on 'Esc' or 'Space' press.

Press Ctrl+C to exit the program.

by Cleiton Souza
""")


# Check for help flag in arguments
if '?' in sys.argv or '/?' in sys.argv:
    print_help()
    sys.exit()

# Default values
simulate_interval = 5  # seconds
suspend_duration = 20  # seconds
simulated_key = 'a'  # default key to simulate

# Updating default values based on args if provided
if len(sys.argv) > 1:
    simulated_key = sys.argv[1]
if len(sys.argv) > 2:
    simulate_interval = int(sys.argv[2])
if len(sys.argv) > 3:
    suspend_duration = int(sys.argv[3])

# Flag to control suspension and program running
suspend = False
running = True


def simulate_key_press():
    global suspend, running
    while running:
        if not suspend:
            # Simulating specified key press
            keyboard.press_and_release(simulated_key)
            # print(f"Simulated key press '{simulated_key}'")
        time.sleep(simulate_interval)


def on_key_event(event):
    global suspend
    if event.name == 'esc' or event.name == 'space':
        suspend = True
        print(f"{event.name.capitalize()} key press detected, suspending simulation...")
        time.sleep(suspend_duration)
        print("Resuming simulation.")
        suspend = False


# Registering a function to handle Ctrl+C
def handle_exit():
    global running
    running = False
    print("Exiting program...")
    sys.exit()


keyboard.add_hotkey('ctrl+c', handle_exit)

# Setting up the key press listener specifically for 'Esc' and 'Space'
keyboard.on_press_key('esc', on_key_event)
keyboard.on_press_key('space', on_key_event)

# Starting the simulate key press thread
thread = threading.Thread(target=simulate_key_press)
thread.start()

print("*** Caffeine Python - Prevent Windows lock screen ***")
print(f"Press 'Esc' or 'Space' to suspend simulated key pressing for {suspend_duration} seconds.")
print("Press Ctrl+C to exit.")
print(f"Simulating key press '{simulated_key}' every {simulate_interval} seconds, press 'Esc' or 'Space' to suspend for {suspend_duration} seconds.")

# Keep the script running until Ctrl+C is pressed
while running:
    time.sleep(0.1)

thread.join()
