from database_connection import get_database_connection


def drop_tables(connection):
    cursor = connection.cursor()

    cursor.execute("DROP TABLE IF EXISTS counters")
    cursor.execute("DROP TABLE IF EXISTS characters")

    connection.commit()


def create_tables(connection):
    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE characters (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL UNIQUE COLLATE NOCASE
        );
    """)

    cursor.execute("""
        CREATE TABLE counters (
            id INTEGER PRIMARY KEY,
            character_id INTEGER NOT NULL,
            counter_character_id INTEGER NOT NULL,
            FOREIGN KEY (character_id) REFERENCES characters (id) ON DELETE CASCADE,
            FOREIGN KEY (counter_character_id) REFERENCES characters (id) ON DELETE CASCADE,
            UNIQUE (character_id, counter_character_id)
        );
    """)

    connection.commit()


def initialize_database():
    connection = get_database_connection()
    drop_tables(connection)
    create_tables(connection)


if __name__ == "__main__":
    initialize_database()
