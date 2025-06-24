import re
from .flashcards_engine import FlashcardEngine

class LearningEngine(FlashcardEngine):
    def __init__(self, word_dict, learning_mode):
        super().__init__(word_dict, learning_mode)
        self.fail_counter=0


    def prepare_answer_string(self):
        correct_answer_clean = re.sub(r"\([^)]*\)", "", str(self.get_translation()))
        correct_variants = [variant.strip() for variant in correct_answer_clean.split(",")]
        return correct_variants




