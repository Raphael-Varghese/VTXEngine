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

# Load AudioPlayer
audio_globals = {}
with open("engine/audio/audio_player.py", "r") as f:
    exec(f.read(), audio_globals)
AudioPlayer = audio_globals["AudioPlayer"]

# Load ScriptEngine
script_globals = {}
with open("engine/scripting/script_engine.py", "r") as f:
    exec(f.read(), script_globals)
ScriptEngine = script_globals["ScriptEngine"]

# Begin simulation
logger.info("VTXEngine Booting...")

# Scripting system
script_engine = ScriptEngine(logger)

# Scripting component
class ScriptComponent(Component):
    def __init__(self, engine, script_text):
        super().__init__("ScriptComponent")
        self.engine = engine
        self.script_text = script_text

    def update(self):
        self.engine.run_script(self.script_text, logger)

# Create entity with script
script = """
x = 5
y = 10
logger.info(f'[Script] x + y = {x + y}')
"""

npc = Entity("NPC")
npc.add_component(ScriptComponent(script_engine, script))

# Simulate frame
logger.info(f"Scene contains: {npc}")
npc.update()

logger.info("VTXEngine Shutdown.")
