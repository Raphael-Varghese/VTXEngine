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

# Begin simulation
logger.info("VTXEngine Booting...")

# Create a custom component
class PrintComponent(Component):
    def __init__(self, message):
        super().__init__("PrintComponent")
        self.message = message

    def update(self):
        logger.info(f"[Component] {self.message}")

# Create an entity and attach components
player = Entity("Player")
player.add_component(PrintComponent("Player is updating..."))
player.add_component(PrintComponent("Player is rendering..."))

# Simulate scene update
logger.info(f"Scene contains: {player}")
player.update()

logger.info("VTXEngine Shutdown.")
