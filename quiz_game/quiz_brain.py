
class QuizBrain:
    def __init__(self, q_question_list):
        self.question_no = 0
        self.score = 0
        self.question_list = q_question_list

    def next_question(self):
        current_question = self.question_list[self.question_no]
        self.question_no += 1
        user_answer = input(f"Q.{self.question_no}:{current_question.text} (True/False) ?")
        print("\n"*5)
        self.check_answer(user_answer, current_question.answer)

    def still_has_questions(self):
        return self.question_no < len(self.question_list)

    def check_answer(self, user_answer, correct_ans):
        if user_answer.lower() == correct_ans.lower():
            self.score += 1
            print(f" You got it right!!! 👾")
        else:
            print("You got it wrong!!! 🧟‍♂️️")
        print(f"correct answer: {correct_ans}")
        print(f"Your score is : {self.score}/{self.question_no}")
