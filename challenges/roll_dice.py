import random


dice1 = random.randint(0, 6)
dice2 = random.randint(0, 6)
result = [random.randint(0, 6), random.randint(0, 6)]   # convert to list
#print(result)


#OR Using class and function
class Dice:
    def roll(self):
        output = random.randint(1,6), random.randint(1,6)
                
        return output
        
Dice1 = Dice()
print(Dice1.roll())
   







