"""Word Finder: finds random words from a dictionary."""
import random

class WordFinder:
    ...
    def __init__(self, filepath):
        """Reads words and report amount of words read"""
        self.filepath = filepath
        self.file = open(self.filepath, 'r')
        self.lst = self.words_list()
        
        print(f'{len(self.lst)} words read')

    
    def words_list(self):  
        """Creates words list"""  

        return [line.strip() for line in self.file]
        
    def random(self):
        """REturns random word from list"""

        return random.choice(self.lst)

class SpecialWordFinder(WordFinder):

    def words_list(self):  
        """Creates words list filtering out empty lines and comments"""  
        
        return [line.strip() for line in self.file if len(line) > 1 and not line.startswith('#')]

