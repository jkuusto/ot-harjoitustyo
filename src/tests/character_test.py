import unittest
from entities.character import Character

class TestCharacter(unittest.TestCase):
    def setUp(self):
        print("No setup created")

    def test_character_can_be_created_and_name_is_accessible(self):
        character = Character("Tester")
        self.assertEqual(character.name, "Tester")
