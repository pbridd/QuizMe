import Answer
import Question
import Quiz
import xml.etree.ElementTree as ET


def xml_to_answer(xml_answer):
    answer_result = Answer.Answer()
    answer_result.answer_text = xml_answer.find("text").text
    answer_result.set_one_char_encoding(xml_answer.find("encoding").text)
    return answer_result


def xml_to_question(xml_question):
    question_result = Question.Question(True)
    question_result.question_text = xml_question.find("text").text
    question_result.question_number = int(xml_question.find("number").text, 10)

    xml_answers = xml_question.findall("answer")
    for xml_answer in xml_answers:
        question_result.add_constructed_answer(xml_to_answer(xml_answer))
    return question_result


def xml_to_quiz(xml_quiz):
    quiz_result = Quiz.Quiz(xml_quiz.find("text").text)
    xml_questions = xml_quiz.findall("question")
    for xml_question in xml_questions:
        quiz_result.add_constructed_question(xml_to_question(xml_question))
    return quiz_result
