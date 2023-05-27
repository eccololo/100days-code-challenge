class QuizBrain:

    def __init__(self, question_list):
        self.question_number = 0
        self.score = 0
        self.question_list = question_list

    def next_question(self):
        current_question = self.question_list[self.question_number]
        question_text = current_question.text
        question_answer = current_question.answer
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number}: {question_text} (True/False): ")
        self.check_answer(user_answer, question_answer)

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            print("You got it right. Great job!")
            self.score += 1
        else:
            print("You got it wrong. Sorry!")
        print(f"Your current score is: {self.score}/{self.question_number}.")
        print(f"The correct answer is: {correct_answer}.")
        print("\n")
