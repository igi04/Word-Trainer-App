from tkinter import *
import re
import ttkbootstrap as ttk

from .base_window import BaseWindow
from logic.learning_engine import LearningEngine
from logic.app_data import AppData
from .sumarry_window import SummaryWindow
from .flashcards_window import FlashcardsWindow

class LearningWindow(BaseWindow):
    def __init__(self, app_data, learning_mode):
        super().__init__(title="Learning mode")
        self.learning_mode = learning_mode
        self.app_data: AppData = app_data
        self.learning_engine = LearningEngine(self.app_data.word_dict, self.learning_mode)
        self.build_interface()
        self.window.bind("<Return>", self.submit_answer)

    def build_interface(self):
        go_back_button = Button(self.window, command=self.on_click_go_back, text="⬅️", font=("helvetica", 30))
        go_back_button.pack(anchor="nw")

        frame = Frame(self.window, bg="lightblue")
        frame.place(relx=0.5, rely=0.5, relwidth=0.7, relheight=0.8, anchor="center")

        self.progress_counter_label = Label(frame, text="0/" + str(len(self.app_data.word_dict)), font=("helvetica", 16, "bold"))
        self.progress_counter_label.pack(pady=(100, 5))

        self.question_label = Label(frame, font=("Helvetica", 30), text="", wraplength=600, justify="center")
        self.question_label.pack(expand=True, pady=20)

        input_frame = Frame(frame)
        input_frame.pack(fill="x", pady=(10, 20))

        self.answer_entry = Entry(input_frame, font=("Helvetica", 25))
        self.answer_entry.pack(side=LEFT, expand=True, fill="x", padx=(0, 10))

        self.submit_button = Button(input_frame, command=self.submit_answer, text="Submit", font=("Helvetica", 25))
        self.submit_button.pack(side=LEFT)

        self.feedback_label = Label(frame, text="")
        self.feedback_label.pack(pady=(10, 0))

        self.show_word_on_the_beginning()

    def on_click_go_back(self):
        from .options import Options
        previous_window = Options(self.app_data, "learning")
        self.destroy()
        previous_window.run()

    def submit_answer(self, event=None):
        user_answer = str(self.answer_entry.get().lower().strip())
        correct_answer = str(self.learning_engine.get_translation()).lower()
        self.answer_entry.delete(0,END)

        if user_answer in self.learning_engine.prepare_answer_string():
            self.learning_engine.mark_known()
            self.feedback_label.config(text=f"✅ You are correct! Answer: {correct_answer.upper()}", fg="green", font=("Helvetica", 16, "bold"))
            self.window.after(2000, lambda: self.feedback_label.config(text=""))

            result = self.learning_engine.get_next_word()
            if result:
                self.question_label.config(text=result)
                self.progress_update()
            else:
                self.answer_entry.config(state="disabled")
                self.submit_button.config(state="disabled")
                self.question_label.config(text="All done! 🎉")
                self.window.after(2000, lambda: self.show_summary())

        else:
            self.learning_engine.fail_counter += 1
            self.feedback_label.config(text=f"❌ Wrong answer! Correctly: {correct_answer.upper()}", fg="red", font=("Helvetica", 16, "bold"))
            self.window.after(2800, lambda: self.feedback_label.config(text=""))
            self.question_label.config(text=self.learning_engine.get_next_word())

        self.progress_update()

    def give_question(self):
        self.question_label.config(text=self.learning_engine.get_translation())

    def show_word_on_the_beginning(self):
        word = self.learning_engine.get_next_word()
        self.question_label.config(text=word)

    def progress_update(self):
        known = len(self.app_data.word_dict)-len(self.learning_engine.remaining_words)
        self.progress_counter_label.config(text=f"{known}/{len(self.app_data.word_dict)}")

    def show_summary(self):
        summary = SummaryWindow(self.app_data, self.learning_engine.fail_counter)
        self.destroy()
        summary.run()