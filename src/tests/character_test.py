import unittest
from entities.character import Character
from repositories.character_repository import character_repository


class TestCharacterEntity(unittest.TestCase):
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


class TestCharacterRepository(unittest.TestCase):
    def setUp(self):
        character_repository.delete_all()
        self.character1 = Character("Tester1")
        self.character2 = Character("Tester2")

    def test_character_can_be_created_in_db(self):
        character_returned = character_repository.create(self.character1)
        characters = character_repository.find_all()

        self.assertEqual(character_returned, self.character1)
        self.assertEqual(len(characters), 1)
        self.assertEqual(characters[0].name, self.character1.name)

    def test_character_with_duplicate_name_cannot_be_created_in_db(self):
        character_repository.create(self.character1)
        with self.assertRaises(ValueError):
            character_repository.create(self.character1)

        characters = character_repository.find_all()

        self.assertEqual(len(characters), 1)

    def test_character_can_be_found_by_id(self):
        character_returned = character_repository.create(self.character1)
        character = character_repository.find_by_id(
            character_returned.character_id)

        self.assertIsNotNone(character)
        assert character is not None
        self.assertEqual(character.character_id,
                         character_returned.character_id)

    def test_nonexisting_character_can_be_not_be_found_by_id(self):
        character = character_repository.find_by_id(999999)

        self.assertIsNone(character)

    def test_all_characters_in_db_can_be_found(self):
        character_repository.create(self.character1)
        character_repository.create(self.character2)
        characters = character_repository.find_all()

        self.assertEqual(len(characters), 2)
        self.assertEqual(characters[0].name, self.character1.name)
        self.assertEqual(characters[1].name, self.character2.name)

    def test_character_can_be_successfully_deleted(self):
        character_repository.create(self.character1)
        result = character_repository.delete_character(self.character1.name)
        characters = character_repository.find_all()

        self.assertEqual(result, True)
        self.assertEqual(len(characters), 0)

    def test_deleting_nonexisting_character_returns_false(self):
        character_repository.create(self.character1)
        result = character_repository.delete_character(self.character2.name)
        characters = character_repository.find_all()

        self.assertEqual(result, False)
        self.assertEqual(len(characters), 1)
