def welcome(name):
    return f"Hello {name} and welcome to the World of Games (WoG).\nHere you can find many cool games to play."


def load_game():
    print("Please choose a game to play:")
    print("1. Memory Game - a sequence of numbers will appear for 1 second and you have to guess it back")
    print("2. Guess Game - guess a number and see if you chose like the computer")
    print("3. Currency Roulette - try and guess the value of a random amount of USD in ILS")

    game_choice = int(input("Enter the number of the game you want to play (1-3): "))
    while game_choice not in [1, 2, 3]:
        print("Invalid choice. Please choose again.")
        game_choice = int(input("Enter the number of the game you want to play (1-3): "))

    difficulty_level = int(input("Please choose game difficulty from 1 to 5: "))
    while difficulty_level not in [1, 2, 3, 4, 5]:
        print("Invalid difficulty level. Please choose again.")
        difficulty_level = int(input("Please choose game difficulty from 1 to 5: "))

    return game_choice, difficulty_level


# For testing purpose
if __name__ == "__main__":
    print(welcome("Guy"))
    load_game()
