from tabulate import tabulate


class UI:
    """Manages the text-based user interface for the application.

    Handles user interaction through a console menu system, allowing users
    to manage characters and counter-pick relationships.

    Attributes:
        _io: The console I/O handler.
        _service: The business logic service.
    """

    def __init__(self, io, counterpicker_service):
        """Initialize a new UI instance.

        Args:
            io: The console I/O handler.
            counterpicker_service: Service for business logic operations.
        """
        self._io = io
        self._service = counterpicker_service

    def start(self):
        """Start the main application loop.

        Displays the menu and processes user choices until exit is selected.
        """
        while True:
            self._show_header()
            self._show_characters()
            self._show_menu()

            choice = self._io.read("Choose action: ")

            if not self._handle_menu_choice(choice):
                break

    def _handle_menu_choice(self, choice):
        """Handle user's menu choice.

        Returns:
            False if user wants to exit, True otherwise.
        """
        if choice == "1":
            self._search_counters()
        elif choice == "2":
            self._add_counter()
        elif choice == "3":
            self._delete_counter()
        elif choice == "4":
            self._add_character()
        elif choice == "5":
            self._delete_character()
        elif choice == "x":
            self._io.write("\nApplication closed.\n")
            return False
        else:
            self._io.write("Invalid choice. Try again.")

        return True

    def _show_header(self):
        """Display the application header."""
        self._io.write("=============\nCounterpicker\n=============")

    def _show_characters(self):
        """Display the list of all characters in the database."""
        self._io.write("\nCharacters:")

        characters = self._service.get_all_characters()

        if len(characters) == 0:
            self._io.write("(no characters added)")
        else:
            names = [character.name for character in characters]
            self._io.write(f"{", ".join(names)}")

        self._io.write("")

    def _show_menu(self):
        """Display the main menu options."""
        self._io.write("Actions:")
        self._io.write("  1) Search counters")
        self._io.write("  2) Add counter")
        self._io.write("  3) Delete counter")
        self._io.write("  4) Add character")
        self._io.write("  5) Delete character")
        self._io.write("  x) Exit")

    def _add_character(self):
        """Handle adding a new character to the database."""
        self._io.write("")
        name = self._io.read("Enter character name: ")

        try:
            character = self._service.create_character(name)  # Changed
            self._io.write(f"{character.name} added successfully.\n")
        except ValueError as e:
            self._io.write(f"Error: {str(e)}\n")

    def _delete_character(self):
        """Handle deleting a character from the database."""
        self._io.write("")
        name = self._io.read("Character to delete: ")

        if not name.strip():
            self._io.write("No character selected for deletion.\n")
            return

        try:
            success = self._service.delete_character(name)

            if success:
                self._io.write(f"{name} deleted successfully.\n")
            else:
                self._io.write(f"{name} not found.\n")
        except Exception as e:
            self._io.write(f"Error: Could not delete character. {str(e)}\n")

    def _prompt_and_find_character(self, prompt):
        """Prompt for character name and find the character.

        Returns:
            Character object if found and valid, None otherwise.
        """
        self._io.write("")
        character_name = self._io.read(prompt)

        if not character_name.strip():
            self._io.write("Character name cannot be empty.\n")
            return None

        character = self._service.find_character_by_name(character_name)

        if not character:
            self._io.write(f"Character '{character_name}' not found.\n")
            return None

        return character

    def _add_counter(self):
        """Handle adding a counter relationship between two characters."""
        character = self._prompt_and_find_character("Character name: ")
        if not character:
            return

        counter_character = self._prompt_and_find_character(
            "Counter character name: ")
        if not counter_character:
            return

        self._create_counter_relationship(character, counter_character)

    def _create_counter_relationship(self, character, counter_character):
        """Create a counter relationship between two characters."""
        try:
            self._service.create_counter_relationship(
                character.character_id,
                counter_character.character_id
            )
            self._io.write(
                f"Counter added: {counter_character.name} counters {character.name}.\n"
            )
        except ValueError as e:
            if str(e).startswith("Duplicate"):
                self._io.write("Counter relationship already exists.\n")
            else:
                self._io.write(f"Error: {str(e)}\n")
        except Exception as e:
            self._io.write(f"Error: Could not add counter. {str(e)}\n")

    def _search_counters(self):
        """Handle searching and displaying counters for a character."""
        character = self._prompt_and_find_character("Character name: ")
        if not character:
            return

        counter_details = self._service.get_counter_details(
            character.character_id)

        if len(counter_details) == 0:
            self._io.write(f"No counters for {character.name} added.\n")
            return

        self._display_counter_table(character, counter_details)

    def _build_counter_table_data(self, counter_details):
        """Build table data from counter detail dictionaries.

        Args:
            counter_details: List of dicts with 'counter_id' and 'character_name'.

        Returns:
            List of lists suitable for tabulate.
        """
        table_data = []
        for detail in counter_details:
            table_data.append([detail["character_name"]])
        return table_data

    def _display_counter_table(self, character, counter_details):
        """Display counters in a formatted table.

        Args:
            character: The Character object being countered.
            counter_details: List of counter detail dictionaries.
        """
        table_data = self._build_counter_table_data(counter_details)
        table_data.sort(key=lambda row: row[0].lower())

        headers = ["\033[1mName\033[0m"]

        self._io.write(f"\nCounters for {character.name}:")
        self._io.write("")
        self._io.write(
            tabulate(table_data, headers=headers, tablefmt="rounded_grid"))
        self._io.write("")
        self._io.read("Press Enter to continue... ")
        self._io.write("")

    def _delete_counter(self):
        """Handle deleting a counter relationship between two characters."""
        character = self._prompt_and_find_character("Character name: ")
        if not character:
            return

        counter_character = self._prompt_and_find_character(
            "Counter character to remove: "
        )
        if not counter_character:
            return

        success = self._service.delete_counter_relationship(
            character.character_id,
            counter_character.character_id
        )

        if success:
            self._io.write(
                f"Counter removed: {counter_character.name} no longer "
                f"counters {character.name}.\n"
            )
        else:
            self._io.write(
                f"Counter relationship not found: {counter_character.name} "
                f"was not set as a counter for {character.name}.\n"
            )
