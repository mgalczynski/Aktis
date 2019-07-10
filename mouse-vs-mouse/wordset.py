from common import filter_dots


class WordSet:
    """This class represents set with words that is used distinguishing the context of the sentence
    """

    def __init__(self, words):
        """
        :param words: list of words to initialize set
        """
        self._words = set(word.strip().lower() for word in words)

    def count_occurrences(self, sentence):
        """This method count occurrences of the word from the set given in :func:`~wordset.WordSet.__init__` method
        :param sentence: sentence that to run analyze
        :return: number of occurrences
        """
        occurences = 0

        for word in filter_dots(sentence.strip()).split():
            if word.lower() in self._words:
                occurences += 1

        return occurences
