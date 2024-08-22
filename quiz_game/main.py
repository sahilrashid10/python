from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for question in question_data:
    new_question = Question(question["text"], question["answer"])  # this new_question is same as current_question in
    question_bank.append(new_question)  # quiz_brain.py

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    ans = quiz.next_question()

print("You have completed the quiz")
print(f"Your final score is {quiz.score}/{quiz.question_no}")

# you can add more variety of questions from Trivia database
