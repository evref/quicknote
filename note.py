import tkinter as tk

from tkutils import center_window
from const import *
import menu

def quick_note(path):
    window = tk.Tk()
    
    window.title("Quicknote")
    entry = tk.Entry(
        fg=FG_WHITE, 
        bg=BG_GREY, 
        font=("Consolas", 40),
        width=40)
    entry.pack()
    entry.focus_set()

    center_window(window)

    def on_enter_pressed(event):
        entered_text = entry.get()
        window.destroy()

        list_file = open(path, "a")
        list_file.write(entered_text + "\n")
        list_file.close()
        menu.main_menu(path)

    def on_escape_pressed(event):
        window.destroy()
        menu.main_menu(path)

    entry.bind('<Return>', on_enter_pressed)
    entry.bind('<Escape>', on_escape_pressed)

    window.mainloop()
