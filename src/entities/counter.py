class Counter:
    def __init__(self, character_id, counter_character_id, counter_id=None):
        self.character_id = character_id
        self.counter_character_id = counter_character_id
        self.counter_id = counter_id

    def __repr__(self):
        return (f"Counter(character_id={self.character_id}, "
                f"counter_character_id={self.counter_character_id}, "
                f"id={self.counter_id})")
