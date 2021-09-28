class User:
    def __init__(self, name, token):
        self._name = name
        self._token = token

    @property
    def name(self):
        return self._name
    
    @property
    def token(self):
        return self._token

    def __str__(self):
        return f'username:{self.name} token:{self.token}'
