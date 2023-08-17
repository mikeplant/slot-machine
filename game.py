from textwrap import dedent

from player import Player
from machine import Machine
from console_printer import ConsolePrinter

class Game():
    def __init__(self, player, machine, printer):
        self.player = player
        self.machine = machine
        self.printer = printer
        self.state = {"prize": 0, "type": "LOSE"}
        self.start()

    def start(self):
        self.printer.welcome(self.player)
        self.play()
  
    def reset_state(self):
        self.state["prize"] = 0
        self.state["type"] = "LOSE"

    def check_for_win(self, symbols):
        self.reset_state()

        win_conditions = [
            {
                "condition": (
                    symbols[0] == symbols[1] or 
                    symbols[1] == symbols[2] or
                    symbols[0] == symbols[2]
                    ),
                "prize": 2,
                "type": "WIN"
            },
            {
                "condition": (
                    symbols[0] == symbols[1] and 
                    symbols[0] == symbols[2]
                    ),
                "prize": 5,
                "type": "JACKPOT"
            }
        ]

        for cond in win_conditions:
            if cond["condition"]:
                self.state["prize"] = cond["prize"]
                self.state["type"] = cond["type"]
          
    def is_gameover(self):
        if self.player.get_money() <= 0 or self.machine.get_money() <= 0:
            return True
        else:
            return False

    def get_winning_message(self):
        if self.player.get_money() <= 0:
            return "You're out of cash! You lose."
        
        if self.machine.get_money() <= 0:
            return "You've drained the machine dry! You win."

    def play(self):
        while True:

            if self.is_gameover():
                self.printer.print_gameover(self.get_winning_message())
                exit(0)

            self.printer.play()

            response = input("> ")

            if response.lower() == 'quit':
                exit(0)

            self.player.reduce_money(1)
            self.machine.increase_money(1)

            results = self.machine.get_symbols()
            
            self.check_for_win(results)
            self.player.increase_money(self.state["prize"])
            self.printer.print_result(results, self.state, self.player)
        
        


player = Player(5)
machine = Machine(300)
printer = ConsolePrinter()
game = Game(player, machine, printer)