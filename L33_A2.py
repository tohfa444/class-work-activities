class Flashcard:
    def __init__(self, word, meaning):
        self.word = word
        self.meaning = meaning

    def __str__(self):
        
        return self.word + ' ( ' + self.meaning + ' ) '


flash = []
print("Welcome to Flashcard Application ")


while True:
    word = input("Enter the word you want to add to flashcard: ")
    meaning = input("Enter the meaning of the word: ")

    obj = Flashcard(word, meaning)
    flash.append(obj)

    option = int(input("Enter 1 to stop, or 0 to add another flashcard: "))
    if option == 1:
        break


print("\nYour Flashcards:")
for i in flash:
    print(">", i)