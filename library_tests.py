import unittest
from library_reservation import Queue, Reservation

class TestLibraryReservation(unittest.TestCase):
    def test_queue_order(self):
        q = Queue()
        q.enqueue(Reservation("Person1", "Book1"))
        q.enqueue(Reservation("Person2", "Book2"))
        self.assertEqual(q.peek().user_name, "Person1")

    def test_dequeue(self):
        q = Queue()
        q.enqueue(Reservation("Person1", "Book1"))
        q.dequeue()
        self.assertIsNone(q.peek())

if __name__ == "__main__":
    unittest.main()