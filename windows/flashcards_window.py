from tkinter import *

from .base_window import BaseWindow
from logic.app_data import AppData
from logic.flashcards_engine import FlashcardEngine

class FlashcardsWindow(BaseWindow):
    def __init__(self,app_data, learning_mode):
        super().__init__("Flashcards mode")
        self.app_data: AppData = app_data
        self.learning_mode = learning_mode
        self.flashcard_engine = FlashcardEngine(self.app_data.word_dict, self.learning_mode)
        self.build_interface()

        self.window.bind("<Left>", self.on_click_no)
        self.window.bind("<Right>", self.on_click_yes)
        self.window.bind("<space>", self.on_click_flashcard_button)

    def build_interface(self):
        go_back_button = Button(self.window, command=self.on_click_go_back, text="⬅️", font=("helvetica", 30))
        go_back_button.pack(anchor="nw")

        frame = Frame(self.window)
        frame.place(relx=0.5, rely=0.5, relwidth=0.5, relheight=0.8, anchor="center")

        self.progress_counter_label = Label(frame, text="0/"+str(len(self.app_data.word_dict)), font=("helvetica", 16, "bold"))
        self.progress_counter_label.pack(fill="x", pady=(10,5))

        self.flashcard_button = Button(frame, command=self.on_click_flashcard_button, text="", font=("helvetica", 32), wraplength=300, justify="center")
        self.flashcard_button.pack(expand=True, fill="both", pady=5)

        self.fail_button = Button(frame, command=self.on_click_no, text="No", font=("helvetica", 14))
        self.fail_button.pack(expand=True, fill="x", side=LEFT, padx=5)

        self.success_button = Button(frame, command=self.on_click_yes, text="Yes", font=("helvetica", 14))
        self.success_button.pack(expand=True, fill="x", side=LEFT, padx=5, pady=20)

        self.window.after(100, self.update_wraplength)
        self.show_word_on_the_beginning()

    def on_click_flashcard_button(self, event=None):
        if self.flashcard_engine.translation_on:
            self.flashcard_button.config(text=self.flashcard_engine.get_word(), fg="#f8f9fa")

        else:
            self.flashcard_button.config(text=self.flashcard_engine.get_translation(), fg="#adb5bd")

    def on_click_yes(self, event=None):
        self.flashcard_engine.mark_known()
        result = self.flashcard_engine.get_next_word()
        if result:
            self.flashcard_button.config(text=result, fg="#f8f9fa")
            self.progress_update()
        else:
            self.progress_update()
            self.flashcard_button.config(text="All done! 🎉", state="disabled")
            self.fail_button.config(state="disabled")
            self.success_button.config(state="disabled")
            self.window.unbind("<Left>")
            self.window.unbind("<Right>")
            self.window.unbind("<space>")

    def on_click_no(self, event=None):
        result = self.flashcard_engine.get_next_word()
        self.flashcard_button.config(text=result, fg="#f8f9fa")

    def show_word_on_the_beginning(self):
        word = self.flashcard_engine.get_next_word()
        self.flashcard_button.config(text=word, fg="#f8f9fa", activeforeground="#f8f9fa")

    def progress_update(self):
        known = len(self.app_data.word_dict)-len(self.flashcard_engine.remaining_words)
        self.progress_counter_label.config(text=f"{known}/{len(self.app_data.word_dict)}")


    def on_click_go_back(self):
        from .options_window import Options
        previous_window = Options(self.app_data, "flashcards")
        self.destroy()
        previous_window.run()

    def update_wraplength(self):
        width = self.flashcard_button.winfo_width()
        self.flashcard_button.config(wraplength=width * 0.9)