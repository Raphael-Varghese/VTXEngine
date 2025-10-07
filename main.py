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

# Begin simulation
logger.info("VTXEngine Booting...")

# Vector2 demo
v1 = Vector2(3, 4)
v2 = Vector2(1, 2)
v3 = v1 + v2
logger.info(f"Vector2 Addition: {v1} + {v2} = {v3}")
logger.info(f"Vector2 Magnitude of {v1}: {v1.magnitude():.2f}")
logger.info(f"Vector2 Normalized: {v1.normalize()}")

# Vector3 demo
v4 = Vector3(1, 0, 0)
v5 = Vector3(0, 1, 0)
v6 = v4.cross(v5)
logger.info(f"Vector3 Cross Product: {v4} x {v5} = {v6}")

logger.info("VTXEngine Shutdown.")
