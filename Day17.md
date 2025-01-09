### Class Examples

**attributes** → what object has 

**methods** → what object does { methods are function, but inside a class takes the method name } 

```python
# Name of the class is in PascalCase 
class User: 

    # Constructor of our function - called any tyme an object of this class is created
    def __init__(self, username, user_id): 
        self.username = username # attribute initialized
        self.id = user_id # attribute initialized
        self.followers = 0 # is an attribute but not in the constructor, so when the object is initialized is not necessary to pass this attribute
        self.following = 0

    def follow(self,user): # self as first parameter, in this way the method knows wich object that called it 
        user.followers += 1 # this its done to the user given as argument
    
        self.following += 1 # this affects the object itself

# Name of the function in camelCase
def myFunction():
    pass # no method or content for the moment

var_one = 1 # Name of the var in snake_case 

user_one = User("Pippo","001")
user_two = User("Angela", "002")

user_one.follow(user_two)

print(f"User {user_one.id} followers: {user_one.followers} \nUser one following: {user_one.following}")
print(f"User {user_two.id} followers: {user_two.followers} \nUser one following: {user_two.following}")
```

---
### Quizz Game

**Data.py**

```python
question_data = [
    {"text": "A slug's blood is green.", "answer": "True"},
    {"text": "The loudest animal is the African Elephant.", "answer": "False"},
    {"text": "Approximately one quarter of human bones are in the feet.", "answer": "True"},
    {"text": "The total surface area of a human lungs is the size of a football pitch.", "answer": "True"},
    {"text": "In West Virginia, USA, if you accidentally hit an animal with your car, you are free to take it home to eat.", "answer": "True"},
    {"text": "In London, UK, if you happen to die in the House of Parliament, you are entitled to a state funeral.", "answer": "False"},
    {"text": "It is illegal to pee in the Ocean in Portugal.", "answer": "True"},
    {"text": "You can lead a cow down stairs but not up stairs.", "answer": "False"},
    {"text": "Google was originally called 'Backrub'.", "answer": "True"},
    {"text": "Buzz Aldrin's mother's maiden name was 'Moon'.", "answer": "True"},
    {"text": "No piece of square dry paper can be folded in half more than 7 times.", "answer": "False"},
    {"text": "A few ounces of chocolate can to kill a small dog.", "answer": "True"}
]
```

**question_model.py**

```python
class Question():
    """Question class - construct the question object to be added in the game"""

    def __init__(self,text:str,answer:str):
        self.text = text
        self.answer = answer 
```

**quiz_brain.py**

```python
class QuizzBrain():

    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
        self.score = 0 

    def still_has_question(self):
        if self.question_number < len(self.question_list):
            return True
        else: 
            return False

    def next_question(self): 
        current_question = self.question_list[self.question_number]
        self.question_number += 1 
        user_answer = input(f"Q.N. :{self.question_number} -> {current_question.text} (True/False): ")

        self.check_answer(user_answer, current_question.answer)

    def check_answer(self, user_answer, correct_answer): 
        if user_answer.lower() == correct_answer.lower(): 
            print("You got it right!")
            self.score += 1

        else: 
            print("That's wrong. ")
            self.score -= 1 

        print(f"The correct answer was: {correct_answer}. ")
        print(f"Your score is : {self.score}/{self.question_number}")
```

**main.py**

```python
class QuizzBrain():

    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
        self.score = 0 

    def still_has_question(self):
        if self.question_number < len(self.question_list):
            return True
        else: 
            return False

    def next_question(self): 
        current_question = self.question_list[self.question_number]
        self.question_number += 1 
        user_answer = input(f"Q.N. :{self.question_number} -> {current_question.text} (True/False): ")

        self.check_answer(user_answer, current_question.answer)

    def check_answer(self, user_answer, correct_answer): 
        if user_answer.lower() == correct_answer.lower(): 
            print("You got it right!")
            self.score += 1

        else: 
            print("That's wrong. ")
            self.score -= 1 

        print(f"The correct answer was: {correct_answer}. ")
        print(f"Your score is : {self.score}/{self.question_number}")
```