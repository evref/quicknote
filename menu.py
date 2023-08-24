import tkinter as tk

from tkutils import center_window
from const import *


def load_notes(path):
    file = open(path, "r")
    notes = []
    for line in file:
        line = line.strip("\n")
        notes.append(line)
    return notes

def main_menu(path):
    notes = load_notes(path)
    print(notes)
    
    window = tk.Tk()
    window.title("Quicknote")

    def on_escape_pressed(event):
        window.destroy()


    note_lbls = []
    note_btns = []

    def strike_note(index):
        note_lbls[index]["font"] = ("Consolas", 20, "overstrike")
        note_lbls[index].pack()
        
    for i in range(len(notes)):
        note_btns.append(tk.Button(text="*"), command=strike_note(i))
        note_btns[i].pack()
        
        note_lbls.append(tk.Label(text=notes[i], fg=FG_WHITE, bg=BG_GREY, font=("Consolas", 20)))
        note_lbls[i].pack()

    center_window(window, 0.2)

    window.bind("<Escape>", on_escape_pressed)

    window.mainloop()


