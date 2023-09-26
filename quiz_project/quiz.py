from question_data import question_data
from question_model import Question

question_bank = []
for question in question_data:
    question_text = question["text"]
    question_answer = question["answer"]
    new_question = Question(q_text=question_text, q_answer=question_answer)    
    question_bank.append(new_question)

print(question_bank)
