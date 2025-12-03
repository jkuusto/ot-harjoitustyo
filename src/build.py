from initialize_database import initialize_database


def build():
    """Initialize the application database.
    
    This function sets up the database by creating all necessary tables.
    It should be run before the first use of the application or when
    resetting the database to a clean state.
    """
    initialize_database()


if __name__ == "__main__":
    build()
