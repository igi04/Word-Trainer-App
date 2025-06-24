from ttkbootstrap import Style
from tkinter import *

class BaseWindow:
    def __init__(self, title="Word Trainer App", style="superhero"):
        self.window = Tk()
        self.style = Style(theme=style)
        self.window.title(title)
        self.set_geometry()
        # self.window.configure(bg=self.style.colors.bg)
        # self.set_styles()
    def set_geometry(self):
        screen_width = self.window.winfo_screenwidth()
        screen_height = self.window.winfo_screenheight()
        width = int(screen_width * 0.8)
        height = int(screen_height * 0.6)
        x = (screen_width - width) // 2
        y = (screen_height - height) // 2
        self.window.geometry(f"{width}x{height}+{x}+{y}")

    # def set_styles(self):
    #     # Style
    #     my_button_style = ttk.Style()
    #     my_button_style.configure('light.Outline.TButton', font=("Helvetica", 30))
    #
    #     my_radio_style = ttk.Style()
    #     my_radio_style.configure("success.TRadiobutton", font=("Helvetica", 30), bootstyle="success-round-toggle")

    def run(self):
        self.window.mainloop()

    def destroy(self):
        self.window.destroy()