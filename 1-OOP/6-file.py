import random

class Game:
    def __init__(self, secret_number, max_guesses):
        self.secret_number = secret_number
        self.max_guesses = max_guesses
        self.num_guesses = 0

    def guess(self, n):
        self.num_guesses += 1
        return n == self.secret_number

    def game_over(self):
        return self.num_guesses >= self.max_guesses or self.guess(self.secret_number)

class Player:
    def __init__(self, name):
        self.name = name
        self.score = 0

    def play(self, game):
        while not game.game_over():
            guess = int(input(f"{self.name}, enter your guess (1 - 10): "))
            if game.guess(guess):
                print("Correct")
                self.score += 1
                break
            else:
                print("Incorrect, try again.")
        if game.game_over():
            print(f"Congratulaions, {self.name}")