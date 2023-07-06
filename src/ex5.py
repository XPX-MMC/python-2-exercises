
class WordCounter:
    def __init__(self, sentence):
        self.sentence = sentence
    
    def count_words(self):
        word_list = self.sentence.split(' ')
        self.word_list = word_list

    
    def get_word_count(self):
        return len(self.word_list)
    
    def get_shortest_word(self):
        min = self.word_list[0]
        for word in self.word_list:
            if len(word) < len(min):
                min = word
        return len(min)
    
    def get_longest_word(self):
        max = self.word_list[0]
        for word in self.word_list:
            if len(word) > len(max):
                max = word
        return len(max)

sentence = "This is a test of the emergency broadcast system"
word_counter = WordCounter(sentence)
word_counter.count_words()
print(word_counter.get_word_count())    # Returns the number of all the words.
print(word_counter.get_shortest_word()) # Returns the length of the shortest word.
print(word_counter.get_longest_word())  # Returns the length of the longest word.