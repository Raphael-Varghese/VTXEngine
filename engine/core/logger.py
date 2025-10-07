class Logger:
    def info(self, message):
        print(f"[INFO] {message}")

    def warn(self, message):
        print(f"[WARN] {message}")

    def error(self, message):
        print(f"[ERROR] {message}")
