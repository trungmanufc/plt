import unittest
from piglatin import PigLatin
from error import PigLatinError


class TestPigLatin(unittest.TestCase):

    def test_piglatin_get_phrase(self):
        p = PigLatin("Hello World")
        self.assertEqual("Hello World", p.get_phrase())

    def test_translate_empty_phrase(self):
        p = PigLatin('')
        self.assertEqual("nil", p.translate())

    def test_translate_end_with_y(self):
        pass

    def test_translate_end_with_vowel(self):
        pass

    def test_translate_end_with_consonant(self):
        p = PigLatin("hello")
        self.assertEqual("ellohay", p.translate())


