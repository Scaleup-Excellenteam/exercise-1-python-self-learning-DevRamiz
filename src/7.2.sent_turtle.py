class PostOffice:
    def __init__(self):
        self.messages = []

    def send(self, message: str):
        self.messages.append(message)

    def receive(self):
        return self.messages.pop(0) if self.messages else None
