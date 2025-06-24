from ttkbootstrap import Style
from tkinter import *

#Base window from which every another window inheritances
class BaseWindow:
    def __init__(self, title="Word Trainer App", style="superhero"):
        #Create Tk() object
        self.window = Tk()

        #Set style theme from ttkbootstrap
        self.style = Style(theme=style)

        self.window.title(title)
        self.set_geometry()

    # Set responsive geometry of window
    def set_geometry(self):
        screen_width = self.window.winfo_screenwidth()
        screen_height = self.window.winfo_screenheight()
        width = int(screen_width * 0.8)
        height = int(screen_height * 0.6)
        x = (screen_width - width) // 2
        y = (screen_height - height) // 2
        self.window.geometry(f"{width}x{height}+{x}+{y}")

    #Run the window
    def run(self):
        self.window.mainloop()

    #Destroy the window
    def destroy(self):
        self.window.destroy()