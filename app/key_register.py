"""Identify pressed key and save them."""
from pynput import keyboard
import collections



class KeyRegister:
    def __init__(self, default_key_list = None) -> None:
        
        
        if default_key_list is not None:
            self.length = len(default_key_list)
            self.saved_keys = default_key_list
        else:
            self.length = 4
            self.saved_keys = []
            
        self.collected_input_buffer = collections.deque(maxlen=self.length) # Input detect
    
    def register_key(self , key : chr):
        if len(self.saved_keys) < self.length:
            self.saved_keys.append(key)
            return True
        else:
            return False
    
    def get_registered_keys(self):
        return self.saved_keys

    def reset_registered_keys(self):
        self.saved_keys.clear()
    
    """Functions from pynput, example usage:
    
        KeyReg = KeyRegister()
    listener = keyboard.Listener(
        on_press=KeyReg.on_press,
        on_release=KeyReg.on_release)
    listener.start()
    listener.join()
    """
    def on_press(self, key):
        print(key)
        
    def on_release(self, key):
        if key == keyboard.Key.esc:
    # Stop listener
            return False


def main():
    keyreg = KeyRegister()
    listener = keyboard.Listener(
        on_press=keyreg.on_press,
        on_release=keyreg.on_release)
    listener.start()
    listener.join()
    

if __name__ == "__main__":
    main()



