from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

for q in range(0, len(question_data)):
    question_bank.append(Question(question_data[q]["text"], question_data[q]["answer"]))

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print("You completed the quiz.")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")
