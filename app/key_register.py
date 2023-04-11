"""Identify pressed key and save them."""
from pynput import keyboard




class KeyRegister:
    def __init__(self, length: int = 3) -> None:
        self.length = length
    
    def set_register_keys(length: int = 3):
        pass
    
    def get_register_keys():
        pass
        
        
from pynput import keyboard

def on_press(key):
    try:
        print('alphanumeric key {0} pressed'.format(
            key.char))
    except AttributeError:
        print('special key {0} pressed'.format(
            key))

def on_release(key):
    print('{0} released'.format(
        key))
    if key == keyboard.Key.esc:
        # Stop listener
        return False


listener = keyboard.Listener(
    on_press=on_press,
    on_release=on_release)
listener.start()
listener.join()