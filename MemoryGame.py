import random

class MemoryGame:
    def __init__(self, difficulty):
        self.difficulty = difficulty
        self.sequence = None

    def generate_sequence(self):
        self.sequence = [random.randint(1, 101) for _ in range(self.difficulty)]
        print("Memorize this sequence:", self.sequence)
        # Add code to display sequence for 0.7 seconds

    def get_list_from_user(self):
        print("Now enter the sequence:")
        return [int(input()) for _ in range(self.difficulty)]

    def is_list_equal(self, user_list):
        return user_list == self.sequence

    def play(self):
        self.generate_sequence()
        user_sequence = self.get_list_from_user()
        return self.is_list_equal(user_sequence)
