class UI:
    def __init__(self, io, character_repository):
        self._io = io
        self._character_repository = character_repository

    def start(self):
        while True:
            self._show_header()
            self._show_characters()
            self._show_menu()

            choice = self._io.read("Choose action: ")

            if choice == "1":
                self._add_character()
            elif choice == "2":
                self._io.write("Ending session...\n")
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
        self._io.write("  2) Exit")

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
            self._io.write(f"{character.name} added!\n")
        except Exception as e:
            self._io.write(f"Error could not add character. {str(e)}\n")
