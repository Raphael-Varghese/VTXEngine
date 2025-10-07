# main.py
# TitanForge Engine Phase 1 - Manual Module Loader

import time

# Load logger.py manually
logger_globals = {}
with open("engine/core/logger.py", "r") as f:
    exec(f.read(), logger_globals)

# Load timer.py manually
timer_globals = {}
with open("engine/core/timer.py", "r") as f:
    exec(f.read(), timer_globals)

# Create instances
Logger = logger_globals["Logger"]
Timer = timer_globals["Timer"]

logger = Logger()
timer = Timer()

logger.info("VTXEngine Engine Booting...")

for frame in range(5):
    logger.info(f"--- Frame {frame + 1} ---")
    timer.reset()

    logger.info("Updating game objects...")
    time.sleep(0.2)

    logger.info("Rendering frame...")
    time.sleep(0.2)

    elapsed = timer.elapsed()
    logger.info(f"Frame completed in {elapsed:.3f} seconds")

logger.info("Engine shutdown.")
