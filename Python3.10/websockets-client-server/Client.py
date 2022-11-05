class Client:
    client_id = None
    name = None

    def __init__(self, c_id, new_name):
        self.client_id = c_id
        self.name = new_name

    def desc(self) -> str:
        return str(f'   client ID: {self.client_id}\n   name: {self.name}')
