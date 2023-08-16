import random

class Machine():
    def __init__(self, money):
        self.money = money
        self.reel = ['0', '#', '!', '£', '7', '$']

    def play(self):
        # get 3 random symbols from self.reel
        
        # print symbols to console
        # check if win
        pass
    
    def get_symbols(self):
        symbols = []

        for i in range(0,3):
            symbols.append(random.choice(self.reel))

        return symbols
    
    def get_money(self):
        return self.money
    
    def increase_money(self, amount):
        self.money += amount