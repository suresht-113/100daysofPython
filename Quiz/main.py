from question_model import Question
from data import question_data
from quiz_brain import Quizbrain

question_bank =[]
for qd in question_data:
    que_text= qd["text"]
    que_ans = qd["answer"]
    newq = Question(que_text,que_ans)
    question_bank.append(newq)

quiz = Quizbrain(question_bank)
while quiz.still_has_questions():
    quiz.next_question()

print("You've completed the quiz")
print(f"your final score was: {quiz.score}/{quiz.question_number}")