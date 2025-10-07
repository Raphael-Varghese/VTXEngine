class UIRenderer:
    def __init__(self):
        self.elements = []

    def add_element(self, text):
        self.elements.append(text)

    def render(self):
        print("\n--- UI ---")
        for element in self.elements:
            print(f"[UI] {element}")
        print("----------\n")

    def clear(self):
        self.elements = []
