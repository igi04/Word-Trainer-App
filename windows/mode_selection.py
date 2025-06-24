from tkinter import *
from .base_window import BaseWindow
from logic.app_data import AppData
from .words_list_window import WordsListWindow
from .flashcards_window import FlashcardsWindow
from .learning_window import LearningWindow
from .options import Options

class ModeSelection(BaseWindow):
    def __init__(self, app_data):
        super().__init__("Game mode window")
        self.app_data: AppData = app_data
        self.build_interface()

    def build_interface(self):
        go_back_button = Button(self.window, command=self.on_click_go_back, text="⬅️", font=("helvetica", 30))
        go_back_button.pack(anchor="nw")

        label = Label(self.window, text="Choose the game mode you are interested in", font=("Helvetica", 27, "bold"))
        label.pack(pady=50)

        button_flashcards = Button(self.window, command=self.on_click_flashcards, text="FLASH CARDS", font=("Helvetica", 27, "bold"))
        button_flashcards.pack(expand=True, padx=10, pady=10)

        button_learning = Button(self.window, command=self.on_click_learning, text="LEARNING", font=("Helvetica", 30, "bold"))
        button_learning.pack(expand=True, padx=10, pady=10)

        button_words = Button(self.window, command=self.on_click_words_list, text="LIST OF WORDS", font=("Helvetica", 27, "bold"))
        button_words.pack(expand=True, padx=10, pady=10)



    def on_click_words_list(self):
        next_window = WordsListWindow(self.app_data)
        self.destroy()
        next_window.run()

    def on_click_learning(self):
        mode = "learning"
        next_window = Options(self.app_data, mode)
        self.destroy()
        next_window.run()

    def on_click_flashcards(self):
        mode = "flashcards"
        next_window = Options(self.app_data, mode)
        self.destroy()
        next_window.run()

    def on_click_go_back(self):
        from .load_file_GUI import LoadFileGUI
        previous_window = LoadFileGUI(self.app_data)
        self.destroy()
        previous_window.run()