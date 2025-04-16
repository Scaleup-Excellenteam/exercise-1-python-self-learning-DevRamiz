class PostOffice:
    def __init__(self, users):
        self.inboxes = {user: [] for user in users}
        self.counter = 1
        self.messages = {}

    def send_message(self, sender, recipient, title, body, urgent=False):
        if recipient not in self.inboxes:
            raise KeyError("Recipient not found")
        msg = {
            "id": self.counter,
            "from": sender,
            "to": recipient,
            "title": title,
            "body": body,
            "unread": True,
            "urgent": urgent
        }
        self.messages[self.counter] = msg
        if urgent:
            self.inboxes[recipient].insert(0, msg)
        else:
            self.inboxes[recipient].append(msg)
        self.counter += 1
        return msg["id"]

    def read_inbox(self, user, n=None):
        inbox = self.inboxes[user]
        messages = inbox[:n] if n else inbox
        for msg in messages:
            msg["unread"] = False
        return messages

    def search_inbox(self, user, keyword):
        keyword = keyword.lower()
        return [
            msg for msg in self.inboxes[user]
            if keyword in msg["title"].lower() or keyword in msg["body"].lower()
        ]

    @property
    def boxes(self):
        return self.inboxes
