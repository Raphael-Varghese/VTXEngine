class NetworkSimulator:
    def __init__(self):
        self.server_queue = []
        self.client_queue = []

    def send_to_server(self, message):
        self.server_queue.append(message)

    def send_to_client(self, message):
        self.client_queue.append(message)

    def process_server(self, logger):
        while self.server_queue:
            msg = self.server_queue.pop(0)
            logger.info(f"[Server] Received: {msg}")
            self.send_to_client(f"Echo: {msg}")

    def process_client(self, logger):
        while self.client_queue:
            msg = self.client_queue.pop(0)
            logger.info(f"[Client] Received: {msg}")
