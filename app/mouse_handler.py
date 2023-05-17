from pynput import mouse


class MouseHandler:
    def __init__(self, on_move_fn=None, on_click_fn=None, on_scroll_fn=None) -> None:
        listener_mouse = mouse.Listener(on_move=on_move_fn, on_click=on_click_fn, on_scroll=on_scroll_fn)
        listener_mouse.start()
