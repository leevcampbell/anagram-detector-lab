

class Anagram:

    def __init__(self, word):
        self.word = word.lower()
        self.word_sorted = sorted(self.word)

    def match(self, words):
        return [word for word in words if self.is_anagram(word)]

    def is_anagram(self, word):
        word = word.lower()
        return word != self.word and sorted(word) == self.word_sorted