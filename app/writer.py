import time

import pynput


class Writer:
    def __init__(self, input_text: str, start_delay: float = 2.5, keypress_delay: float = 0.01) -> None:
        self.input_text = input_text
        self.start_delay = start_delay
        self.keypress_delay = keypress_delay
        self.is_running_allowed = False
        self.interrupt = False
        self.clicked = False
        self.clicked_is_checked_on_run = True
        self.keyboard_controller = pynput.keyboard.Controller()

    def load_text(self, input_text: str):
        self.input_text = input_text

    def run(self) -> None:
        if self.is_running_allowed is False:
            return
        self.interrupt = False  # If from previous interrupt it stayed true
        
        time.sleep(self.start_delay)
        
        self.clicked = False
        
        if self.clicked_is_checked_on_run is True:
            while(self.clicked is False):
                time.sleep(0)
            time.sleep(0.5)
            
        
        
        
        for char in self.input_text:
            if self.interrupt is True:
                break
            time.sleep(self.keypress_delay)
            self.keyboard_controller.type(char)

    def enable_run(self) -> None:
        self.is_running_allowed = True

    def disable_run(self) -> None:
        self.is_running_allowed = False

    def interrupt_execution(self):
        self.interrupt = True
        
    def reset_interrupt(self):
        self.interrupt = False
    
    def enable_click_detection(self):
        self.clicked_is_checked_on_run = True
    
    def disable_click_detection(self):
        self.clicked_is_checked_on_run = False
        
    def click_detected(self):
        self.clicked = True