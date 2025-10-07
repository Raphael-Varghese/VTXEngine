class Entity:
    def __init__(self, name="UnnamedEntity"):
        self.name = name
        self.components = []

    def add_component(self, component):
        self.components.append(component)

    def update(self):
        for comp in self.components:
            comp.update()

    def __repr__(self):
        return f"<Entity: {self.name}, Components: {len(self.components)}>"
