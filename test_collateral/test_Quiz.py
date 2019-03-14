import unittest
from Quiz import *


class MyTestCase(unittest.TestCase):
    def test_quiz(self):
        test_quiz = Quiz("my quiz")
        self.assertEqual(test_quiz.quiz_name, "my quiz")

        test_answer_list = ["Charizard", "Pikachu", "Blastoise", "Venusaur"]
        test_quiz.add_question("Who is your favorite pokemon?", test_answer_list, False)
        added_question = test_quiz.question_list[0]
        self.assertEqual(added_question.question_text, "Who is your favorite pokemon?")


if __name__ == '__main__':
    unittest.main()
