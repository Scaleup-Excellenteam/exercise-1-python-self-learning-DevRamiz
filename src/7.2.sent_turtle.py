class PostOffice:
    def __init__(self, users):
        self.inboxes = {user: [] for user in users}
        self.messages = {}
        self.counter = 0

    def send_message(self, sender, recipient, title, body, urgent=False):
        if recipient not in self.inboxes:
            raise KeyError("Recipient not found")
        msg = {
            "id": self.counter,
            "from": sender,
            "to": recipient,
            "title": title,
            "body": body,
            "urgent": urgent,
            "read": False
        }
        self.messages[self.counter] = msg
        self.inboxes[recipient].append(self.counter)
        self.counter += 1
        return msg["id"]

    def read(self, user):
        if self.inboxes[user]:
            msg_id = self.inboxes[user].pop(0)
            self.messages[msg_id]["read"] = True
            return self.messages[msg_id]
        return None
