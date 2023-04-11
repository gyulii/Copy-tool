import time

import pynput


class Writer:
    def __init__(self, input_text: str, start_delay: float = 2.5, keypress_delay: float = 0.01) -> None:
        self.input_text = input_text
        self.start_delay = start_delay
        self.keypress_delay = keypress_delay
        self._is_running_allowed = False
        self.keyboard_controller = pynput.keyboard.Controller()

    def run(self) -> None:
        time.sleep(self.start_delay)
        for char in self.input_text:
            if self.is_running_allowed is False:
                break
            time.sleep(self.keypress_delay)
            self.keyboard_controller.type(char)

    def enable_run(self) -> None:
        self.is_running_allowed = True

    def disable_run(self) -> None:
        self.is_running_allowed = False
