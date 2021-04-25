"""
Palindrome class realization.
"""

from arraystack import ArrayStack

class Palindrome:
    """Class for palindrome searching."""

    @staticmethod
    def read_file(filename: str):
        """Reads the file and returns a list of words in it."""
        words = []
        with open(filename, 'r', encoding='utf-8') as words_file:
            for line in words_file:
                words.append(line.split()[0])
        return words


    @staticmethod
    def write_to_file(word: str, filename: str):
        """Writes a word to the file."""
        with open(filename, 'a', encoding='utf-8') as new_f:
            new_f.write(f'{word}\n')


    @staticmethod
    def check_palindrome(word):
        """Returns True if the word is palindrome and False otherwise."""
        stack_word = ArrayStack()
        for letter in word:
            stack_word.push(letter)
        reversed_word = ''
        for _ in range(len(stack_word)):
            reversed_word += stack_word.pop()
        return word == reversed_word


    def find_palindromes(self, word_file: str, palindrome_file: str):
        """Searches for palindromes from the file with word list and writes them to a file."""
        all_words = self.read_file(word_file)
        palindromes = []
        for word in all_words:
            if self.check_palindrome(word):
                self.write_to_file(word, palindrome_file)
                palindromes.append(word)
        return palindromes
