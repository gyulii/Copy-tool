"""Identify pressed key and save them."""
from pynput import keyboard
import collections



class KeyRegister:
    def __init__(self, on_press_fn=None, on_release_fn=None, default_key_list = None,) -> None:
        
        self.listener = keyboard.Listener(
            on_press=on_press_fn,
            on_release=on_release_fn)
        self.listener.start()
        
        
        if default_key_list is not None:
            self.length = len(default_key_list)
            self.registered_keys = default_key_list
        else:
            self.length = 4
            self.registered_keys = []
            
        self.collected_input_buffer = collections.deque(maxlen=self.length) # Input detect
    
    def register_key(self , key : chr):
        if len(self.registered_keys) < self.length:
            self.registered_keys.append(key)
            return True
        else:
            return False
    
    def check_new_input_key(self, key : chr) -> bool:
        self.collected_input_buffer.append(key)
        if(list(self.collected_input_buffer) == self.registered_keys):
            return True
        return False
        
    
    def get_registered_keys(self):
        return self.registered_keys

    def reset_registered_keys(self):
        self.registered_keys.clear()
    
    """Functions from pynput, example usage:
    
        KeyReg = KeyRegister()
    listener = keyboard.Listener(
        on_press=KeyReg.on_press,
        on_release=KeyReg.on_release)
    listener.start()
    listener.join()
    """


def main():
    keyreg = KeyRegister()
    listener = keyboard.Listener(
        on_press=keyreg.on_press,
        on_release=keyreg.on_release)
    listener.start()
    listener.join()
    

if __name__ == "__main__":
    main()



