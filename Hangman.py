import requests
import random


class Hangman:
    WRONG_GUESSES = 0

    def __init__(self, user_name):
        self.user_name = user_name


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

        return ''.join(list(blanks_lst))
    

    def game(self):
        chances = 0

        generated_word = self.generate_word()
        blanked_word = self.replace_word_with_blank_lines(generated_word)
        blank_word_to_display = ' '. join(list(blanked_word))

        print(f"Your word has {len(blanked_word)} characters: {blank_word_to_display}")

        while chances <= 7:
            user_guess = self.get_user_guess()
            blanked_word = self.check_letter_guess_with_word(user_guess, generated_word, blanked_word)

            if user_guess not in blanked_word and self.WRONG_GUESSES < 7:
                print(f'It\'s not the "{user_guess}"! Try again! \n {self.draw_hanged_man(self.WRONG_GUESSES)}')
                chances += 1
                self.WRONG_GUESSES += 1
            elif self.WRONG_GUESSES <= 7:
                print(f"{self.user_name} you lost! The word was: {generated_word}")
                chances = 7
            elif blanked_word == generated_word:
                print(f'Congratulations {self.user_name} you guessed the word "{generated_word}" and you won!')
                chances = 7
            else:
                print(f"Word: {blanked_word}")
            

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
    hangman = Hangman('Kamil')
    hangman.game()
