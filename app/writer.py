import time

import pynput


class Writer:
    mutex = False

    def __init__(self, input_text: str, start_delay: float = 0.3, keypress_delay: float = 0.01) -> None:
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
        if self.is_running_allowed is False or self.is_mutex_locked():
            return
        self.interrupt = False  # If from previous interrupt it stayed true
        self.lock_mutex()

        self.clicked = False

        if self.clicked_is_checked_on_run is True:
            while self.clicked is False:
                time.sleep(0)  # Waiting for click
            time.sleep(0.5)

        # Fixes the bug when the task is started and it is waiting for click but the module is disabled in the meanwhile
        if self.is_running_allowed is False:
            return

        time.sleep(self.start_delay)

        for char in self.input_text:
            if self.interrupt is True:
                break
            time.sleep(self.keypress_delay)
            self.keyboard_controller.type(char)

        self.unlock_mutex()

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

    @classmethod
    def lock_mutex(cls):
        cls.mutex = True

    @classmethod
    def unlock_mutex(cls):
        cls.mutex = False

    @classmethod
    def is_mutex_locked(cls):
        if cls.mutex is True:
            return True
        else:
            return False
