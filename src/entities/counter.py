class Counter:
    """Represents a counter-pick relationship between two characters.

    A counter relationship indicates that one character is effective against
    another character in the game.

    Attributes:
        character_id: The database ID of the character being countered.
        counter_character_id: The database ID of the character that counters.
        counter_id: The unique database identifier for this relationship.
            Defaults to None for new relationships before database insertion.
    """

    def __init__(self, character_id, counter_character_id, counter_id=None):
        """Initialize a new Counter instance.

        Args:
            character_id: The database ID of the character being countered.
            counter_character_id: The database ID of the countering character.
            counter_id: Database ID. Defaults to None.
        """
        self.character_id = character_id
        self.counter_character_id = counter_character_id
        self.counter_id = counter_id

    def __repr__(self):
        return (f"Counter(character_id={self.character_id}, "
                f"counter_character_id={self.counter_character_id}, "
                f"id={self.counter_id})")
