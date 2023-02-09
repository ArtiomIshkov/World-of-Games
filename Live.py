
def get_user_name():
    name = input("Please enter your name: ")
    print("Hello", name, "and welcome to the World of Games (WoG).\n Here you can find many cool games to play")


def load_game():
    while True:
        try:
            number = int(input("Please choose a game from 1 to 3:\n1. Memory Game\n2. Guess Game\n"
                               "3. Currency Roulette\n-> "))
            if number == 1:
                game1()
                break
            elif number == 2:
                game2()
                break
            elif number == 3:
                game3()
                break
        except ValueError:
            print("Error! please enter a valid number.")


def game1():
    print("Memory Game - a sequence of numbers will appear for 1 second and you have to guess it back")
    from MemoryGame import play_Memory_Game
    play_Memory_Game()

def game2():
    print("Guess Game - guess a number and see if you choose like the computer")
    from GuessGame import play_guess_game
    play_guess_game()

def game3():
    print("Currency Roulette - try and guess the value of a random amount of USD in ILS")
#end
