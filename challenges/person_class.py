class Person():
    def __init__(self, name):
        self.name = name
    def talk(self):
        print(f"Hi! i am {self.name}")


p1 = Person("Ziauddin")
p1.talk()

p2 = Person("Barni")
p2.talk()