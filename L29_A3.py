class person:

    def __init__(self,name,ID_number):
        self.name=name
        self.ID_number=ID_number

    def display(self):
        print(self.name)
        print(self.ID_number)

class employee(person):

    def __init__(self,name,ID_number,salary,post):
        self.salary=salary
        self.post=post

        person.__init__(self,name,ID_number)
    
a = employee("MD Mamun",185,20000,"Intern")

a.display()