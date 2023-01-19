

from unittest import TestCase


class Animal:
    def __init__(self, name):
        self.name = name

    def say_name(self):
        return f'The animal says its name is {self.name}'


class AnimalTest(TestCase):
    def setUp(self) -> None:
        self.obj = Animal(name='Alfredo')
        self.name = 'Alfredo'

    def test_say_name(self):
        self.assertEqual(self.obj.say_name(), f'The animal says its name is {self.name}')
