from GuessGame import GuessGame
from MemoryGame import MemoryGame
from CurrencyRouletteGame import CurrencyRouletteGame

def load_game():
    print("Starting load_game function")
    game_choice = int(input("Choose a game to play:\n1. Guess Game\n2. Memory Game\n3. Currency Roulette\n"))
    difficulty = int(input("Choose difficulty level (1-5): "))

    if game_choice == 1:
        print("Starting Guess Game")
        game = GuessGame(difficulty)
    elif game_choice == 2:
        print("Starting Memory Game")
        game = MemoryGame(difficulty)
    elif game_choice == 3:
        print("Starting Currency Roulette")
        game = CurrencyRouletteGame(difficulty)
    else:
        print("Invalid choice")
        return

    print("Playing the game")
    result = game.play()
    print("You won!" if result else "You lost!")

load_game()
