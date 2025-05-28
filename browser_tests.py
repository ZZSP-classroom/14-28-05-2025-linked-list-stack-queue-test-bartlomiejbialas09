import unittest
from browser_history import Stack

class TestBrowserHistory(unittest.TestCase):
    def test_stack_navigation(self):
        s = Stack()
        s.push("site1")
        s.push("site2")
        self.assertEqual(s.pop(), "site2")
        self.assertEqual(s.peek(), "site1")

if __name__ == "__main__":
    unittest.main()