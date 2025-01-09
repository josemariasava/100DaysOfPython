from  question_model import Question
from data import question_data
from quiz_brain import QuizzBrain


#creating the question bank - list of Question() objects
question_bank = []

# Iterate question_data list 
for q in question_data:
    q_text = q["text"] # access text key for each dict item inside the question_data list 
    q_answer = q["answer"]# access answer key for each dict item inside the question_data list 
    question_obj = Question(q_text,q_answer) # Create for each step of the loop an object of class Question() 

    question_bank.append(question_obj) # Append each of theese question object inside the list question_bank

quiz = QuizzBrain(question_bank)


while quiz.still_has_question():
    quiz.next_question()

# print(question_bank[0].text) # print the text attribute of the object question with index 0 inside the question_bank list 
# print(question_bank[0].answer) # print the answer attribute of the object question with index 0 inside the question_bank list 
print(f"Your final score was: {quiz.score}\{quiz.question_number}")
print("#### Game finish! ####")
