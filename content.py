class Content:
    def __init__(self):
        with open('signal.txt', 'r') as file:
            self.data = file.read().strip()
            self._key = 43                          # Standard