class Character:
    """Represents a game character in the application.

    Characters can be stored in a database and linked to counter-pick
    relationships with other characters.

    Attributes:
        name: The name of the character as a string.
        character_id: The unique database identifier for the character.
            Defaults to None for new characters before database insertion.
    """

    def __init__(self, name, character_id=None):
        """Initialize a new Character instance.

        Args:
            name: The name of the character.
            character_id: Database ID. Defaults to None.
        """
        self.name = name
        self.character_id = character_id

    def __str__(self):
        return self.name

    def __repr__(self):
        return f"Character(name='{self.name}', id={self.character_id})"
