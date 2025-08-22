class India:

    def capital(self):
        print("India's capital is noya Dhilli")
    
    def language(self):
        print("Hindi is the most spoken language in india")

    def type(self):
        print("India is a developing country")
        
class USA:

    def capital(self):
        print("USA's capital is Washington, D.C.")
    
    def language(self):
        print("English is the primary language of USA")

    def type(self):
        print("USA is a developped country")
        
obj_india = India()
obj_usa = USA()

for country in (obj_india,obj_usa):
    country.capital()
    country.language()
    country.type()
