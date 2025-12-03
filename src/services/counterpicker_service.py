from entities.character import Character


class CounterPickerService:
    """Handles business logic for the counterpicker application.

    This service manages character and counter operations, providing
    a clean interface between the UI and data repositories.

    Attributes:
        _character_repository: Repository for character data operations.
        _counter_repository: Repository for counter relationship operations.
    """

    def __init__(self, character_repository, counter_repository):
        """Initialize the service with required repositories.

        Args:
            character_repository: CharacterRepository instance.
            counter_repository: CounterRepository instance.
        """
        self._character_repository = character_repository
        self._counter_repository = counter_repository

    def get_all_characters(self):
        """Get all characters from the database.

        Returns:
            List of Character objects.
        """
        return self._character_repository.find_all()

    def find_character_by_name(self, name):
        """Find a character by name (case-insensitive).

        Args:
            name: The name to search for.

        Returns:
            Character object if found, None otherwise.
        """
        characters = self._character_repository.find_all()
        name_lower = name.strip().lower()

        for character in characters:
            if character.name.lower() == name_lower:
                return character

        return None

    def create_character(self, name):
        """Create a new character with validation.

        Args:
            name: Name of the character to create.

        Returns:
            The created Character object.

        Raises:
            ValueError: If name is empty or character already exists.
        """
        if not name or not name.strip():
            raise ValueError("Character name cannot be empty")

        if self.find_character_by_name(name):
            raise ValueError(f"Character '{name.strip()}' already exists")

        character = Character(name.strip())
        return self._character_repository.create(character)

    def delete_character(self, name):
        """Delete a character by name.

        Args:
            name: Name of the character to delete.

        Returns:
            True if deleted, False if character not found.
        """
        if not name or not name.strip():
            return False

        return self._character_repository.delete_character(name.strip())

    def create_counter_relationship(self, character_id, counter_character_id):
        """Create a counter relationship between two characters.

        Args:
            character_id: ID of the character being countered.
            counter_character_id: ID of the character that counters.

        Raises:
            ValueError: If relationship already exists or IDs are invalid.
        """
        self._counter_repository.create(character_id, counter_character_id)

    def get_counters_for_character(self, character_id):
        """Get all counters for a specific character.

        Args:
            character_id: ID of the character.

        Returns:
            List of Counter objects.
        """
        return self._counter_repository.find_counters_for(character_id)

    def get_counter_details(self, character_id):
        """Get detailed counter information for a character.

        Returns counters with full character details rather than just IDs.

        Args:
            character_id: ID of the character to get counters for.

        Returns:
            List of dictionaries containing (counter_id, counter_character_name).
        """
        counters = self._counter_repository.find_counters_for(character_id)

        counter_details = []
        for counter in counters:
            counter_character = self._character_repository.find_by_id(
                counter.counter_character_id
            )
            counter_details.append({
                "counter_id": counter.counter_id,
                "character_name": counter_character.name
            })

        return counter_details
