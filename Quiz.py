import Question
import Answer
from string import ascii_lowercase

class Quiz():
    def __init_(self):
        return

    def __init__(self, quiz_name):
        self.quiz_name = quiz_name
        self.question_list = []

    def add_question(self, question_text, answer_list, preserve_answer_order):
        if len(question_text) == 0 or len(answer_list) == 0:
            return False
        new_question = Question.Question(preserve_answer_order)
        new_question.question_text = question_text

        answer_index = 1
        for answer_text in answer_list:
            curr_encoding = ascii_lowercase[answer_index - 1]
            new_question.add_answer(answer_text, str(curr_encoding))
            answer_index += 1

        self.question_list.append(new_question)
        return True