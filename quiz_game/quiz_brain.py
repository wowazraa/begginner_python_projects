from data import question_data

class QuizBrain:
    def __init__(self, question_list):
        self.question_list = question_list
        self.question_number = 0
        self.score = 0

    def next_question(self):
        current_question = self.question_list[self.question_number]
        user_answer = input(f"Q{self.question_number + 1}: {current_question.text} (True/False)?: ")
        self.check_answer(user_answer)
        self.question_number += 1

    def still_has_questions(self):
        return self.question_number < len(question_data)

    def check_answer(self, user_answer):
        if user_answer.lower() == question_data[self.question_number]["answer"].lower():
            print("You got it right!")
            self.score += 1

        else:
            print("That's wrong.")
            print(f"The correct answer is {question_data[self.question_number]["answer"]}")

        print(f"Your current score is: {self.score}/{self.question_number + 1}")
        print('\n')
