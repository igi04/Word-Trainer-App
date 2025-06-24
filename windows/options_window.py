from tkinter import *

#Components import
from .base_window import BaseWindow

class Options(BaseWindow):
    def __init__(self, app_data, mode):
        super().__init__("Options window")
        self.app_data = app_data
        self.mode = mode
        self.option_selected = StringVar()

        self.build_interface()

    def build_interface(self):
        go_back_button = Button(self.window,
                                command=self.on_click_go_back,
                                text="⬅️", font=("helvetica", 30))
        go_back_button.pack(anchor="nw")

        frame = Frame(self.window)
        frame.place(relx=0.5, rely=0.5, anchor="center")

        label = Label(frame,
                      text="Choose the option for your learning",
                      font=("Helvetica", 30, "bold"))
        label.pack()

        #List of radiobutton options
        options_list = ["English to Polish", "Polish to English"]

        #Create a Tkinter Variable to Keep Track of everything
        self.option_selected.set("English to Polish")

        #Show RadioButtons
        for option in options_list:
            radiobutton = Radiobutton(frame,
                                          text=option,
                                          variable=self.option_selected,
                                          value=option,
                                          font=("Helvetica", 28))
            radiobutton.pack(side=TOP, pady=40)

        submit_button = Button(frame,
                               command=self.on_start_click,
                               text="Start Learning",
                               font=("Helvetica", 25))
        submit_button.pack(padx=10)

    # The works of launching new windows
    def on_click_go_back(self):
        from .mode_selection_window import ModeSelection

        previous_window = ModeSelection(self.app_data)
        self.destroy()
        previous_window.run()

    def on_start_click(self):
        if self.mode == "learning":
            from .learning_window import LearningWindow

            next_window = LearningWindow(self.app_data, self.option_selected.get())
            self.destroy()
            next_window.run()
        if self.mode == "flashcards":
            from .flashcards_window import FlashcardsWindow

            next_window = FlashcardsWindow(self.app_data, self.option_selected.get())
            self.destroy()
            next_window.run()
