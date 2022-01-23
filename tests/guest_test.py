import unittest
from classes.guest import Guest
class TestGuest(unittest.TestCase):
    def setUp(self):
        self.guests = Guest("Rachel")

    # passed test
    def test_has_name(self):
        self.assertEqual("Rachel", self.guests.name)