class Person:
    def __init__(self, name, id):
        self.name = name
        self.id = id

# Creating Person class with my  name and ID
p1 = Person("Md. Shahin Miah", 5646)
print(p1.name)
print(p1.id)

class People:
    def __init__(self, name, id):
        self.name = name
        self.id = id
    
    def writing(self):
        print(f"Hey! I am {self.name}, id: {self.id}. Today's lab session")

mm = People('Md. Shahin Miah', 5646)
mm.writing()

class Encap:
    def __init__(self):
        # protected number
        self._a = 58
        # private number
        self.__b = 74

e = Encap()
print(e._a)  # Accessing protected attribute
#print(e.__b)  # This will show  an error because __b is private
