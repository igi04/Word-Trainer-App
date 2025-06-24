from tkinter import filedialog
from tkinter import messagebox

#The works of file and data load
class FileLoader:
    def __init__(self, app_data, window):
        self.app_data = app_data
        self.window = window

    #Launch works of file loading
    def load_file_dialog(self):
        file_types = [("Text files", "*.txt")]

        #Validation of exceptions
        try:
            self.app_data.filepath = filedialog.askopenfilename(title="Choose set to exercise",
                                                                filetypes=file_types)

            self.app_data.word_dict = self.parse_txt_file(self.app_data.filepath)

            if len(self.app_data.word_dict) == 0:
                messagebox.showerror("Error",
                                     "Your file is empty or contains invalid form of learning set ")
            else:
                messagebox.showinfo("Success",
                                    "Your set was loaded properly")

        except:
            messagebox.showerror("Error",
                                 "Something went wrong with loading file. Try again")

    #Load the data form selected file
    def parse_txt_file(self, file_path):
        self.app_data.word_dict.clear()
        with open(file_path, "r", encoding="utf-8") as f:
            for line in f:
                if "-" in line:
                    word, translation = line.strip().split("-",1)
                    self.app_data.word_dict[word.strip()] = translation.strip()

        return self.app_data.word_dict