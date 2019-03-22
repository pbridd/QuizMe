import unittest
import xml.etree.ElementTree as ET
import xml_conversion
import Answer

class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.test_tree = ET.parse('test_collateral/test_xml/test_quiz.xml')
        self.test_tree_root = self.test_tree.getroot()

    def test_convert_answer(self):
        first_question_xml = self.test_tree_root.find("question")
        first_answer_xml = first_question_xml.find("answer")
        answer_object = xml_conversion.xml_to_answer(first_answer_xml)
        self.assertEqual(answer_object.answer_text, "Because it's beautiful")
        self.assertEqual(answer_object.answer_encoding, "A")

    def test_convert_question(self):
        first_question_xml = self.test_tree_root.find("question")
        question_object = xml_conversion.xml_to_question(first_question_xml)

        self.assertEqual(question_object.question_text, "Why is the sky blue?")
        self.assertEqual(question_object.question_number, 1)
        self.assertEqual(len(question_object.answer_map), 2)

    def test_convert_quiz(self):
        quiz_xml = self.test_tree_root
        quiz_object = xml_conversion.xml_to_quiz(quiz_xml)
        self.assertEqual(quiz_object.quiz_name, "Optimist or Pessimist?")
        self.assertEqual(len(quiz_object.question_map), 2)
        self.assertEqual(quiz_object.question_map[1].question_text, "Why is the sky blue?")
        self.assertEqual(quiz_object.question_map[2].question_text, "Is the cup half full or half empty?")
        self.assertEqual(quiz_object.question_map[1].answer_map["A"].answer_text,
                         "Because it's beautiful")
        self.assertEqual(quiz_object.question_map[1].answer_map["B"].answer_text,
                         "It's not. It's actuall"
                         "y hideous.")


if __name__ == '__main__':
    unittest.main()
