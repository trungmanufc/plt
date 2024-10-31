import unittest
from piglatin import PigLatin
from error import PigLatinError


class TestPigLatin(unittest.TestCase):

    def test_piglatin_get_phrase(self):
        p = PigLatin("Hello World")
        self.assertEqual("Hello World", p.get_phrase())

    def test_piglatin_create(self):
        pass;
