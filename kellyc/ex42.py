# Is-A, Has-A, Objects, and class_names

# Class Animal is-a class of type object
## In Python3, it's recommended (to be explicit) but not necessary to put object after name of class

class Animal(object):
    pass

# Dog is a class of Animal
class Dog(Animal):

    def __init__(self, name):
        # this class has a name
        self.name = name

# Cat is a class of Animal
class Cat(Animal):

    def __init__(self, name):
        # this class has a name
        self.name = name

# The class Person is a thing, man....
class Person(object):

    def __init__(self, name):
        # this class has a name
        self.name = name

# ?
class Person(object):

    def __init__(self, name):
        # tthis class has a name
        self.name = name

        # Person has a pet and value until set otherwise is None
        self.pet = None

# Employee is a class of Person
class Employee(Person):

    def __init__(self, name, salary):
        #
        super(Employee, self).__init__(name)
        # salary is married to self, they meld together and emerge out of pelting rice-rain with the name salary
        self.salary = salary

# Fish is now a class. Announcement over.
class Fish(object):
    pass

#  Salmon is a class of fish
class Salmon(Fish):s
    pass

# Halibut is a class of fish
class Halibut(Fish):
    pass

# Ruffles is an instance of the class Dog
ruffles = Dog("Ruffles")

# Urchin is an instance of the class cat
urchin = Cat("Urchin")

# Mary is an instance of the class Person
mary = Person("Mary")

# Frank is an instance of the class Person
frank = Person("Frank")

# Mary has a pet Satan
mary.pet = satan

# Frank is an instance of the class employee with number 120000
frank = Employee("Frank", 120000)

# Frank has-a pet, Ruffles
frank.pet = ruffles

# Flipper is a Fish
flipper = Fish()

# Crouse is a Salmon
crouse = Salmon()

# Harry is a Halibut
harry = Halibut()
