import re
#Components import
from .flashcards_engine import FlashcardEngine

#Main engine of Learning mode work (inheritance from FlashcardsEngine because of a lot of similarity)
class LearningEngine(FlashcardEngine):
    def __init__(self, word_dict, learning_mode):
        super().__init__(word_dict, learning_mode)
        self.fail_counter=0


    #Return the correct answer to check out
    def prepare_answer_string(self):
        #Ignore the text in brackets
        correct_answer_clean = re.sub(r"\([^)]*\)", "", str(self.get_translation()))

        #Prepare correct variants of answer
        correct_variants = [variant.strip() for variant in correct_answer_clean.split(",")]

        return correct_variants




