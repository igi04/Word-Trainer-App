from tkinter import *
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt

from .base_window import BaseWindow

class SummaryWindow(BaseWindow):
    def __init__(self, app_data, fail_counter):
        super().__init__("Session Summary")
        self.app_data = app_data
        self.fail_counter = fail_counter
        self.total_words = len(self.app_data.word_dict)
        self.success_count = self.total_words - self.fail_counter

        self.build_interface()
    def build_interface(self):
        # Title label
        title = Label(self.window, text="Learning Summary", font=("Helvetica", 30, "bold"))
        title.pack(pady=20)

        # Text summary
        summary_text = f"✅ Correct: {self.success_count}\n❌ Incorrect: {self.fail_counter}"
        summary_label = Label(self.window, text=summary_text, font=("Helvetica", 18))
        summary_label.pack(pady=18)

        #Bar chart
        self.plot_summary_chart()

        # Back to menu
        back_btn = Button(self.window, command=self.back_to_menu, text="Back to Menu", font=("Helvetica", 25, "bold"))
        back_btn.pack(pady=18)


    def back_to_menu(self):
        from .mode_selection_window import ModeSelection
        previous_window = ModeSelection(self.app_data)
        self.destroy()
        previous_window.run()

    def plot_summary_chart(self):
        fig, ax = plt.subplots(figsize=(4, 3), dpi=100, facecolor='#f0f0f0')
        categories = ['Correct', 'Incorrect']
        values = [self.success_count, self.fail_counter]
        colors = ['green', 'red']
        ax.bar(categories, values, color=colors)
        ax.set_title("Answers Overview")
        ax.set_ylabel("Number of Words")
        ax.set_ylim(0, max(values) + 1)

        canvas = FigureCanvasTkAgg(fig, master=self.window)
        canvas.draw()
        canvas.get_tk_widget().pack()

        plt.close(fig)
