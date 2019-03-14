import unittest
from Answer import *

class test_Answer(unittest.TestCase):
    def test_answer(self):
        my_answer = Answer()
        my_answer.answer_text = "ridiculous"
        self.assertEqual(my_answer.answer_text, "ridiculous")
        self.assertEqual(my_answer.set_one_char_encoding("2"), True)
        self.assertEqual(my_answer.answer_encoding, "2")
        self.assertEqual(my_answer.set_one_char_encoding("adsj"), False)
        self.assertEqual(my_answer.answer_encoding, "2")

    def test_serialize(self):
        my_answer = Answer()
        my_answer.answer_text = "ridiculous"
        my_answer.set_one_char_encoding("2")

if __name__ == '__main__':
    unittest.main()
