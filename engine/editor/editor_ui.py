class EditorUI:
    def __init__(self):
        self.scene_entities = []

    def add_entity(self, entity):
        self.scene_entities.append(entity)

    def render(self, logger):
        print("\n=== VTXEditor ===")
        print(f"Entities in Scene: {len(self.scene_entities)}")
        for i, entity in enumerate(self.scene_entities):
            print(f"[{i}] {entity.name}")
            for comp in entity.components:
                print(f"    - {comp}")
        print("=================\n")
        logger.info("[Editor] Scene rendered")
