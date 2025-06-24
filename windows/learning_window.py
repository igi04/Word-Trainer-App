from tkinter import *

#Components import
from .base_window import BaseWindow
from logic.learning_engine import LearningEngine
from logic.app_data import AppData
from .sumarry_window import SummaryWindow

class LearningWindow(BaseWindow):
    def __init__(self, app_data, learning_mode):
        super().__init__(title="Learning mode")
        # Learning mode chose in options_window
        self.learning_mode = learning_mode

        self.app_data: AppData = app_data
        self.learning_engine = LearningEngine(self.app_data.word_dict, self.learning_mode)
        self.build_interface()

        # Bind buttons to ease learning mode work
        self.window.bind("<Return>", self.submit_answer)

    def build_interface(self):
        go_back_button = Button(self.window,
                                command=self.on_click_go_back,
                                text="⬅️",
                                font=("helvetica", 30))
        go_back_button.pack(anchor="nw")

        frame = Frame(self.window)
        frame.place(relx=0.5, rely=0.5, relwidth=0.7, relheight=0.8, anchor="center")

        self.progress_counter_label = Label(frame,
                                            text="0/" + str(len(self.app_data.word_dict)),
                                            font=("helvetica", 16, "bold"))
        self.progress_counter_label.pack(pady=(100, 5))

        self.question_label = Label(frame,
                                    font=("Helvetica", 30),
                                    text="",
                                    wraplength=600,
                                    justify="center")
        self.question_label.pack(expand=True, pady=20)

        input_frame = Frame(frame)
        input_frame.pack(fill="x", pady=(10, 20))

        self.answer_entry = Entry(input_frame,
                                  font=("Helvetica", 25))
        self.answer_entry.pack(side=LEFT, expand=True, fill="x", padx=(0, 10))

        self.submit_button = Button(input_frame,
                                    command=self.submit_answer,
                                    text="Submit",
                                    font=("Helvetica", 25))
        self.submit_button.pack(side=LEFT)

        self.feedback_label = Label(frame,
                                    text="")
        self.feedback_label.pack(pady=(10, 0))

        # Show the word on the beginning of app work
        self.show_word_on_the_beginning()

    # The works of launching new window
    def on_click_go_back(self):
        from .options_window import Options

        previous_window = Options(self.app_data, "learning")
        self.destroy()
        previous_window.run()

    #Submit and check the answer
    def submit_answer(self, event=None):
        user_answer = str(self.answer_entry.get().lower().strip())
        correct_answer = str(self.learning_engine.get_translation()).lower()
        self.answer_entry.delete(0,END)

        if user_answer in self.learning_engine.prepare_answer_string():
            self.learning_engine.mark_known()
            self.feedback_label.config(text=f"✅ You are correct! Answer: {correct_answer.upper()}",
                                       fg="green",
                                       font=("Helvetica", 16, "bold"))

            #Show the feedback label for 2s
            self.window.after(2000, lambda: self.feedback_label.config(text=""))

            #The works of showing new word or ending learning because of no words
            result = self.learning_engine.get_next_word()
            if result:
                self.question_label.config(text=result)
                self.progress_update()
            else:
                self.answer_entry.config(state="disabled")
                self.submit_button.config(state="disabled")
                self.question_label.config(text="All done! 🎉")

                #Unbind the button
                self.window.unbind("<Return>")

                #Wait to launch summary window
                self.window.after(1500, lambda: self.show_summary())

        else:
            self.learning_engine.fail_counter += 1
            self.feedback_label.config(text=f"❌ Wrong answer! Correctly: {correct_answer.upper()}",
                                       fg="red",
                                       font=("Helvetica", 16, "bold"))

            # Show the feedback label for 3s
            self.window.after(3000, lambda: self.feedback_label.config(text=""))

            #Show next word
            self.question_label.config(text=self.learning_engine.get_next_word())

        self.progress_update()

    def give_question(self):
        self.question_label.config(text=self.learning_engine.get_translation())

    def show_word_on_the_beginning(self):
        word = self.learning_engine.get_next_word()
        self.question_label.config(text=word)

    #Updating the progress label
    def progress_update(self):
        known = len(self.app_data.word_dict)-len(self.learning_engine.remaining_words)
        self.progress_counter_label.config(text=f"{known}/{len(self.app_data.word_dict)}")

    #Show the summary window
    def show_summary(self):
        summary = SummaryWindow(self.app_data, self.learning_engine.fail_counter)
        self.destroy()
        summary.run()