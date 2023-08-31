import os
import argparse

from menu import main_menu
from note import quick_note

parser = argparse.ArgumentParser(description = "A GUI notetaking program")

parser.add_argument('-m', '--menu', action='store_true')

args = parser.parse_args()


def create_save_path():
    path = os.path.join(os.path.dirname(__file__), "data")

    if not os.path.exists(path):
        os.makedirs(path)

    path = os.path.join(path, "note_list.txt")

    if not os.path.exists(path):
        open(path, "x")
    
    return path

save_path = create_save_path()

if args.menu:
    main_menu(save_path)
else:
    quick_note(save_path)
