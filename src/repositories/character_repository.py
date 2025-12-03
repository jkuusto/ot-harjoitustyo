import sqlite3
from entities.character import Character
from database_connection import get_database_connection


class CharacterRepository:
    """Manages character data in the database.

    Handles all database operations related to characters, including
    creating, reading, updating, and deleting character records.

    Attributes:
        _connection: The database connection object.
    """

    def __init__(self, connection):
        """Initialize a new CharacterRepository instance.

        Args:
            connection: The database connection object.
        """
        self._connection = connection

    def create(self, character):
        """Create a new character in the database.

        Args:
            character: The Character object to be stored.

        Returns:
            The Character object with updated character_id.

        Raises:
            ValueError: If a character with the same name already exists.
        """
        cursor = self._connection.cursor()

        try:
            cursor.execute("INSERT INTO characters (name) VALUES (?)",
                           (character.name,))
        except sqlite3.IntegrityError as error:
            if "UNIQUE constraint failed" in str(error):
                raise ValueError(f"Duplicate: {character.name}") from error
            raise

        self._connection.commit()

        character.character_id = cursor.lastrowid

        return character

    def find_by_id(self, character_id):
        """Find a character by their database ID.

        Args:
            character_id: The database ID of the character to find.

        Returns:
            A Character object if found, None otherwise.
        """
        cursor = self._connection.cursor()

        cursor.execute(
            "SELECT id, name FROM characters WHERE id = ?", (character_id,))
        row = cursor.fetchone()

        if row:
            return Character(name=row["name"], character_id=row["id"])
        return None

    def find_all(self):
        """Retrieve all characters from the database.

        Returns:
            A list of Character objects ordered alphabetically by name.
        """
        cursor = self._connection.cursor()

        cursor.execute("SELECT id, name FROM characters ORDER BY name ASC")

        rows = cursor.fetchall()

        characters = []
        for row in rows:
            character = Character(name=row["name"], character_id=row["id"])
            characters.append(character)

        return characters

    def delete_character(self, name: str):
        """Delete a character from the database by name.

        Args:
            name: The name of the character to delete.

        Returns:
            True if the character was deleted, False if not found.
        """
        cursor = self._connection.cursor()

        cursor.execute("SELECT * FROM characters WHERE name = ?", (name,))
        result = cursor.fetchone()

        if result:
            cursor.execute("DELETE FROM characters WHERE name = ?", (name,))
            self._connection.commit()
            return True

        return False

    def delete_all(self):
        """Delete all characters from the database.

        This method is primarily used for testing purposes.
        """
        cursor = self._connection.cursor()

        cursor.execute("DELETE FROM characters")

        self._connection.commit()


character_repository = CharacterRepository(get_database_connection())
