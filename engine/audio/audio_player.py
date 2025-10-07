class AudioPlayer:
    def __init__(self):
        self.queue = []

    def play_sound(self, sound_name):
        self.queue.append(sound_name)

    def update(self, logger):
        while self.queue:
            sound = self.queue.pop(0)
            logger.info(f"[Audio] Playing sound: {sound}")
