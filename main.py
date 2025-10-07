import time

# Load Logger
logger_globals = {}
with open("engine/core/logger.py", "r") as f:
    exec(f.read(), logger_globals)
Logger = logger_globals["Logger"]
logger = Logger()

# Load Timer
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
script_engine = ScriptEngine(logger)

# Load AssetManager
asset_globals = {}
with open("engine/assets/asset_manager.py", "r") as f:
    exec(f.read(), asset_globals)
AssetManager = asset_globals["AssetManager"]
assets = AssetManager()

# Load NetworkSimulator
network_globals = {}
with open("engine/network/network_simulator.py", "r") as f:
    exec(f.read(), network_globals)
NetworkSimulator = network_globals["NetworkSimulator"]
network = NetworkSimulator()

# Load EditorUI
editor_globals = {}
with open("engine/editor/editor_ui.py", "r") as f:
    exec(f.read(), editor_globals)
EditorUI = editor_globals["EditorUI"]
editor = EditorUI()

# Begin simulation
logger.info("VTXEngine Booting...")

# Create sample entity
player = Entity("Player")

# Add dummy components
class DummyComponent(Component):
    def __init__(self, name):
        super().__init__(name)

player.add_component(DummyComponent("Transform"))
player.add_component(DummyComponent("Renderer"))
player.add_component(DummyComponent("Collider"))

# Add entity to editor
editor.add_entity(player)

# Render editor UI
editor.render(logger)

logger.info("VTXEngine Shutdown.")
