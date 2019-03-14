import unittest
from Question import *


class test_Question(unittest.TestCase):
    def test_question(self):
        my_question = Question(True)
        my_question.question_text = "Do you think this is going to work?"
        self.assertEqual(my_question.question_text, "Do you think this is going to work?")
        self.assertEqual(my_question.add_answer("Yes", "Y"), True)
        self.assertEqual(my_question.answer_encoding_exists("Y"), True)
        self.assertEqual(my_question.add_answer("No", "N"), True)
        self.assertEqual(my_question.answer_encoding_exists("N"), True)
        self.assertEqual(my_question.add_answer("Negatory", "NEG"), False)
        self.assertEqual(my_question.answer_encoding_exists("NEG"), False)
        self.assertEqual(my_question.add_answer("Nancy Drew", "N"), False)
        self.assertEqual(my_question.answer_map["N"].answer_text, "No")
        my_answer_list_0 = my_question.get_answer_list()
        self.assertEqual(len(my_answer_list_0), 2)
        self.assertEqual(my_answer_list_0[0].answer_text, "Yes")
        self.assertEqual(my_answer_list_0[1].answer_text, "No")

        # test randomized functionality
        my_question.preserve_answer_order = False
        my_question.add_answer("Test", "T")
        my_answer_list_1 = my_question.get_answer_list()
        self.assertEqual(len(my_answer_list_1), 3)

        # check to make sure all three answers are in the list
        found_yes = False
        found_no = False
        found_test = False
        for t_a in my_answer_list_1:
            if t_a.answer_text == "Yes":
                found_yes = True
            elif t_a.answer_text == "Test":
                found_test = True
            elif t_a.answer_text == "No":
                found_no = True
        self.assertTrue(found_yes and found_no and found_test)


if __name__ == '__main__':
    unittest.main()
