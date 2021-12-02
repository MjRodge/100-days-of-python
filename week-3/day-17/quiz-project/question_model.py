class Question:
    def __init__(self, question, answer):
        self.question = question
        self.answer = answer


new_question = Question("what's the question?", "answer")

print(new_question.answer)
