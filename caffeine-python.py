import sys
import pyautogui
import time

kb_button = '.'
timeout = 2
if len(sys.argv) > 1:
    kb_button = sys.argv[1]


def no_lock(button):
    try:
        while True:
            pyautogui.press(button)
            time.sleep(timeout)

    except Exception as ex:
        print('no_lock | Error: ', ex)


def main():
    try:
        print('Windows Lock Prevention running...')
        print('Press Ctrl+C to stop')
        print(f"Key setup: {kb_button}  |  Timeout: {timeout} seconds\n\n")
        no_lock(kb_button)

    except Exception as ex:
        print('main | Error: ', ex)


if __name__ == "__main__":
    main()
