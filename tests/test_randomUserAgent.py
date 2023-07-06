import unittest
from src.randomUserAgent import random_user_agent

class TestRandomUserAgent(unittest.TestCase):

    def test_not_None(self):
        self.assertEqual(type(random_user_agent()), str)

    def test_persistence(self):
        string = 'Mozilla/5.0 (Windows NT 10.0; x86; rv:107.0) Gecko/20100101 Firefox/107.0'
        self.assertEqual(random_user_agent(1), string)


if __name__ == '__main__':
    unittest.main()
