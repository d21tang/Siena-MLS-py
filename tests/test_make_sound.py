import unittest
from siena_mls import makeSound

class TestMakeSound(unittest.TestCase):
    def test_valid_sound(self):
        sound_object = makeSound("tests/assets/sample-6s.wav")
        self.assertIsNotNone(sound_object)

if __name__ == '__main__':
    unittest.main()
