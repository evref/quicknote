import os

from note import quick_note
from menu import main_menu


def create_save_path():
    home = os.path.expanduser("~")
    path = os.path.join(home, "projects/evref/local-scripts/quicknote/data")

    if not os.path.exists(path):
        raise Exception("Save directory does not exist")

    path = os.path.join(path, "note_list.txt")
    
    return path

save_path = create_save_path()
quick_note(save_path)
#main_menu(save_path)
