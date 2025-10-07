class Component:
    def __init__(self, name="UnnamedComponent"):
        self.name = name

    def update(self):
        pass  # Override in subclasses

    def __repr__(self):
        return f"<Component: {self.name}>"
