import unittest
from services.counterpicker_service import CounterPickerService


class FakeCharacterRepository:
    def __init__(self, characters=None):
        self.characters = characters or []

    def find_all(self):
        return self.characters

    def create(self, character):
        if any(char.name == character.name for char in self.characters):
            raise ValueError(
                f"Duplicate: {character.name}")

        character.character_id = len(self.characters) + 1
        self.characters.append(character)
        return character


class FakeCounterRepository:
    def __init__(self, counters=None):
        self.counters = counters or []

    def find_all(self):
        return self.counters


class TestCounterPickerService(unittest.TestCase):
    def setUp(self):
        self.counterpicker_service = CounterPickerService(
            FakeCharacterRepository(),
            FakeCounterRepository()
        )

    def test_create_character_with_valid_name(self):
        self.counterpicker_service.create_character("Tester")
        characters = self.counterpicker_service.get_all_characters()

        self.assertEqual(len(characters), 1)
        self.assertEqual(characters[0].name, "Tester")
