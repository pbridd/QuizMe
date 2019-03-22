import Answer


class Question:

    def __init__(self):
        self.init_question(False)

    def __init__(self, preserve_answer_order):
        self.init_question(preserve_answer_order)

    def add_answer(self, answer_text, answer_encoding):
        new_answer = Answer.Answer()
        new_answer.answer_text = answer_text
        if not new_answer.set_one_char_encoding(answer_encoding) or self.answer_encoding_exists(answer_encoding):
            return False
        self.answer_map[answer_encoding] = new_answer
        self.answer_order.append(answer_encoding)
        return True

    def add_constructed_answer(self, answer):
        answer_encoding = answer.answer_encoding
        if self.answer_encoding_exists(answer_encoding):
            return False
        self.answer_map[answer_encoding] = answer
        self.answer_order.append(answer_encoding)
        return True

    def get_answer_list(self):
        output_list = []
        if self.preserve_answer_order:
            for encoding in self.answer_order:
                output_list.append(self.answer_map[encoding])
        else:
            for encoding in self.answer_map:
                output_list.append(self.answer_map[encoding])
        return output_list

    def answer_encoding_exists(self, encoding):
        if encoding in self.answer_map:
            return True
        else:
            return False

    def init_question(self, preserve_answer_order):
        self.question_text = ""
        self.answer_map = {}
        self.preserve_answer_order = preserve_answer_order
        self.answer_order = []
        self.question_number = -1


