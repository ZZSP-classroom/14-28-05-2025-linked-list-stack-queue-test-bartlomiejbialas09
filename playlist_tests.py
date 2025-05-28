import unittest
from playlist_manager import LinkedList

class TestPlaylistManager(unittest.TestCase):
    def test_add_and_get_next_song(self):
        p = LinkedList()
        p.add_song("Song1", "Artist1")
        self.assertEqual(p.get_next_song().title, "Song1")

    def test_remove_song(self):
        p = LinkedList()
        p.add_song("Song1", "Artist1")
        p.remove_song()
        self.assertIsNone(p.get_next_song())

if __name__ == "__main__":
    unittest.main()