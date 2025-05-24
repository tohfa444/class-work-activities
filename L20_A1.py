import random
playing=True
number=random.randint(1,10)
print("I will generate a number from 1 to 10 and \nu also have to guess a number from 1 to 10")
while playing:
    guess=int(input("Enter a any guess from 1 to 10 :"))
    if number==guess:
        print("You win the game and the number was",guess)
        break
    else:
        print("Your guess is not currect try again")
