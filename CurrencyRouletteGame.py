import random
import requests

class CurrencyRouletteGame:
    def __init__(self, difficulty):
        self.difficulty = difficulty
        self.correct_value = None

    def get_money_interval(self):
        response = requests.get("https://api.exchangerate-api.com/v4/latest/USD")
        data = response.json()
        exchange_rate = data["rates"]["ILS"]
        value = random.randint(1, 100)
        lower_bound = value - (5 - self.difficulty)
        upper_bound = value + (5 - self.difficulty)
        return lower_bound * exchange_rate, upper_bound * exchange_rate

    def get_guess_from_user(self):
        return float(input("Guess the value in ILS: "))

    def play(self):
        interval = self.get_money_interval()
        guess = self.get_guess_from_user()
        return interval[0] <= guess <= interval[1]
