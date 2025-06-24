#Components import
from windows.load_file_window import LoadFileGUI
from logic.app_data import AppData

def main():
    #Initialize app
    app_data = AppData()
    load_file_window = LoadFileGUI(app_data)
    load_file_window.run()

if __name__ == '__main__':
    main()