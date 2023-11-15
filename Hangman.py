import requests
import random


class Hangman:
    WRONG_GUESSES = 0

    def __init__(self):
        pass

    def replace_word_with_blank_lines(self):
        replaced_word = ''
        generated_word = self.generate_word()
        for _ in generated_word:
            replaced_word += '_'

        return [replaced_word, generated_word]

    def check_letter_guess_with_word(self):
        user_guess = self.get_user_guess()
        words_guess = self.replace_word_with_blank_lines()
        replaced_word_lst = list(words_guess[1])
        chars_to_replace = list(words_guess[0])

        for idx, _ in enumerate(replaced_word_lst):
            if user_guess in replaced_word_lst[idx]:
                chars_to_replace[idx] = user_guess
            else:
                self.WRONG_GUESSES += 1

        return ''.join(chars_to_replace)

    @staticmethod
    def generate_word():
        word_site = 'https://www.mit.edu/~ecprice/wordlist.10000'
        response = requests.get(word_site)
        words = response.content.splitlines()

        return random.choice(words).decode('utf-8')

    @staticmethod
    def get_user_guess():
        guess = input('Guess the letter: ')
        return guess

    @staticmethod
    def draw_hanged_man(wrong_guesses):
        hanged_man = [
            """
              -----
              |   |
                  |
                  |
                  |
                  |
                  |
                  |
                  |
                  |
            -------
            """,
            """
              -----
              |   |
              O   |
                  |
                  |
                  |
                  |
                  |
                  |
                  |
            -------
            """,
            """
              -----
              |   |
              O   |
             ---  |
              |   |
              |   |
                  |
                  |
                  |
                  |
            -------
            """,
            """
              -----
              |   |
              O   |
             ---  |
            / |   |
              |   |
                  |
                  |
                  |
                  |
            -------
            """,
            """
              -----
              |   |
              O   |
             ---  |
            / | \ |
              |   |
                  |
                  |
                  |
                  |
            -------
            """,
            """
              -----
              |   |
              O   |
             ---  |
            / | \ |
              |   |
             ---  |
            /     |
            |     |
                  |
            -------
            """,
            """
              -----
              |   |
              O   |
             ---  |
            / | \ |
              |   |
             ---  |
            /   \ |
            |   | |
                  |
            -------
            """,
            ]

        return hanged_man[wrong_guesses]


hangman = Hangman()

print(hangman.check_letter_guess_with_word())
