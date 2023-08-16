from textwrap import dedent

from player import Player
from machine import Machine

class Game():
    def __init__(self, player, machine):
        self.player = player
        self.machine = machine
        self.start()

    def start(self):
        print(dedent("""
            Welcome to the One-Armed Bastard!
                   _____________  
                  
                  ---------------  _
                  | £ || £ || £ | ( )
                  | 7 || 7 || 7 | //
                  | $ || $ || $ | ||
                  --------------- ||
                  _______________//
            
            Type 'pull' to pull the lever or 'quit' to leave.       
            """
        ))

        response = input("> ")

        if response.lower() == 'pull':
            self.play()
        else:
            exit(0)


    def show_result(self, results):
        print(dedent(f"""
                  --|| {results[0]} || {results[1]} || {results[2]} ||--
              """))


    def play(self):
        # check player has money
        if self.player.get_money() <= 0:
            # game_over(LOSE)
            pass
        
        # check machine has money
        if self.machine.get_money() <= 0:
            # game_over(WIN)
            pass

        self.player.reduce_money(1)
        self.machine.increase_money(1)

        # Results
        results = self.machine.get_symbols()
        # print results
        self.show_result(results)

          #if win:
        if machine.check_for_win(results):
            print("Winner!")
            #player.increase_money()
        else:
            print("Not this time :(")
        # print player money
        pass


player = Player(10)
machine = Machine(300)
game = Game(player, machine)

# game.play()