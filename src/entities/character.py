class Character:
    def __init__(self, name, character_id=None):
        self.name = name
        self.character_id = character_id

    def __str__(self):
        return self.name

    def __repr__(self):
        return f"Character(name='{self.name}', id={self.character_id})"
