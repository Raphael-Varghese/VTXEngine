import os

class AssetManager:
    def __init__(self, base_path="assets"):
        self.base_path = base_path

    def list_assets(self, category):
        path = os.path.join(self.base_path, category)
        if not os.path.exists(path):
            return []
        return [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]

    def load_asset(self, category, filename):
        path = os.path.join(self.base_path, category, filename)
        if not os.path.exists(path):
            return None
        with open(path, "r") as f:
            return f.read()

    def save_asset(self, category, filename, content):
        path = os.path.join(self.base_path, category)
        os.makedirs(path, exist_ok=True)
        with open(os.path.join(path, filename), "w") as f:
            f.write(content)
