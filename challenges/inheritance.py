class Mammals():
    def walk(self):
        print("walk")
    
class Dog(Mammals):
    def bark(self):
        print("bark")

class Cat(Mammals):
    pass

c1 = Cat()
c1.walk()

d1 = Dog()
d1.walk()
d1.bark()
