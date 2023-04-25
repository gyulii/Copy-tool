"""Identify pressed key and save them."""
import collections

from pynput import keyboard


class KeyRegister:
    def __init__(self, on_press_fn=None, on_release_fn=None) -> None:
        
        self.listener = keyboard.Listener(
            on_press=on_press_fn,
            on_release=on_release_fn)
        self.listener.start()
        
        self.collected_input_buffer = collections.deque() # Input detect

    def check_queue_to_keycombination(self, registered_key_combination: list) -> bool:
        queue_list = list(self.collected_input_buffer)
        if(len(registered_key_combination) == 0):
            return False
        
        if(len(registered_key_combination) < len(queue_list)):
            # Cut the first n-th element (oldest items)
            if(queue_list[ len(queue_list) - len(registered_key_combination):] == registered_key_combination):
                return True   
        elif(queue_list == registered_key_combination):
                return True
        return False
    
    def add_new_input_key_to_queue(self , key : chr):
        self.collected_input_buffer.append(key)
        
    def get_queue(self):
        return list(self.collected_input_buffer)

    def reset_queue(self):
        self.collected_input_buffer.clear()

def main():
 
    keyreg = KeyRegister()
    listener = keyboard.Listener(
        on_press=keyreg.on_press,
        on_release=keyreg.on_release)
    listener.start()
    listener.join()
    

if __name__ == "__main__":
    main()



