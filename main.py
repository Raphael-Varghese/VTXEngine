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

# Begin simulation
logger.info("VTXEngine Booting...")

# Audio system
audio = AudioPlayer()

# Audio component
class AudioComponent(Component):
    def __init__(self, player):
        super().__init__("AudioComponent")
        self.player = player

    def update(self):
        self.player.play_sound("jump.wav")
        self.player.play_sound("pickup_coin.wav")
        self.player.update(logger)

# Create entity with audio
player = Entity("Player")
player.add_component(AudioComponent(audio))

# Simulate frame
logger.info(f"Scene contains: {player}")
player.update()

logger.info("VTXEngine Shutdown.")
