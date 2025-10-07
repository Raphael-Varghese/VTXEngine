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

# Begin simulation
logger.info("VTXEngine Booting...")

# Save a script asset
script_code = "print('[Asset Script] Hello from asset script')"
assets.save_asset("scripts", "hello_script.txt", script_code)

# Load and run the script
loaded_script = assets.load_asset("scripts", "hello_script.txt")
if loaded_script:
    logger.info("[Asset] Loaded script content:")
    logger.info(loaded_script)
    try:
        exec(loaded_script)
    except Exception as e:
        logger.error(f"[Asset] Script execution error: {e}")

# List available scripts
script_list = assets.list_assets("scripts")
logger.info(f"[Asset] Available scripts: {script_list}")

logger.info("VTXEngine Shutdown.")
