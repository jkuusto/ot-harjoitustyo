import unittest
from entities.counter import Counter
from entities.character import Character
from repositories.counter_repository import counter_repository
from repositories.character_repository import character_repository


class TestCounterEntity(unittest.TestCase):
    def setUp(self):
        self.counter = Counter(1, 2, 1)

    def test_counter_can_be_created_and_character_attributes_are_accessible(self):
        self.assertEqual(self.counter.character_id, 1)
        self.assertEqual(self.counter.counter_character_id, 2)

    def test_repr_returns_correct_data(self):
        self.assertEqual(self.counter.__repr__(),
                         "Counter(character_id=1, counter_character_id=2, id=1)")


class TestCounterRepository(unittest.TestCase):
    def setUp(self):
        counter_repository.delete_all()
        character_repository.delete_all()

    def _generate_test_characters(self):
        character1 = character_repository.create(Character("Chosen One"))
        character2 = character_repository.create(Character("The Counterer"))

        return character1, character2

    def test_counter_with_duplicate_relationship_cannot_be_created_in_db(self):
        character1, character2 = self._generate_test_characters()
        counter_repository.create(
            character1.character_id, character2.character_id)
        with self.assertRaises(ValueError):
            counter_repository.create(
                character1.character_id, character2.character_id)

        counters = counter_repository.find_counters_for(
            character1.character_id)

        self.assertEqual(len(counters), 1)

    def test_counter_relationship_can_be_created_in_db(self):
        character1, character2 = self._generate_test_characters()
        counter = counter_repository.create(
            character1.character_id, character2.character_id)

        self.assertIsNotNone(counter.counter_id)
        self.assertEqual(counter.character_id, character1.character_id)
        self.assertEqual(counter.counter_character_id, character2.character_id)

    def test_counter_data_can_be_found_for_a_specific_character(self):
        character1, character2 = self._generate_test_characters()
        counter_repository.create(
            character1.character_id, character2.character_id)

        counters = counter_repository.find_counters_for(
            character1.character_id)
        counter_ids = [c.counter_character_id for c in counters]

        self.assertEqual(len(counters), 1)
        self.assertIn(character2.character_id, counter_ids)
