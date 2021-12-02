from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

for x in question_data:
    question_bank.append(Question(x["text"], x["answer"]))
    # print(x)

# print(question_bank[4].answer)

quizzer = QuizBrain(question_bank)

while quizzer.still_has_questions():
    quizzer.next_question()
print("you've completed the quiz!")
print(f"you scored: {quizzer.score}/{quizzer.question_number}")
