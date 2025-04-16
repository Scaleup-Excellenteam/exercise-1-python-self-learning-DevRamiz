class PostOffice:
    def __init__(self, users):
        self.users = users
        self.inboxes = {user: [] for user in users}

    def send(self, sender, recipient, title, body, urgent=False):
        if recipient not in self.inboxes:
            raise ValueError("Recipient not found")
        self.inboxes[recipient].append({
            'from': sender,
            'title': title,
            'body': body,
            'urgent': urgent
        })

    def read(self, user):
        if self.inboxes[user]:
            return self.inboxes[user].pop(0)
        return None
