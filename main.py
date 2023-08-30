import os

from menu import main_menu

def create_save_path():
    path = os.path.join(os.path.dirname(__file__), "data")

    if not os.path.exists(path):
        os.makedirs(path)

    path = os.path.join(path, "note_list.txt")

    if not os.path.exists(path):
        open(path, "x")
    
    return path

save_path = create_save_path()
main_menu(save_path)
