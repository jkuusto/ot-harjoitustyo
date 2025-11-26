import sqlite3
from entities.counter import Counter
from database_connection import get_database_connection


class CounterRepository:
    def __init__(self, connection):
        self._connection = connection

    def create(self, character_id, counter_character_id):
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

    def delete_all(self):
        cursor = self._connection.cursor()

        cursor.execute("DELETE FROM counters")

        self._connection.commit()


counter_repository = CounterRepository(get_database_connection())
