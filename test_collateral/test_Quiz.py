import unittest
from Quiz import *
import Question


class MyTestCase(unittest.TestCase):
    def test_quiz(self):
        test_quiz = Quiz("my quiz")
        self.assertEqual(test_quiz.quiz_name, "my quiz")

        test_answer_list = ["Charizard", "Pikachu", "Blastoise", "Venusaur"]
        test_quiz.add_question("Who is your favorite pokemon?", test_answer_list, False, 2)
        added_question = test_quiz.question_map[2]
        self.assertEqual(added_question.question_text, "Who is your favorite pokemon?")

        constructed_question = Question.Question(True)
        constructed_question.question_text = "What's up?"
        constructed_question.add_answer("Not much", "A")
        constructed_question.question_number = 1
        test_quiz.add_constructed_question(constructed_question)
        self.assertEqual(len(test_quiz.question_map), 2)
        added_question = test_quiz.question_map[1]
        self.assertEqual(added_question.question_text, "What's up?")

        bad_question = Question.Question(True)
        bad_question.question_text = "I'm a terrible question!"
        self.assertFalse(test_quiz.add_constructed_question(bad_question))
        bad_question.add_answer("what kind of answer is this?", "E")
        bad_question.question_number = 1
        self.assertFalse(test_quiz.add_constructed_question(bad_question))



if __name__ == '__main__':
    unittest.main()
