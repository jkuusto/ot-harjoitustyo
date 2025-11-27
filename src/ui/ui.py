class UI:
    def __init__(self, io, character_repository, counter_repository):
        self._io = io
        self._character_repository = character_repository
        self._counter_repository = counter_repository

    def start(self):
        while True:
            self._show_header()
            self._show_characters()
            self._show_menu()

            choice = self._io.read("Choose action: ")

            if choice == "1":
                self._add_character()
            elif choice == "2":
                self._add_counter()
            elif choice == "3":
                self._delete_character()
            elif choice == "x":
                self._io.write("\nSession closed.\n")
                break
            else:
                self._io.write("Invalid choice. Try again.")

    def _show_header(self):
        self._io.write("=============\nCounterpicker\n=============")

    def _show_characters(self):
        self._io.write("\nCharacters:")

        characters = self._character_repository.find_all()

        if len(characters) == 0:
            self._io.write("(no characters added)")
        else:
            names = [character.name for character in characters]
            self._io.write(f"{", ".join(names)}")

        self._io.write("")

    def _show_menu(self):
        self._io.write("Actions:")
        self._io.write("  1) Add character")
        self._io.write("  2) Add counter")
        self._io.write("  3) Delete character")
        self._io.write("  x) Exit")

    def _find_character_by_name(self, name):
        characters = self._character_repository.find_all()
        name_lower = name.lower()

        for character in characters:
            if character.name.lower() == name_lower:
                return character
            
        return None

    def _add_character(self):
        self._io.write("")
        name = self._io.read("Enter character name: ")

        if not name.strip():
            self._io.write("Character name cannot be empty.\n")
            return

        from entities.character import Character

        try:
            character = Character(name.strip())
            self._character_repository.create(character)
            self._io.write(f"{character.name} added successfully.\n")
        except Exception as e:
            if str(e).startswith("Duplicate"):
                self._io.write(f"Character '{name}' already exists.\n")
            else:
                self._io.write(f"Error: {str(e)}\n")

    def _delete_character(self):
        self._io.write("")
        name = self._io.read("Character to delete: ")

        if not name.strip():
            self._io.write("No character selected for deletion.\n")
            return

        try:
            success = self._character_repository.delete_character(name)

            if success:
                self._io.write(f"{name} deleted successfully.\n")
            else:
                self._io.write(f"{name} not found.\n")
        except Exception as e:
            self._io.write(f"Error: Could not delete character. {str(e)}\n")

    def _add_counter(self):
        self._io.write("")
        character_name = self._io.read("Character name: ")

        if not character_name.strip():
            self._io.write("Character name cannot be empty.\n")
            return
        
        character = self._find_character_by_name(character_name.strip())

        if not character:
            self._io.write(f"Character '{character_name}' not found.\n")
            return
        
        counter_name = self._io.read("Counter character name: ")

        if not counter_name.strip():
            self._io.write("Counter character name cannot be empty.\n")
            return
        
        counter_character = self._find_character_by_name(counter_name.strip())

        if not counter_character:
            self._io.write(f"Character '{counter_name}' not found.\n")
            return
        
        try:
            self._counter_repository.create(
                character.character_id,
                counter_character.character_id
            )
            self._io.write(
                f"Counter added: {counter_character.name} counters {character.name}.\n"
            )
        except ValueError as e:
            if str(e).startswith("Duplicate"):
                self._io.write(f"Counter relationship already exists.\n")
            else:
                self._io.write(f"Error: {str(e)}\n")
        except Exception as e:
            self._io.write(f"Error: Could not add counter. {str(e)}\n")
