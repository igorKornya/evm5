from pynput import keyboard

def on_press(key):
    try:
        print(f'Клавиша нажата: {key.char}')
    except AttributeError:
        print(f'Специальная клавиша нажата: {key}')

def on_release(key):
    if key == keyboard.Key.esc:
        return False

with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
