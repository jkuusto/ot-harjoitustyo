import sqlite3
from entities.counter import Counter
from database_connection import get_database_connection


class CounterRepository:
    """Manages counter-pick relationship data in the database.

    Handles all database operations related to counter relationships between
    characters, including creating, reading, and deleting counter records.

    Attributes:
        _connection: The database connection object.
    """

    def __init__(self, connection):
        """Initialize a new CounterRepository instance.

        Args:
            connection: The database connection object.
        """
        self._connection = connection

    def create(self, character_id, counter_character_id):
        """Create a new counter relationship in the database.

        Args:
            character_id: The database ID of the character being countered.
            counter_character_id: The database ID of the countering character.

        Returns:
            The Counter object with updated counter_id.

        Raises:
            ValueError: If the counter relationship already exists.
        """
        cursor = self._connection.cursor()

        try:
            cursor.execute("""
                INSERT INTO counters (character_id, counter_character_id)
                VALUES (?, ?)
            """, (character_id, counter_character_id))
        except sqlite3.IntegrityError as error:
            if "UNIQUE constraint failed" in str(error):
                raise ValueError(
                    f"Duplicate: {character_id} -> {counter_character_id}") from error
            raise

        self._connection.commit()

        counter = Counter(character_id, counter_character_id,
                          counter_id=cursor.lastrowid)

        return counter

    def find_counters_for(self, character_id):
        """Find all counter relationships for a specific character.

        Args:
            character_id: The database ID of the character to find counters for.

        Returns:
            A list of Counter objects representing characters that counter
            the specified character.
        """
        cursor = self._connection.cursor()

        cursor.execute("""
            SELECT id, character_id, counter_character_id
            FROM counters
            WHERE character_id = ?
        """, (character_id,))

        rows = cursor.fetchall()

        counters = []
        for row in rows:
            counter = Counter(
                character_id=row["character_id"],
                counter_character_id=row["counter_character_id"],
                counter_id=row["id"]
            )
            counters.append(counter)

        return counters

    def delete(self, character_id, counter_character_id):
        """Delete a counter relationship from the database.

        Args:
            character_id: The database ID of the character being countered.
            counter_character_id: The database ID of the countering character.

        Returns:
            True if the relationship was deleted, False if not found.
        """
        cursor = self._connection.cursor()

        cursor.execute("""
            SELECT id FROM counters
            WHERE character_id = ? AND counter_character_id = ?
        """, (character_id, counter_character_id))

        result = cursor.fetchone()

        if result:
            cursor.execute("""
                DELETE FROM counters
                WHERE character_id = ? AND counter_character_id = ?
            """, (character_id, counter_character_id))
            self._connection.commit()
            return True

        return False

    def delete_all(self):
        """Delete all counter relationships from the database.

        This method is primarily used for testing purposes.
        """
        cursor = self._connection.cursor()

        cursor.execute("DELETE FROM counters")

        self._connection.commit()


counter_repository = CounterRepository(get_database_connection())
