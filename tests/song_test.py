import unittest
from classes.song import Song
from classes.room import Room

class TestSong(unittest.TestCase):

    def setUp(self):
        self.song = Song("Left Behind", "Slipknot")

    # Passed test
    def test_song_has_name(self):
        self.assertEqual("Left Behind", self.song.name)

    # Passed test
    def test_song_has_artist(self):
        self.assertEqual("Slipknot", self.song.artist)

  