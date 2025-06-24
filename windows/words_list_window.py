from tkinter import *

from .base_window import BaseWindow
from logic.app_data import AppData

class WordsListWindow(BaseWindow):
    def __init__(self, app_data):
        super().__init__(title="List of your words")
        self.app_data: AppData = app_data
        self.build_interface()

    def build_interface(self):
        go_back_button = Button(self.window, command=self.on_click_go_back, text="⬅️", font=("helvetica", 30))
        go_back_button.pack(anchor="nw")

        scrollbar = Scrollbar(self.window)
        scrollbar.pack(side="right", fill="y")
        text = Text(self.window, font=("Helvetica", 20), yscrollcommand=scrollbar.set, spacing3=20)
        text.pack(expand=True, fill="both")
        scrollbar.config(command=text.yview())

        #Tags configuration
        text.tag_config("center", justify="center")
        text.tag_config("eng", foreground="red", font=("Helvetica", 16))
        text.tag_config("pl", font=("Helvetica", 16, "bold"))

        for word, translation in self.app_data.word_dict.items():
            text.insert("end", word+"   ", ("eng","center"))
            text.insert("end", "-", "center")
            text.insert("end", "   "+translation+ "\n",("pl","center"))

        text.config(state="disabled")


    def on_click_go_back(self):
        from .mode_selection_window import ModeSelection
        previous_window = ModeSelection(self.app_data)
        self.destroy()
        previous_window.run()