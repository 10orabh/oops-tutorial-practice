class chatbook:
    Accounts = {
    }
    def __init__(self):
        self.username = ""
        self.password = ""
        self.logged_in = False
        self.friends = []
    def register(self, username, password):
        self.username = username
        self.password = password
        print(f"User {username} registered successfully.")
