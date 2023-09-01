import tkinter as tk

from tkutils import center_window
from const import *
import menu

def quick_note(path):
    window = tk.Tk()
    
    window.title("Quicknote")
    window.config(bg=BG_GREY)
    entry = tk.Entry(
        fg=FG_WHITE, 
        bg=BG_GREY, 
        insertbackground=FG_WHITE,
        font=("Consolas", 40),
        width=40)
    entry.pack()
    entry.focus_set()

    center_window(window)

    def on_enter_pressed(event):
        entered_text = entry.get()
        window.destroy()
        if len(entered_text) <= 0:
            return

        list_file = open(path, "a")
        list_file.write(entered_text + "\n")
        list_file.close()

    def on_escape_pressed(event):
        window.destroy()

    def on_menu_pressed(event):
        window.destroy()
        menu.main_menu(path)

    entry.bind('<Return>', on_enter_pressed)
    entry.bind('<Escape>', on_escape_pressed)
    entry.bind('q', on_escape_pressed)
    entry.bind('<Control-m>', on_menu_pressed)

    window.mainloop()
