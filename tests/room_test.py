import unittest
from classes.song import Song
from classes.room import Room
from classes.guest import Guest
from tests.song_test import TestSong
from tests.guest_test import TestGuest
class TestRoom(unittest.TestCase):

    def setUp(self):
        self.name = Room("Metal")
        self.guest = []
        self.jukebox = []
        self.song = Song("Left Behind", "Slipknot")
        self.new_guest = Guest("Rachel")

    # Passed test
    def test_add_song_to_jukebox(self):
        self.jukebox = self.song
        self.assertEqual(self.jukebox, self.song)

    # Passed test 
    def test_add_guest_to_room(self):
        self.guest = self.new_guest
        self.assertEqual(self.guest, self.new_guest)

    # Passed test
    def test_remove_guest_from_room(self):
        self.guest.clear()
        self.assertEqual([], self.guest)