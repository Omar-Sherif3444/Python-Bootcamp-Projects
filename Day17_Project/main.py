from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

for question in question_data:
    question_text = question["text"]
    question_answer = question["answer"]
    newQ = Question(question_text, question_answer)
    question_bank.append(newQ)

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.NextQuestion()

print("You have completed the quiz")
print(f"Your Score is {quiz.user_score}/{quiz.question_number}")