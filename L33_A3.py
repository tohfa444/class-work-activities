import random

class FruitQuiz:
    
    def __init__(self):
        
        self.fruits = {
            'apple': 'red',
            'orange': 'orange',
            'watermelon': 'green',
            'banana': 'yellow'
        }

    
    def quiz(self):
        while True:
            fruit, color = random.choice(list(self.fruits.items()))

            print(f"What is the color of {fruit}?")
            user_answer = input("Your answer: ")

            if user_answer.lower() == color:
                print("Correct answer ")
            else:
                print("Wrong answer ")

            option = int(input("Enter 0 to quit, or 1 to play again: "))
            if option == 0:
                break


print("Welcome to Fruit Quiz ")
fq = FruitQuiz()
fq.quiz()