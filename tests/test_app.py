import unittest

from app import greet


class TestGreet(unittest.TestCase):
    def test_default_greeting(self):
        self.assertEqual(greet(), "Hello, Azure DevOps!")

    def test_custom_greeting(self):
        self.assertEqual(greet("Funmibi"), "Hello, Funmibi!")


if __name__ == "__main__":
    unittest.main()
