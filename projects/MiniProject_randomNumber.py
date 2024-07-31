import random

class Game:
    def __init__(self, number):
        self.number = number

    def randomNumber(self):
        rand = random.randint(0, 100)
        print(rand)
        return rand

    def takeInput(self):
        return int(input("guess the number: "))

    def checker(self, n, rando):
        while n != rando:
            if n > rando:
                print("The number is bigger")
            elif n < rando:
                print("The number is smaller")
            n = self.takeInput()
        print("The number is found")

n = int(input("Enter any number: "))
g1 = Game(n)
rand = g1.randomNumber()
g1.checker(n, rand)