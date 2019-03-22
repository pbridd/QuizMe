import Question
import Answer
from string import ascii_uppercase

class Quiz():
    def __init_(self):
        return

    def __init__(self, quiz_name):
        self.quiz_name = quiz_name
        self.question_map = {}

    def add_question(self, question_text, answer_list, preserve_answer_order, question_number):
        if self.should_reject_question(question_text, answer_list, question_number):
            return False

        new_question = Question.Question(preserve_answer_order)
        new_question.question_text = question_text
        new_question.question_number = question_number

        answer_index = 1
        for answer_text in answer_list:
            curr_encoding = ascii_uppercase[answer_index - 1]
            new_question.add_answer(answer_text, str(curr_encoding))
            answer_index += 1

        self.question_map[question_number] = new_question

        return True

    def add_constructed_question(self, constructed_question):
        if self.should_reject_question(constructed_question.question_text, constructed_question.answer_map,
                                       constructed_question.question_number):
            return False

        self.question_map[constructed_question.question_number] = constructed_question

        return True

    def question_number_exists(self, question_number):
        return question_number in self.question_map

    def should_reject_question(self, question_text, answer_list, question_number):
        if len(question_text) == 0 or len(answer_list) == 0 or self.question_number_exists(question_number):
            return True

        return False