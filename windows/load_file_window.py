from tkinter import *

from .base_window import BaseWindow
from logic.file_loader import FileLoader
from .mode_selection_window import ModeSelection
from logic.app_data import AppData

class LoadFileGUI(BaseWindow):
    def __init__(self, app_data):
        super().__init__(title="Load File to Exercise")
        self.file_loader = FileLoader(app_data, self.window)
        self.app_data: AppData = app_data
        self.build_interface()

    def build_interface(self):
        label = Label(self.window, text="Word Trainer App", font=("Helvetica", 35, "bold"))
        label.pack(pady=(150,40))

        button = Button(self.window, command=self.on_load_click, text="Load set to exercise", font=("Helvetica", 30, "bold"))
        button.pack(expand=True, padx=10, pady=10)


    def on_load_click(self):
        #Called function load_file_dialog() from file_loader.py
        self.file_loader.load_file_dialog()

        if len(self.app_data.word_dict) != 0:
            next_window = ModeSelection(self.app_data)
            self.destroy()
            next_window.run()
