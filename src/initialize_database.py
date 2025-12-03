from database_connection import get_database_connection


def drop_tables(connection):
    """Drop all database tables.

    Args:
        connection: The database connection object.
    """
    cursor = connection.cursor()

    cursor.execute("DROP TABLE IF EXISTS counters")
    cursor.execute("DROP TABLE IF EXISTS characters")

    connection.commit()


def create_tables(connection):
    """Create all required database tables.

    Creates the characters and counters tables with appropriate
    constraints and relationships.

    Args:
        connection: The database connection object.
    """
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
    """Initialize the database by dropping and recreating all tables.

    This function resets the database to a clean state by dropping
    existing tables and creating new ones with the current schema.
    """
    connection = get_database_connection()
    drop_tables(connection)
    create_tables(connection)


if __name__ == "__main__":
    initialize_database()
