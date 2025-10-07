import time

# Load logger
logger_globals = {}
with open("engine/core/logger.py", "r") as f:
    exec(f.read(), logger_globals)
Logger = logger_globals["Logger"]
logger = Logger()

# Load timer
timer_globals = {}
with open("engine/core/timer.py", "r") as f:
    exec(f.read(), timer_globals)
Timer = timer_globals["Timer"]
timer = Timer()

# Load Vector2
vector2_globals = {}
with open("engine/math/vector2.py", "r") as f:
    exec(f.read(), vector2_globals)
Vector2 = vector2_globals["Vector2"]

# Load Vector3
vector3_globals = {}
with open("engine/math/vector3.py", "r") as f:
    exec(f.read(), vector3_globals)
Vector3 = vector3_globals["Vector3"]

# Load Rasterizer
rasterizer_globals = {}
with open("engine/graphics/rasterizer.py", "r") as f:
    exec(f.read(), rasterizer_globals)
Rasterizer = rasterizer_globals["Rasterizer"]

# Load Component
component_globals = {}
with open("engine/scene/component.py", "r") as f:
    exec(f.read(), component_globals)
Component = component_globals["Component"]

# Load Entity
entity_globals = {}
with open("engine/scene/entity.py", "r") as f:
    exec(f.read(), entity_globals)
Entity = entity_globals["Entity"]

# Load InputHandler
input_globals = {}
with open("engine/input/input_handler.py", "r") as f:
    exec(f.read(), input_globals)
InputHandler = input_globals["InputHandler"]

# Load UIRenderer
ui_globals = {}
with open("engine/ui/ui_renderer.py", "r") as f:
    exec(f.read(), ui_globals)
UIRenderer = ui_globals["UIRenderer"]

# Begin simulation
logger.info("VTXEngine Booting...")

# Input system
input_handler = InputHandler()
input_handler.simulate_key_press("W")

# UI system
ui = UIRenderer()
ui.add_element("Health: 100")
ui.add_element("Ammo: 30")
ui.add_element("Press [W] to move forward")

# Input component
class InputComponent(Component):
    def __init__(self, handler):
        super().__init__("InputComponent")
        self.handler = handler

    def update(self):
        key = self.handler.get_key()
        if key:
            logger.info(f"[Input] Key '{key}' was pressed")
            self.handler.clear()

# UI component
class UIComponent(Component):
    def __init__(self, renderer):
        super().__init__("UIComponent")
        self.renderer = renderer

    def update(self):
        self.renderer.render()
        self.renderer.clear()

# Create entity with input and UI
player = Entity("Player")
player.add_component(InputComponent(input_handler))
player.add_component(UIComponent(ui))

# Simulate frame
logger.info(f"Scene contains: {player}")
player.update()

logger.info("VTXEngine Shutdown.")
