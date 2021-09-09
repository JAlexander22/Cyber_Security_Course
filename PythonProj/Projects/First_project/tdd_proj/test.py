import unittest
import calculator


class Calcttest(unittest.TestCase):
    def test_add(self):
        self.assertEqual(calculator.add(2, 5), 7)