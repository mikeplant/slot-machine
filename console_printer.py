from textwrap import dedent

from colorist import bg_yellow, bg_green, bg_red, Color

class ConsolePrinter():
    def welcome(self, player):
        print(dedent(f"""
            Welcome to the One-Armed Bastard!
                   _____________  
                  
                  ---------------  _
                  | £ || £ || £ | ( )
                  | 7 || 7 || 7 | //
                  | $ || $ || $ | ||
                  --------------- ||
                  _______________//
                     
            Match 2 or more symbols to win!
                     
            You have: £{player.get_money()}
            """
        ))

    def play(self):
        print(dedent(f"""
            Hit {Color.GREEN}'return'{Color.OFF} to pull the lever or type {Color.RED}'quit'{Color.OFF} to leave.       
            """
        ))

    def print_result(self, results, state, player):
        print(dedent(f"""
                     
            --|| {results[0]} || {results[1]} || {results[2]} ||--
            
            """ ))
        
        if state["type"] == "JACKPOT":
            bg_yellow("  JACKPOT!  ")

        elif state["type"] == "WIN":
            bg_green("  WIN  ")

        else:
            bg_red("  LOSE  ")
        
        print("\n")
        
        if state["type"] != "LOSE":
            print(f"Prize: £{state['prize']}")

        print(f"You now have: £{player.get_money()}\n")
        print("-" * 50)
        
    def print_gameover(self, string):
        print(string)
        