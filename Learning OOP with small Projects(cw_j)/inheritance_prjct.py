""" Define a Python class named Animal with a constructor that takes five parameters: name, region, animal_type, color, and lethal. Inside the constructor, set the instance variables accordingly.
Implement a method in the Animal class named animal_bio() that prints the animal's name and type.
Create a subclass named Clinic which inherits from Animal.
In the Clinic class, define a method animal_bio() that prints a message indicating the animal's name and the region it's found in. """


class Animal:
    def __init__(self,name,region,animal_type,color,lethal):
        self.name = name 
        self.animal_type = animal_type
        self.color = color
        self.lethal = lethal
        self.region = region
    def animal_bio(self):
        print(f"Animal Name:{self.name} Animal type: {self.animal_type}")
        
        
class Clinic(Animal):
    def animal_bio(self):
        print(f'This is a {self.name} found in {self.region}')
        
    def search(self,animals):
        
        region = input('Enter a region Name ').lower()
        
        for animal in animals:
            if self.region==region:
                print(f'Species')
                
                

animals = []
animal_count = int(input('Enter how many animal in the list you want: '))
region_name =input('Enter a region : ')

for i in range(animal_count):
    animal_name =input('Enter a Animal Name: ')
    animals.append(animal_name)
    
animal_details = Clinic('Tiger',region_name,animal_type='Mengrove',color='white',lethal='Yes')
animal_details.search(animals)