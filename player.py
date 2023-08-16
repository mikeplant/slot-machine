class Player():
    def __init__(self, money):
        self.money = money

    def get_money(self):
        return self.money
    
    def reduce_money(self, amount):
        self.money -= amount