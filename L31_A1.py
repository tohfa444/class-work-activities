class myclass:

    __privatevar = 27

    def __priveMeth(self):
        print("I am inside class myclass")

    def hello(self):
        print("Private varialble's value:",myclass.__privatevar)

foo = myclass()
foo.hello()
foo.__priveMeth()