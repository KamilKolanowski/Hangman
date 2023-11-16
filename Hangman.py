import requests
import random


class Hangman:
    WRONG_GUESSES = 0

    def __init__(self):
        pass


    def replace_word_with_blank_lines(self, word):
        replaced_word = ''
        generated_word = word
        for _ in generated_word:
            replaced_word += '_'

        return replaced_word


    def check_letter_guess_with_word(self, letter, word, blank_chars):
        word_lst = list(word)
        blanks_lst = list(blank_chars)

        for idx, _ in enumerate(word_lst):
            if letter in word_lst[idx]:
                blanks_lst[idx] = letter
            else:
                self.WRONG_GUESSES += 1

        return ''.join(list(blanks_lst))
    

    def game(self):
        chances = 0
        generated_word = self.generate_word()
        blanked_word = self.replace_word_with_blank_lines(generated_word)
        print(f"Generated word: {generated_word}")

        while chances <= len(generated_word) :
            user_guess = self.get_user_guess()
            blanked_word = self.check_letter_guess_with_word(user_guess, generated_word, blanked_word)
            print(blanked_word)
            if user_guess not in blanked_word:
                print(f"It's not the '{user_guess}'! Try again! \n {self.draw_hanged_man(chances)}")
                chances += 1

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


if __name__ == '__main__':
    chances = 0
    hangman = Hangman()

    hangman.game()
    # while chances < 5:
    #     print(hangman.check_letter_guess_with_word())
