#Main storage of data in all app. An object creating once, in main.py, then convey from class to class
class AppData:
    def __init__(self):
        self.word_dict = {}
        self.filepath = ""