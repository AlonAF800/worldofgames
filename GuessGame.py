import random

class GuessGame:
    def __init__(self, difficulty):
        self.difficulty = difficulty
        self.secret_number = None

    def generate_number(self):
        self.secret_number = random.randint(1, self.difficulty)

    def get_guess_from_user(self):
        return int(input(f"Guess a number between 1 and {self.difficulty}: "))

    def compare_results(self, guess):
        return guess == self.secret_number

    def play(self):
        self.generate_number()
        guess = self.get_guess_from_user()
        return self.compare_results(guess)
