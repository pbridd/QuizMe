
class Answer():
    def __init__(self):
        self.answer_text = ""
        self.answer_encoding = ""
        return

    def set_one_char_encoding(self, answer_encoding):
        if len(answer_encoding) != 1:
            return False
        self.answer_encoding = answer_encoding
        return True