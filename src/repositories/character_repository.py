from entities.character import Character
from database_connection import get_database_connection

class CharacterRepository:
    def __init__(self, connection):
        self._connection = connection

    def create(self, character):
        cursor = self._connection.cursor()

        cursor.execute("INSERT INTO characters (name) VALUES (?)",
                       (character.name,))

        self._connection.commit()

        character.character_id = cursor.lastrowid

        return character

    def find_all(self):
        cursor = self._connection.cursor()

        cursor.execute("SELECT id, name FROM characters ORDER BY name ASC")

        rows = cursor.fetchall()

        characters = []
        for row in rows:
            character = Character(name=row["name"], character_id=row["id"])
            characters.append(character)

        return characters

    def delete_all(self):
        cursor = self._connection.cursor()

        cursor.execute("DELETE FROM characters")

        self._connection.commit()

character_repository = CharacterRepository(get_database_connection())
