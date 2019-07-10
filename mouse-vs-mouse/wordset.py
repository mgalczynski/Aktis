from common import filter_dots

class WordSet:
    def __init__(self, words):
        self._words = set(word.strip().lower() for word in words)

    def count_occurrences(self, sentence):
        occurences = 0

        for word in filter_dots(sentence.strip()).split():
            if word.lower() in self._words:
                occurences += 1

        return occurences
