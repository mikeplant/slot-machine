from textwrap import dedent

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
        print(dedent("""
            Hit 'return' to pull the lever or type 'quit' to leave.       
            """
        ))

    def print_result(self, results, state, player):
        print(dedent(f"""
                  --|| {results[0]} || {results[1]} || {results[2]} ||--

                  {state["type"]}

                  Prize: £{state["prize"]}
                  You now have: £{player.get_money()}
              """))
        
    def print_gameover(self, string):
        print(string)
        