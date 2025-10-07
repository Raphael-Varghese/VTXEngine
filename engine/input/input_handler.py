class InputHandler:
    def __init__(self):
        self.last_key = None

    def simulate_key_press(self, key):
        self.last_key = key

    def get_key(self):
        return self.last_key

    def clear(self):
        self.last_key = None
