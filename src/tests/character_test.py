import unittest
from entities.character import Character


class TestCharacter(unittest.TestCase):
    def setUp(self):
        self.character = Character("Tester", 1)

    def test_character_can_be_created_and_name_is_accessible(self):
        self.assertEqual(self.character.name, "Tester")

    def test_str_returns_character_name(self):
        self.assertEqual(self.character.__str__(), "Tester")

    def test_repr_returns_correct_data(self):
        self.assertEqual(self.character.__repr__(),
                         "Character(name='Tester', id=1)")

    def test_repr_returns_correct_data_when_no_id(self):
        character = Character("IDlessTester")
        self.assertEqual(character.__repr__(),
                         "Character(name='IDlessTester', id=None)")
