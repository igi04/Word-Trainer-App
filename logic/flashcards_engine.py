import random

#Main engine of flashcards work
class FlashcardEngine:
    def __init__(self, word_dict, learning_mode):
        self.all_words = word_dict.copy()
        self.remaining_words = list(word_dict.items())
        self.current_word = None
        self.translation_on = False

        # Learning mode chose in options_window
        self.learning_mode = learning_mode

    #Return next word (word or translation)
    def get_next_word(self):
            self.translation_on = False
            if not self.remaining_words:
                return False
            self.current_word = random.choice(self.remaining_words)
            if self.learning_mode == "English to Polish":
                return self.current_word[0]

            else:
                return self.current_word[1]

    #Set word as known and remove from list of remaining words
    def mark_known(self):
        self.remaining_words.remove(self.current_word)

    #Return word translation
    def get_translation(self):
        if self.current_word:
            self.translation_on = True
            if self.learning_mode == "English to Polish":
                return self.current_word[1]

            else:
                return self.current_word[0]
        return None

    #Return the word
    def get_word(self):
        if self.current_word:
            self.translation_on = False
            if self.learning_mode == "English to Polish":
                return self.current_word[0]
            else:
                return self.current_word[1]
        return None




