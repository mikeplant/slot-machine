import random

class Machine():
    def __init__(self, money):
        self.money = money
        self.reel = ['0', '?', '8', '£', '7', '$']

    def play(self):
        # get 3 random symbols from self.reel
        self.get_symbols()

        # check if win

    
    def get_symbols(self):
        symbols = []

        for i in range(0,3):
            symbols.append(random.choice(self.reel))

        return symbols
    
    def check_for_win(self, symbols):
        winning_combos = [
            (symbols[0] == symbols[1] and symbols[0] == symbols[2])
        ]

        if winning_combos[0]:
            return True
        else:
            return False
    
    def get_money(self):
        return self.money
    
    def increase_money(self, amount):
        self.money += amount