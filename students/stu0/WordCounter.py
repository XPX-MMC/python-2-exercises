class WordCounter:

    def __init__(self, sentence):
        self._word_count = 0
        self._longest_word_len = 0
        self._shortest_word_len = 0
        self._sentence = sentence

    def count_words(self):
        word_list = self._sentence.split(" ")
        self._word_count = len(word_list)
        self._shortest_word_len = len(min(word_list, key=len))
        self._longest_word_len = len(max(word_list, key=len))
        pass

    def get_longest_word(self):
        return self._longest_word_len

    def get_shortest_word(self):
        return self._shortest_word_len

    def get_word_count(self):
        return self._word_count
