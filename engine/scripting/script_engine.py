class ScriptEngine:
    def __init__(self, logger):
        self.context = {"logger": logger}  # Inject logger into script context

    def run_script(self, script_text, logger):
        try:
            exec(script_text, self.context)
            logger.info("[Script] Executed successfully")
        except Exception as e:
            logger.error(f"[Script] Error: {e}")
